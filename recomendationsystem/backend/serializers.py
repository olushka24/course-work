from rest_framework import serializers

from backend.models import Area, Format, Categorie, Course, Client, CompletedCourse, Recomendation


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    format = FormatSerializer()
    categorie = CategorieSerializer()
    class Meta:
        model = Course
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CompletedCourseSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    course = CourseSerializer()
    class Meta:
        model = CompletedCourse
        fields = '__all__'

class RecomendationSerializer(serializers.ModelSerializer):
    completedCourse = CourseSerializer()
    recomendatedCourse = CourseSerializer()
    class Meta:
        model = Recomendation
        fields = '__all__'