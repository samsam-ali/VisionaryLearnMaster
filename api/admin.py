from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Student, Teacher, Lesson, Assignment, Question, Choice, Topic, ImageCaption

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Topic)
admin.site.register(ImageCaption)