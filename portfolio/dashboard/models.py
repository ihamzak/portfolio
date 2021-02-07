from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Database(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Datascience(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Cloudskill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=500)
    credentials= models.URLField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title= models.CharField(max_length=500)
    description = models.TextField()
    github = models.URLField()

    def __str__(self):
        return self.name
    





