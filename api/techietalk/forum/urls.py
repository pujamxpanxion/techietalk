# create this file
# rerouting all requests that have ‘api’ in the url to the <code>apps.core.urls
from django.conf.urls import url
from rest_framework import routers
from forum.views import ForumViewSet, CategoryViewSet
 
router = routers.DefaultRouter()
router.register(r'forums', ForumViewSet)
router.register(r'categories', CategoryViewSet)
 
urlpatterns = router.urls