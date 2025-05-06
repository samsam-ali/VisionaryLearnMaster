from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class ImageCaption(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    caption = models.CharField(max_length=255, default="No caption created")
    def __str__(self):
        return self.caption

from django.dispatch import receiver
from django.db.models.signals import post_save
@receiver(post_save, sender=ImageCaption)
def generate_caption(sender, instance, created, **kwargs):
    if created and instance.image:
        import requests

        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        headers = {"Authorization": "Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}

        def query(filename):
            with open(filename, "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        image_file = instance.image.path
        instance.caption = query(image_file)[0]['generated_text']
        instance.save()


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"
        ADMIN = "ADMIN", "Admin"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.username

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)

class Student(User):
    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"

class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)

class Teacher(User):
    base_role = User.Role.TEACHER

    teacher = TeacherManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for teachers"

class Course(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    imagecaption = models.ForeignKey(ImageCaption, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # weight = models.FloatField()

    def __str__(self):
        return self.title

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    imagecaption = models.ForeignKey(ImageCaption, on_delete=models.CASCADE, null=True, blank=True) 
    text = models.TextField()

    def __str__(self):
        return self.title
    

