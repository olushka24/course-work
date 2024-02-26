from rest_framework import generics, status
from .models import Course, Client, CompletedCourse, Recomendation
from .serializers import CourseSerializer, ClientSerializer, CompletedCourseSerializer, RecomendationSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CompletedCourseList(generics.ListCreateAPIView):
    queryset = CompletedCourse.objects.all()
    serializer_class = CompletedCourseSerializer

class RecomendationList(generics.ListCreateAPIView):
    queryset = Recomendation.objects.all()
    serializer_class = RecomendationSerializer
