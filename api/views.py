from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, CourseSerializer, GetTeacherSerializer, GetCourseSerializer, GetLessonSerializer, TopicSerializer, AssignmentSerializer, QuestionSerializer, ChoiceSerializer, GetQuestionSerializer, ImageCaptionSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import AbstractUser
from .models import Student, Teacher, Course, Lesson, Topic, Assignment, Question, Choice, ImageCaption

from django.shortcuts import get_object_or_404

def frontpage(request):
    return render(request,'lms/frontpage.html')


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = None

    student = Student.objects.filter(username=username).first()
    
    if student and student.check_password(password):
        user = student
    else:
        teacher = Teacher.teacher.filter(username=username).first()
        print(teacher)
        if teacher and teacher.check_password(password):
            user = teacher
        else:
            return Response({"detail": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup_student(request):
    # initialise serializer based on request data
    serializer = StudentSerializer(data=request.data)
    
    # if data is valid: save user in database
    if serializer.is_valid():
        student = serializer.save()
        # retrieve student and create token
        # student = Student.objects.get(username=request.data['username'])
        # for security saves hashed password
        student.set_password(request.data['password'])
        student.role = Student.Role.STUDENT
        student.save()
        token = Token.objects.create(user=student)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup_teacher(request):
    # initialise serializer based on request data
    serializer = TeacherSerializer(data=request.data)
    
    # if data is valid: save user in database
    if serializer.is_valid():
        teacher = serializer.save()
        # retrieve student and create token
        # teacher = Teacher.objects.get(username=request.data['username'])
        # for security saves hashed password
        teacher.set_password(request.data['password'])
        teacher.role = Student.Role.TEACHER
        teacher.save()
        token = Token.objects.create(user=teacher)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_lesson(request):
    serializer = GetLessonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    serializer = GetLessonSerializer(lesson)
    return Response(serializer.data)

@api_view(['GET'])
def get_lessons(request):
    lessons = Lesson.objects.all()
    serializer = GetLessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_teachers(request):
    teachers = Teacher.teacher.all()
    serializer = GetTeacherSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_question(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_lesson_assignments(request, lesson_id):
    assignments = Assignment.objects.filter(lesson=lesson_id)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_assignment_questions(request, assignment_id):
    questions = Question.objects.filter(assignment=assignment_id)
    serialized_data = []

    for question in questions:
        choices = Choice.objects.filter(question=question)
        serializer = GetQuestionSerializer(question)
        serialized_question = serializer.data
        serialized_question['choices'] = ChoiceSerializer(choices, many=True).data
        serialized_data.append(serialized_question)

    return Response(serialized_data)

@api_view(['GET'])
def get_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    serializer = AssignmentSerializer(assignment)
    return Response(serializer.data)

@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = GetCourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    serializer = GetCourseSerializer(course)
    return Response(serializer.data)

@api_view(['GET'])
def get_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    serializer = TopicSerializer(topic)
    return Response(serializer.data)

@api_view(['POST'])
def add_topic(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_assignment(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_choice(request):
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_question_choices(request, question_id):
    choices = Choice.objects.filter(question=question_id)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_lesson_topics(request, lesson_id):
    topics = Topic.objects.filter(lesson=lesson_id)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_course_lessons(request, course_id):
    lessons = Lesson.objects.filter(course=course_id)
    serializer = GetLessonSerializer(lessons, many=True)
    return Response(serializer.data)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    
    return Response("passed for {}".format(request.user.email))


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


# ------------------------------MODEL TESTING------------------------------------------------



from rest_framework.views import APIView


class AddImageCaption(APIView):
    def post(self, request, format=None):
        serializer = ImageCaptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_imagecaption(request, imagecaption_id):
    imagecaption = get_object_or_404(ImageCaption, pk=imagecaption_id)
    serializer = ImageCaptionSerializer(imagecaption)
    return Response(serializer.data)