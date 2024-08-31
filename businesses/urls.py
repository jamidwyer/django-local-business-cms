from django.urls import include, path
from rest_framework import routers
from businesses import views


router = routers.DefaultRouter()

router.register('', views.BusinessViewSet, basename='businesses')

urlpatterns = [
    path('', include(router.urls)),
]
