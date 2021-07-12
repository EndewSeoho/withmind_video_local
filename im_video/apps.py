from django.apps import AppConfig
import cv2
import torch
import os
from .model import *
import torchvision

# class ImVideoConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'im_video'


class ImConfig(AppConfig):
    name = 'im_video'

    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    # os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def get_state_dict(origin_dict):
        old_keys = origin_dict.keys()
        new_dict = {}

        for ii in old_keys:
            temp_key = str(ii)
            if temp_key[0:7] == "module.":
                new_key = temp_key[7:]
            else:
                new_key = temp_key

            new_dict[new_key] = origin_dict[temp_key]
        return new_dict

    FD_Net = cv2.dnn.readNetFromCaffe("C:/Users/withmind/Desktop/models/opencv_ssd.prototxt", "C:/Users/withmind/Desktop/models/opencv_ssd.caffemodel")

    Landmark_Net = LandmarkNet(3, 3)
    # Landmark_Net = torch.nn.DataParallel(Landmark_Net).to(device)
    Landmark_Net = Landmark_Net.to(device)
    Landmark_Net.load_state_dict(torch.load("C:/Users/withmind/Desktop//models/ETRI_LANDMARK_68pt.pth.tar", map_location=device)['state_dict'])

    Headpose_Net = HeadposeNet(torchvision.models.resnet.Bottleneck, [3, 4, 6, 3], 66)
    Headpose_Net = Headpose_Net.to(device)
    Headpose_Net.load_state_dict(torch.load("C:/Users/withmind/Desktop/models/ETRI_HEAD_POSE.pth.tar"))

    Emotion_Net = EmotionNet(num_classes=7).to(device)
    new_dict = get_state_dict(torch.load("C:/Users/withmind/Desktop/models/ETRI_Emotion.pth.tar")['state_dict'])
    # new_dict = get_state_dict(torch.load("/home/ubuntu/projects/withmind_video/im_video/file/ETRI_EMOTION.pth.tar")['state_dict'])
    Emotion_Net.load_state_dict(new_dict)