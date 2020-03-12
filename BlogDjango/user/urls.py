from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/user',UserViewSet,'user') #the api/user is the api call!

urlpatterns = router.urls