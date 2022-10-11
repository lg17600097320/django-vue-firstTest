<template>
  <BlogHeader  ref="header"  />
  <div id="user-center">
    <h3>更新资料信息</h3>
    <form action="">
            <div class=" form-elem">
                <span>用户名:</span>
                <input v-model="username" type="text" placeholder="请输入用户名">
            </div>
            <div class=" form-elem">
                <span>新密码:</span>
                <input  v-model="password" type="text" placeholder="请输入密码">
            </div>

            <div class="form-elem">
               <button v-on:click.prevent="changeInfo">更新</button>
            </div>
            <div class="form-elem">
                <button class="delete-btn" v-on:click.prevent="showingDeleteAlert = true">删除用户</button>
                <div :class="{ shake: showingDeleteAlert }">
                    <button class="confirm-btn"
                            v-if="showingDeleteAlert"
                            @click.prevent="confirmDelete"
                    >确定删除此用户吗?</button>
                </div>
            </div>
    </form>
  </div>
  <BlogFooter />
</template>

<script>
import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue';
import axios from 'axios';
import authorization from '@/untils/authorization'

const storage = localStorage
export default {
    name: 'UserCenter',
    components:{
    BlogHeader,
    BlogFooter,
    },
    data: function() {
        return{
            username : '',
            password : '',
            token : '',
            showingDeleteAlert : false,
        }
    },
    mounted(){
        this.username = storage.getItem('username.myblog');
        this.welcomeName = storage.getItem('username.myblog');
    },
    methods: {
        changeInfo(){
            const that = this;
            //验证登录状态
            authorization()
                            .then(function(response){
                                //检查登录状态
                                //若登录已过期,不执行后续操作
                                if(!response[0]){
                                    alert('登录已过期,请重新登录');
                                    return
                                }
                                console.log('change info start')
                                if(that.password.length > 0 && that.password.length < 6) {
                                    alert('PassWord too short')
                                    return
                                }
                                // 旧的username 用于向接口发送请求
                                const oldName = storage.getItem('username.myblog');
                                // 获取已填写的表单数据
                                let data = {};
                                if(that.username != ''){
                                    data.username = that.username;
                                }
                                if(that.password != ''){
                                    data.password = that.password;
                                }
                                //获取令牌
                                that.token = storage.getItem('access.myblog');
                                //发送更新数据到接口
                                axios
                                    .patch(
                                        '/api/user/'+oldName+'/',
                                        data,
                                        {
                                            headers : {Authorization : 'Bearer ' + that.token}
                                        }
                                    )
                                    .then(function(response){
                                        const name = response.data.username;
                                        storage.setItem('username.myblog',name);
                                        that.$router.push({name:'UserCenter',params:{username:name}});
                                        that.$refs.header.refresh();
                                    })

                            })
        },

        confirmDelete() {
            const that =this;
            authorization()
                        .then(function (response){
                            if(response[0]){
                                that.token = storage.getItem('access.myblog');
                                axios
                                    .delete('/api/user/'+ that.username +'/',{
                                        headers: {Authorization: 'Bearer ' + that.token}
                                    })
                                    .then(function(){
                                        storage.clear()
                                        that.$router.push({name:'HomeView'})
                                    })
                            }
                        })
        }   
    }

}
</script>

<style scoped>
    #user-center {
        text-align: center;
    }
    .form-elem {
        padding: 10px;
    }
    input {
        height: 25px;
        padding-left: 10px;
    }
    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 200px;
    }

    .confirm-btn {
        width: 80px;
        background-color: darkorange;
    }
    .delete-btn {
        background-color: darkred;
        margin-bottom: 10px;
    }
    .shake {
        animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
        transform: translate3d(0, 0, 0);
        backface-visibility: hidden;
        perspective: 1000px;
    }
    @keyframes shake {
        10%,
        90% {
            transform: translate3d(-1px, 0, 0);
        }
        20%,
        80% {
            transform: translate3d(2px, 0, 0);
        }
        30%,
        50%,
        70% {
            transform: translate3d(-4px, 0, 0);
        }
        40%,
        60% {
            transform: translate3d(4px, 0, 0);
        }
    }
</style>