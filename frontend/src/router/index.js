// Example of how to use Vue Router

import { createRouter, createWebHistory } from 'vue-router'
import { createStore } from 'vuex';


// 1. Define route components.
// These can be imported from other files
import Home from '../pages/Home.vue';
import Dashboard from '../pages/Dashboard.vue';
import Login from '../pages/Login.vue';
import Signup from '../pages/Signup.vue';
import AddCourse from '../pages/Teacher/AddCourse.vue';
import Question from '../pages/Teacher/Question.vue';
import LessonList from '../pages/LessonList.vue';
import Lesson from '../pages/Lesson.vue';
import Assignment from '../pages/Assignment.vue';
import test from '../pages/Teacher/test.vue'
import AddLesson from '../pages/Teacher/AddLesson.vue'
import AddAssignment from '../pages/Teacher/AddAssignment.vue'

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'Home', component: Home },
        { 
            path: '/Dashboard', 
            name: 'Dashboard', 
            component: Dashboard,
            meta: {
                requiresAuth: true,
                requiresRole: 'student'
            }
        },
        { 
            path: '/Login', 
            name: 'Login', 
            component: Login,
            meta: {
                requiresNoAuth: true
            }
        },
        { 
            path: '/Signup', 
            name: 'Signup', 
            component: Signup,
            meta: {
                requiresNoAuth: true
            }
        },
        { 
            path: '/AddCourse', 
            name: 'AddCourse', 
            component: AddCourse,
            meta: {
                requiresAuth: true,
                requiresRole: 'teacher'
            }
        },
        { 
            path: '/AddLesson', 
            name: 'AddLesson', 
            component: AddLesson,
            meta: {
                requiresAuth: true,
                requiresRole: 'teacher'
            }
        },
        { 
            path: '/AddAssignment', 
            name: 'AddAssignment', 
            component: AddAssignment,
            meta: {
                requiresAuth: true,
                requiresRole: 'teacher'
            }
        },
        { 
            path: '/test', 
            name: 'test', 
            component: test,
        },
        { 
            path: '/Question', 
            name: 'Question', 
            component: Question,
            meta: {
                requiresAuth: true,
                requiresRole: 'teacher'
            }
        },
        { 
            path: '/courses/:id/lessons', 
            name: 'LessonList', component: 
            LessonList, 
            props: true 
        },
        { 
            path: '/courses/lessons/:id', 
            name: 'lesson', component: Lesson, 
            props: true,
            meta: {
                requiresAuth: true,
            }
        },
        { 
            path: '/courses/assignment/:id', 
            name: 'assignment', 
            component: Assignment, 
            props: true,
            meta: {
                requiresAuth: true,
            }
        },
        
    ]
});

router.beforeEach((to, from, next) => {
    const isAuthenticated = localStorage.getItem('token');
    const userRole = localStorage.getItem('role');

    if (to.meta.requiresAuth && !isAuthenticated) {
        console.log('Not authenticated')
        next({ name: 'Login' });
    } else if (to.meta.requiresRole && userRole !== to.meta.requiresRole) {
        console.log('Not correct role')
        next({ name: 'Home' });
    } else if (to.meta.requiresNoAuth && isAuthenticated) {
        console.log('Already Logged in')
        next({ name: 'Home' });
    } else {
        next();
    }

});

export default router
