from django.urls import path
from . import views_vision




urlpatterns = [
    path("live/", views_vision.live_view, name="live_view"),
    path("start/", views_vision.start_camera_view, name="start_camera"),
    path("stop/", views_vision.stop_camera_view, name="stop_camera"),
    path("objects/", views_vision.objects_view, name="objects_view"),
    path("frame/", views_vision.get_frame_view, name="frame_view"),
    path("detect/", views_vision.DetectView.as_view(), name="detect"),
]
