from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Student, Teacher, Course, Lesson, Assignment, Question, Choice, Topic
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, CourseSerializer, GetTeacherSerializer, GetCourseSerializer, GetLessonSerializer, TopicSerializer, AssignmentSerializer, QuestionSerializer, ChoiceSerializer, GetQuestionSerializer, ImageCaptionSerializer

class TestSetUp(APITestCase):
    def setUp(self):
        self.signup_student_url = reverse('signup_student')
        self.login_url = reverse('login')
        self.signup_teacher_url = reverse('signup_teacher')
        self.add_course_url = reverse('add_course')

        self.student_data={
            'username': "test",
            'password': "Test@1234",
            'first_name': "Test",
            'last_name': "Test",
            'email': "test@gmail.com",
            'role': "STUDENT",
        }

        self.teacher_data={
            'username': "test2",
            'password': "Test@1234",
            'first_name': "Test2",
            'last_name': "Test2",
            'email': "test2@gmail.com",
            'role': "TEACHER",
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_student_cannot_signup_with_no_data(self):
        res = self.client.post(self.signup_student_url)
        # use following to see variables e.g. res.data
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)
    
    def test_student_can_signup_correctly(self):
        res = self.client.post(self.signup_student_url, self.student_data, format="json")
        self.assertEqual(res.data['user']['email'], self.student_data['email'])
        self.assertEqual(res.data['user']['username'], self.student_data['username'])
        self.assertEqual(res.status_code, 200)

    def test_student_can_login(self):
        signup_response = self.client.post(self.signup_student_url, self.student_data, format="json")
        self.assertEqual(signup_response.status_code, 200)

        login_data = {
            'username': self.student_data['username'],
            'password': self.student_data['password']
        }
        login_response = self.client.post(self.login_url, login_data, format="json")
        
        self.assertEqual(login_response.status_code, 200)
        self.assertIn('token', login_response.data)

    def test_teacher_cannot_signup_with_no_data(self):
        res = self.client.post(self.signup_teacher_url)
        self.assertEqual(res.status_code, 400)
    
    def test_teacher_can_signup_correctly(self):
        res = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(res.data['user']['email'], self.teacher_data['email'])
        self.assertEqual(res.data['user']['username'], self.teacher_data['username'])
        self.assertEqual(res.status_code, 200)

    def test_teacher_can_login(self):
        signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(signup_response.status_code, 200)

        login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        login_response = self.client.post(self.login_url, login_data, format="json")
        
        self.assertEqual(login_response.status_code, 200)
        self.assertIn('token', login_response.data)

    
