from django.urls import path
from album.views import *


urlpatterns = [
    path('',index,name='home'),
    path('signup',signup,name='signup'),
    path('check-name',checkName,name='checkname'),
    path('save-user',saveUser,name='saveuser'),
    path('login',login,name='login'),
    path('login-validation',loginValidation,name='loginvalidation'),
    path('logout',logout,name='logout'),
    path('my-gallery',mygallery,name='mygallery'),
    path('add-photo',makegallery,name='makegallery'),
    path('save-gallery',saveGallery,name='savegallery'),
    path('view-photo',viewPhoto,name='photo'),
    path('delete-image',deleteImage,name='deleteimage'),
    
]
