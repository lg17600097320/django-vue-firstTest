import { createWebHistory,createRouter } from "vue-router";
import HomeView from '@/views/Home.vue';
import ArticleDetail from '@/views/ArticleDetail.vue';
import LoginView from '@/views/Login.vue'
import UserCenter from '@/views/UserCenter.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import ArticleEdit from '@/views/ArticleEdit'
const routes = [
    {
        path : '/',
        name : 'HomeView',
        component: HomeView
    },
    {
        path: '/article/:id',
        name : "ArticleDetail",
        component: ArticleDetail
    },
    {
        path: '/login',
        name: 'LoginView',
        component: LoginView
    },
    {
        path: '/user/:username',
        name: 'UserCenter',
        component: UserCenter
    },
    {
        path: '/article/create',
        name: 'ArticleCreate',
        component: ArticleCreate
    },
    {
        path: '/article/edit/:id',
        name: 'ArticleEdit',
        component: ArticleEdit
    },
];

const router =createRouter({
    history: createWebHistory(),
    routes
});

export default router;