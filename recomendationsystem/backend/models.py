from django.db import models

class Area(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
class Format(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
class Categorie(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.TextField()
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()
    area = models.ForeignKey(Area, related_name= "area", on_delete=models.CASCADE)
    format = models.ForeignKey(Format, related_name= "format", on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, related_name= "categorie", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
class CompletedCourse(models.Model):
    client = models.ForeignKey(Client, related_name= "client", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name= "course", on_delete=models.CASCADE)
    mark = models.IntegerField()

class Recomendation(models.Model):
    completedCourse = models.ForeignKey(Course, related_name= "completedCourse", on_delete=models.CASCADE)
    recomendatedCourse = models.ForeignKey(Course, related_name= "recomendatedCourse", on_delete=models.CASCADE)
    intersections = models.IntegerField()

