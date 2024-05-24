from django.urls import path, re_path, include

from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'post', PostViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    #path('api/v1/postlist/', PostViewSet.as_view({'get': 'list'})),
    #path('api/v1/postlist/<int:pk>/', PostViewSet.as_view({'put': 'update'})),
    #path('api/v1/postdetail/<int:pk>/', PostAPIDetailView.as_view()),


    path('', PostHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>/', ShowPage.as_view(), name='post'),
    path('category/<int:cat_id>/', CategoryHome.as_view(), name='category')
]


