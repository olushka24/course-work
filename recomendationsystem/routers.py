from rest_framework import routers
from backend.viewsets import CourseViewSet

router = routers.SimpleRouter()

router.register(r'course', CourseViewSet, basename="course")

urlpatterns = router.urls