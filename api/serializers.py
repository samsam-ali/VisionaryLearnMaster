from rest_framework import serializers
# from django.contrib.auth.models import AbstractUser
from .models import User, Student, Teacher, Course, Question, Lesson, Topic, Assignment, Choice, ImageCaption


# map json objects from apis to entries in database
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'role']

class StudentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Student
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'role']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Teacher
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'role']

class GetTeacherSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Teacher
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

class CourseSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Course
        fields = ['id', 'title', 'teacher','imagecaption']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Question
        fields = ['id', 'assignment','title']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Choice
        fields = ['id', 'question', 'title', 'is_correct']

class GetQuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta(object):
        model = Question
        fields = ['id', 'assignment','title', 'choices']

class GetCourseSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Course
        fields = ['id', 'title', 'teacher', 'imagecaption']

class GetLessonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Lesson
        fields = ['id', 'course', 'title']

class TopicSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Topic
        fields = ['id', 'lesson','title', 'image', 'imagecaption', 'text']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Assignment
        fields = ['id', 'lesson', 'title']

class ImageCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCaption
        fields = '__all__'