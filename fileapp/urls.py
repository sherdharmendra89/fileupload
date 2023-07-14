from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('superusers/', views.SuperuserCreateView.as_view(), name='superuser-create'),
    path('staffusers/', views.SuperuserCreateView.as_view(), name='normaluser-create'),
    path('upload/', views.FileUploadAPI.as_view(), name='file-upload'),
    path('files/', views.FileListAPI.as_view(), name='file-list'),
    path('files/<int:pk>/', views.FileDownloadAPI.as_view(), name='file-download'),


    # path('login/', views.UserLoginView.as_view(), name='login'),
]