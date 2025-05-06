# VisionaryLearn

VisionaryLearn is an inclusive Learning Management System designed to support visually impaired online learners. The system integrates assistive technologies such as image captioning (via Hugging Face BLIP) and text-to-speech (via ResponsiveVoice) to enhance accessibility in education. Built with Django (backend) and Vue.js (frontend), VisionaryLearn allows both students and teachers to interact with course content in an accessible, user-friendly environment.

## Features

- User authentication with role-based access (Student / Teacher)
- Course, lesson and assignment management
- Teacher features: Add courses, lessons and assignments
- Student features: View lessons, complete assignments
- Text-to-speech feedback for all navigable elements
- AI-powered image captioning for educational content
- Full keyboard navigation support
- RESTful API integration using Django REST Framework

## Tech Stack

- Frontend: Vue.js, Vuex, Vue Router, Axios, Bootstrap
- Backend: Django, Django REST Framework
- APIs: Hugging Face BLIP (image captioning), ResponsiveVoice (text-to-speech)

## Requirements

### Python Dependencies

- Python 3.10
- Django
- djangorestframework
- django-cors-headers
- django-environ
- djangorestframework-simplejwt

### JavaScript Dependencies

- Vue 3
- Vuex
- Vue Router
- Axios
- Bootstrap
