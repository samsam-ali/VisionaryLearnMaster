# api/urls.py
from django.urls import re_path, path
from . import views

urlpatterns = [
   re_path('login', views.login, name='login'),
   re_path('signup_student', views.signup_student, name='signup_student'),
   re_path('signup_teacher', views.signup_teacher, name='signup_teacher'),
   re_path('test_token', views.test_token),
   re_path('get_user', views.get_user),
   re_path('get_teachers', views.get_teachers),
   re_path('add_course', views.add_course, name="add_course"),
   re_path('get_courses', views.get_courses),
   path('get_course/<int:course_id>/', views.get_course, name="get_course"),
   re_path('add_lesson', views.add_lesson, name="add_lesson"),
   path('get_lesson/<int:lesson_id>/', views.get_lesson, name="get_lesson"),
   re_path('get_lessons', views.get_lessons),
   path('get_lesson_topics/<int:lesson_id>/', views.get_lesson_topics, name="get_lesson_topics"),
   path('get_course_lessons/<int:course_id>/', views.get_course_lessons),
   re_path('add_topic', views.add_topic, name="add_topic"),
   path('get_topic/<int:topic_id>/', views.get_topic),
   re_path('add_question', views.add_question, name="add_question"),
   path('get_assignment/<int:assignment_id>/', views.get_assignment, name="get_assignment"),
   path('get_assignment_questions/<int:assignment_id>/', views.get_assignment_questions, name="get_assignment_questions"),
   re_path('add_assignment', views.add_assignment, name="add_assignment"),
   path('get_lesson_assignments/<int:lesson_id>/', views.get_lesson_assignments),
   re_path('add_assignment', views.add_assignment),
   re_path('add_choice', views.add_choice, name="add_choice"),
   path('get_question_choices/<int:question_id>/', views.get_question_choices, name="get_question_choices"),
   path('add-image-caption/', views.AddImageCaption.as_view(), name='add_image_caption'),
   path('get_imagecaption/<int:imagecaption_id>/', views.get_imagecaption),
]