class TestAddCourse(TestSetUp):
    def test_teacher_can_add_course(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        # import pdb
        # pdb.set_trace()
        
        self.assertEqual(add_course_response.status_code, 201)
        self.assertEqual(add_course_response.data['title'], course_data['title'])

class TestGetCourse(TestSetUp):
    def test_teacher_can_get_course(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        get_course_response = self.client.get(reverse('get_course', kwargs={'course_id': course_id}), format="json")
        
        self.assertEqual(get_course_response.status_code, 200)
        self.assertEqual(get_course_response.data['title'], course_data['title'])

class TestAddAndGetLesson(TestSetUp):
    def test_teacher_can_add_lesson(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)

    def test_teacher_can_get_lesson(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)
        lesson_id = add_lesson_response.data['id']

        get_lesson_response = self.client.get(reverse('get_lesson', kwargs={'lesson_id': lesson_id}), format="json")

        self.assertEqual(get_lesson_response.status_code, 200)
        self.assertEqual(get_lesson_response.data['title'], lesson_data['title'])

class TestAddAndGetAssignment(TestSetUp):
    def test_teacher_can_add_assignment(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)
        lesson_id = add_lesson_response.data['id']

        assignment_data = {
            'lesson': lesson_id,
            'title': "Test Assignment"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_assignment_response = self.client.post(reverse('add_assignment'), assignment_data, format="json")
        self.assertEqual(add_assignment_response.status_code, 201)

    def test_teacher_can_get_assignment(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)
        lesson_id = add_lesson_response.data['id']

        assignment_data = {
            'lesson': lesson_id,
            'title': "Test Assignment"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_assignment_response = self.client.post(reverse('add_assignment'), assignment_data, format="json")
        self.assertEqual(add_assignment_response.status_code, 201)
        assignment_id = add_assignment_response.data['id']

        get_assignment_response = self.client.get(reverse('get_assignment', kwargs={'assignment_id': assignment_id}), format="json")

        self.assertEqual(get_assignment_response.status_code, 200)
        self.assertEqual(get_assignment_response.data['title'], assignment_data['title'])

class TestGetLessonTopics(TestSetUp):
    def test_get_lesson_topics(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)
        lesson_id = add_lesson_response.data['id']

        topic_data = {
            'lesson': lesson_id,
            'title': "Topic 1",
            'image': None,
            'imagecaption': None,
            'text': "Topic 1 description"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_topic_response = self.client.post(reverse('add_topic'), topic_data, format="json")
        self.assertEqual(add_topic_response.status_code, 201)

        get_topics_response = self.client.get(reverse('get_lesson_topics', kwargs={'lesson_id': lesson_id}), format="json")

        self.assertEqual(get_topics_response.status_code, 200)
        self.assertGreaterEqual(len(get_topics_response.data), 1)

class TestAssignmentQuestions(TestSetUp):
    def test_get_assignment_questions(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)
        lesson_id = add_lesson_response.data['id']

        assignment_data = {
            'lesson': lesson_id,
            'title': "Test Assignment"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_assignment_response = self.client.post(reverse('add_assignment'), assignment_data, format="json")
        self.assertEqual(add_assignment_response.status_code, 201)
        assignment_id = add_assignment_response.data['id']

        question_data1 = {
            'assignment': assignment_id,
            'title': "Test Question 1"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_question_response1 = self.client.post(reverse('add_question'), question_data1, format="json")
        self.assertEqual(add_question_response1.status_code, 201)

        question_data2 = {
            'assignment': assignment_id,
            'title': "Test Question 2"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_question_response2 = self.client.post(reverse('add_question'), question_data2, format="json")
        self.assertEqual(add_question_response2.status_code, 201)

        get_questions_response = self.client.get(reverse('get_assignment_questions', kwargs={'assignment_id': assignment_id}), format="json")

        self.assertEqual(get_questions_response.status_code, 200)
        self.assertGreaterEqual(len(get_questions_response.data), 2)

class TestGetQuestionChoices(TestSetUp):
    def test_get_question_choices(self):
        teacher_signup_response = self.client.post(self.signup_teacher_url, self.teacher_data, format="json")
        self.assertEqual(teacher_signup_response.status_code, 200)

        teacher_login_data = {
            'username': self.teacher_data['username'],
            'password': self.teacher_data['password']
        }
        teacher_login_response = self.client.post(self.login_url, teacher_login_data, format="json")
        self.assertEqual(teacher_login_response.status_code, 200)
        teacher_token = teacher_login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        course_data = {
            'title': "Test Course",
            'teacher': teacher_signup_response.data['user']['id'],
            'imagecaption': None,
        }
        add_course_response = self.client.post(reverse('add_course'), course_data, format="json")
        self.assertEqual(add_course_response.status_code, 201)
        course_id = add_course_response.data['id']

        lesson_data = {
            'course': course_id,
            'title': "Test Lesson"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)

        add_lesson_response = self.client.post(reverse('add_lesson'), lesson_data, format="json")
        self.assertEqual(add_lesson_response.status_code, 201)
        lesson_id = add_lesson_response.data['id']

        assignment_data = {
            'lesson': lesson_id,
            'title': "Test Assignment"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_assignment_response = self.client.post(reverse('add_assignment'), assignment_data, format="json")
        self.assertEqual(add_assignment_response.status_code, 201)
        assignment_id = add_assignment_response.data['id']

        question_data = {
            'assignment': assignment_id,
            'title': "Test Question"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_question_response = self.client.post(reverse('add_question'), question_data, format="json")
        self.assertEqual(add_question_response.status_code, 201)
        question_id = add_question_response.data['id']

        choice_data = {
            'question': question_id,
            'title': "Choice 1",
            'is_correct': False
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + teacher_token)
        add_choice_response = self.client.post(reverse('add_choice'), choice_data, format="json")
        self.assertEqual(add_choice_response.status_code, 201)

        get_choices_response = self.client.get(reverse('get_question_choices', kwargs={'question_id': question_id}), format="json")

        self.assertEqual(get_choices_response.status_code, 200)
        self.assertGreaterEqual(len(get_choices_response.data), 1)


# [--]login, 
# [--]signup student + teacher, 
# [--]add_course, 
# [--]get_course/<int:course_id>/, 
# [--]add_assignment, 
# [--]get_assignment,
# [--]get_lesson/<int:lesson_id>/
# [--]add_lesson
# [--]get_lesson_topics
# [--]get_assignment_questions
# [--]get_question_choices/<int:question_id>/

# ---------------------------------------------Image Captioning Testing------------------------------------------------
from django.test import TestCase
from django.urls import reverse
from unittest import mock
from .models import ImageCaption
from django.core.files.uploadedfile import SimpleUploadedFile


class TestImageCaption(TestCase):
    def setUp(self):
        with open('media/images/tree.jpg', 'rb') as f:
            image_content = f.read()

        self.image_file = SimpleUploadedFile(
            name='tree.jpg', 
            content=image_content, 
            content_type='image/jpeg'
        )
        self.caption_data = {'image': self.image_file, 'caption': 'Test Caption'}

    def test_image_caption_creation(self):
        response = self.client.post(reverse('add_image_caption'), data=self.caption_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(ImageCaption.objects.exists())

    def test_caption_generation(self):
        with mock.patch('requests.post') as mocked_post:
            mocked_post.return_value.json.return_value = [{'generated_text': 'Generated Caption'}]
            response = self.client.post(reverse('add_image_caption'), data=self.caption_data)
            self.assertEqual(response.status_code, 201)
            caption = ImageCaption.objects.first()
            self.assertEqual(caption.caption, 'Generated Caption')
