from django.urls import path
from . import views

app_name = 'im_video'

urlpatterns = [
    path('', views.IM_video_Anaylysis.as_view())
]