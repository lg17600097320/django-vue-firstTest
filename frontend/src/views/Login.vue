<template>
   <BlogHeader/>

<div id="grid">
    <div id="signup">
        <h3>注册账号</h3>
        <form>
            <div class="form-elem">
                <span>账号:</span> 
                <input v-model="signupName" type="text" placeholder="输入用户名">
            </div>
            <div class="form-elem">
                <span>密码：</span> 
                <input v-model="signupPwd" type="password" placeholder="输入密码">
            </div>
            <div class="form-elem">
                <span>密码：</span> 
                <input v-model="signupPwd2" type="password" placeholder="请再次输入密码">
            </div>
            <div class="form-elem">
                <button v-on:click.prevent="signup">提交</button>
            </div>
        </form>
</div>
<div id="signin">
            <h3>登录账号</h3>
            <form>
                <div class="form-elem">
                    <span>账号：</span>
                    <input v-model="signinName" type="text" placeholder="输入用户名">
                </div>

                <div class="form-elem">
                    <span>密码：</span>
                    <input v-model="signinPwd" type="password" placeholder="输入密码">
                </div>

                <div class="form-elem">
                    <button v-on:click.prevent="signin">登录</button>
                </div>
            </form>
        </div>
    </div>
<BlogFooter/>
</template>

<script>
    import axios from 'axios';
import BlogHeader from '@/components/BlogHeader.vue';
import BlogFooter from '@/components/BlogFooter.vue';
export default {
        name: 'LoginView',
        components : {BlogHeader,BlogFooter},
        data : function () {
            return{
                signupName: '',
                signupPwd: '' ,
                signupPwd2: '',
                signupResponse: null,
                signinName: '',
                signinPwd: '' ,
            }
        },
        methods: {
          
            signup() {
                const that = this;
                let pw1 = this.signupPwd
                let pw2 = this.signupPwd2
                if (pw1 == pw2){
                    axios
                    .post('/api/user/',{
                        username: this.signupName,
                        password: this.signupPwd,
                    })
                    .then(function (response){
                        that.signupResponse = response.data;
                        alert('注册成功拉,快去登录吧！')
                    })
                    .catch(function (error){
                        alert(error.message);
                    })
                }
                else{
                    alert('俩次密码不一致！')
                }

                
            },
            signin() {
                const that = this
                console.log(that.signinName,that.signinPwd)
                axios
                    .post('/api/token/',{
                        username: that.signinName,
                        password: that.signinPwd
                    })
                    .then(function (response){
                        const storage = localStorage;
                        const expiredTime =  Date.parse(response.headers.date) + 60000;

                        storage.setItem('access.myblog',response.data.access);
                        storage.setItem('refresh.myblog', response.data.refresh);
                        storage.setItem('expiredTime.myblog', expiredTime);
                        storage.setItem('username.myblog', that.signinName);
                         that.token = storage.getItem('access.myblog')
                           //判断是否是管理员
                           axios
                            .get('/api/user/'+ that.signinName + '/',{
                                headers: {
                                    authorization: 'Bearer ' + that.token
                                }
                            }
                            )
                            .then(function(response){
                                console.log(response.data)
                                storage.setItem('is_superuser.myblog',response.data.is_superuser)
                                //路由跳转到这里
                                that.$router.push({name: 'HomeView'})
                            })
                    })
                    .catch(function(err){
                            console.log(err)
                    })
            },
        }
}
</script>

<style scoped>
    #grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
    #signup {
        text-align: center;
    }
    .form-elem {
        padding: 10px;
    }
   form  div input {
        height: 25px;
        padding-left: 10px;
        border:1px solid;
    }
    form  div span{
        display: inline-block;
    }
    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 60px;
    }
    #signin {
        text-align: center;
    }
</style>