import Vue from 'vue';
import Router from 'vue-router';
import UserSearch from './components/UserSearch.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Landing',
      component: UserSearch,
    },
    {
      path: '/usersearch',
      name: 'User Search',
      component: UserSearch,
    },
  ],
});
