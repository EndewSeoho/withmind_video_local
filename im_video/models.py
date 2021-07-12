from django.db import models

class Result(models.Model):
    userkey = models.IntegerField(null=False)
    videoNo = models.IntegerField(null=False)
    emotion_surprise = models.FloatField()
    emotion_fear = models.FloatField()
    emotion_aversion = models.FloatField()
    emotion_happy = models.FloatField()
    emotion_sadness = models.FloatField()
    emotion_angry = models.FloatField()
    emotion_neutral = models.FloatField()
    gaze = models.TextField()
    face_angle_mean = models.TextField()
    shoulder_angle_mean = models.TextField()
    shoulder_move_left = models.TextField()
    shoulder_move_right = models.TextField()
    shoulder_move_center = models.TextField()
    hand_count = models.IntegerField()
    hand_time = models.FloatField()

    class Meta:
        db_table = 'IM_video_Result'

    # def __str__(self):
    #     return self.emotion
#
# class input_data(models.Model):
#     userkey = models.IntegerField(null=False)
#     videoNo = models.IntegerField(null=False)
#     videobyte = models.TextField(null=False)
#
#     class Meta:
#         db_table = 'IM_input_data'