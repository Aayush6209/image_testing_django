from django.urls import path

from .views import *

urlpatterns = [
    path('upload/', upload_view),
    path('update/<int:pk>/', update_view),
    path('delete/<int:pk>/', delete_view),
    path('download/<int:pk>', download_view),
]