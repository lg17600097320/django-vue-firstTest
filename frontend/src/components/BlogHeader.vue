<template>
  <!-- 头部 -->
  <div id="header">
    <div class="grid">
      <div></div>
      <h1>My Drf-Vue Blog</h1>
      <!-- 搜索 -->
      <SearchButton />
      <!-- 搜索-end -->
    </div>
    <hr />

    <div class="login">
    <div v-if="hasLogin">
      <div class="dropdown" >
          <button class="dropbtn">欢迎,{{ userName }}</button>
          <div class="dropdown-content">
            <router-link :to="{name:'UserCenter', params: { username : userName } }">用户中心</router-link>
            <router-link :to="{name:'ArticleCreate'}" v-if="isSuperuser">发表文章</router-link>
            <router-link :to="{name:'HomeView'}" v-on:click="loginOut" >退出账号</router-link>
          </div>
      </div>
    </div>
    <div v-if="hasLogin == false">
      <router-link :to="{name:'LoginView'}">登录</router-link>
    </div>
    </div>
  </div>
</template>

<script>
import SearchButton from '@/components/SearchButton.vue';
import authorization from '@/untils/authorization';
export default {
  name: "BlogHeader",
  components:{
    SearchButton,
  },
  data: function() {
    return{
      userName : '',
      hasLogin : '',
      isSuperuser : JSON.parse(localStorage.getItem('is_superuser.myblog')),
    }
  },
  methods: {
      refresh(){
        this.userName = localStorage.getItem('username.myblog')
      },
      // 退出账号
      loginOut(){
        localStorage.clear()
      }
  },
  mounted() {
      authorization().then(
        (data) => [this.hasLogin,this.userName] = data
      )
  },

};
</script>


<style scoped>
 #header {
        text-align: center;
        margin-top: 20px;
    }

    .grid {
        display: grid;
        grid-template-columns: 1fr 4fr 1fr;
    }

    .login{
      display: block;
        text-align: right;
        padding-right: 5px;
    }
    .login-link {
        color: black;
    }

    
</style>
<style scoped>
  /* 样式来源: https://www.runoob.com/css/css-dropdowns.html* /
  /* 下拉按钮样式 */
  .dropbtn {
      background-color: mediumslateblue;
      color: white;
      padding: 8px 8px 30px 8px ;
      font-size: 16px;
      border: none;
      cursor: pointer;
      height: 16px;
      border-radius: 5px;
  }
  /* 容器 <div> - 需要定位下拉内容 */
  .dropdown {
      position: relative;
      display: inline-block;
  }
  /* 下拉内容 (默认隐藏) */
  .dropdown-content {
      display: none;
      position: absolute;
      background-color: #f9f9f9;
      min-width: 120px;
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
      text-align: center;
  }
  /* 下拉菜单的链接 */
  .dropdown-content a {
      color: black;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
  }
  /* 鼠标移上去后修改下拉菜单链接颜色 */
  .dropdown-content a:hover {
      background-color: #f1f1f1
  }
  /* 在鼠标移上去后显示下拉菜单 */
  .dropdown:hover .dropdown-content {
      display: block;
  }
  /* 当下拉内容显示后修改下拉按钮的背景颜色 */
  .dropdown:hover .dropbtn {
      background-color: darkslateblue;
  }
</style>