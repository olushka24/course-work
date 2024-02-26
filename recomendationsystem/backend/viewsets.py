from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from backend.models import Course

from backend.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]