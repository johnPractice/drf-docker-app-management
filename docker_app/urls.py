from django.urls import include, path
from docker_app.routers import DockerAppStatusViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'dockerize', DockerAppStatusViewset,
                basename='docker app')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
