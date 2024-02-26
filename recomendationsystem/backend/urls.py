from django.urls import path
from .views import CourseList, ClientList, CompletedCourseList, RecomendationList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('courses/', CourseList.as_view()),
    path('clients/', ClientList.as_view()),
    path('completedCourses/', CompletedCourseList.as_view()),
    path('recomendations/', RecomendationList.as_view()),
]