<template>
  <BlogHeader />

  <div id="article-create">
    <h3>发表文章</h3>
    <!-- 提交标题图表单 -->
    <form id="image_form">
      <div class="form-elem">
          <span>图片:</span>
          <input type="file" id="file" v-on:change="onFileChange">
      </div>
    </form>
    <!-- 提交数据的表单 -->
    <form>
        <div class="form-elem">
            <span>标题:</span>
            <input v-model="title"  type="text" placeholder="输入标题">
        </div>

        <div class="form-elem">
            <span>分类:</span>
            <span v-for="category in categories"
            :key="category.id"
            >
              <button class="category-btn"
                      :style="categoryStyle(category)"  
                      @click.prevent="chooseCategory(category)"
              > 
              {{ category.title }}
            </button>
            </span>
        </div>

        <div class="form-elem">
            <span>标签:</span>
            <input v-model="tags"  type="text" placeholder="输入标签,逗号分隔">
        </div>

        <div class="form-elem">
            <span>正文:</span>
            <textarea   v-model="body" placeholder="输入正文" cols="80" rows="20"></textarea>
        </div>


        <div class="form-elem">
            <button v-on:click.prevent="submit" >提交</button>
        </div>

    </form>
  </div>

  <BlogFooter />
</template>

<script>
import BlogFooter from "@/components/BlogFooter.vue";
import BlogHeader from "@/components/BlogHeader.vue";
import axios from 'axios';
import authorization from '@/untils/authorization';

export default {
  name: "ArticleCreate",
  components: {
    BlogHeader,
    BlogFooter,
  },
  data: function(){
    return{
      //文章标题
      title : '',
      //文章正文
      body : '',
      //数据库所有的问题 列表格式
      categories: [],
      //选定的分类
      selectedCategory : null,
      //标签
      tags : '' ,
      //标题图ID
      avatarID: null,
    }
  },
  mounted() {
      //页面初始化时获取所有的分类
      axios
          .get('/api/category/')
          .then(response => this.categories = response.data)
  },
  methods: {
    //根据分类是否被选中,按钮的颜色发生变化
    categoryStyle(category) {
        if(this.selectedCategory != null && category.id == this.selectedCategory.id){
          return{
            backgroundColor : 'black',
          }
        }
        return{
            backgroundColor : 'lightgrey',
            color: 'black'
          }
    },
    // 选取分类方法
    chooseCategory(category){
      if(this.selectedCategory != null && category.id == this.selectedCategory.id){
          this.selectedCategory = null
        }
      else{
        this.selectedCategory = category
      }
    },
    // 标题图处理
    onFileChange(e){
      // 将文件二进制数据添加到提交数据中
      //在发表新文章页面中选定图片后，不等待文章的提交而是立即将图片上传。
      //图片上传成功后返回图片 id，前端将 id 保存待用。
      //提交文章时，将图片 id 一并打包提交即可。
      const file = e.target.files[0]
      let formDate = new FormData();
      formDate.append('content',file)

      axios
          .post('/api/avatar/',formDate,
          {
            headers : {
              'Content-Type': 'multipart/form-data',
              'Authorization': 'Bearer ' + localStorage.getItem('access.myblog')
            }
          })
          .then(response => this.avatarID = response.data.id)

    },
    //点击提交按钮
    submit(){
          const that = this;
          authorization()
                        .then(function (response){
                            if(response[0]){
                              //需要传给后端的字典
                              let data = {
                                title : that.title,
                                content : that.body
                              };
                              // 添加标题图id
                              data.avatar_id = that.avatarID;
                              //添加分类
                              if(that.selectedCategory){
                                data.category_id = that.selectedCategory.id
                              }
                              // 标签预处理
                              data.tag = that.tags //以逗号进行分割
                                                    .split(',')
                                                    // 剔除首尾的空格
                                                    .map(x => x.trim())
                                                    // 检测是否为空
                                                    .filter(x => x.charAt(0) != '');
                            //获取token令牌
                            that.token = localStorage.getItem('access.myblog')
                            console.log(data)
                            axios
                                  .post('/api/article/',data,
                                  {
                                    headers : {Authorization : 'Bearer '+ that.token}
                                  })
                                  .then(function(response){
                                     that.$router.push({name:'ArticleDetail',params: {id: response.data.id }});
                                  })
                            }
                            else{
                              alert('令牌过期,请重新登录');
                            }
                        })
    }
  },
};
</script>

<style scoped>
  .category-btn {
    margin-right: 10px;
  }
  #article-create {
    text-align: center;
    font-size: large;
    margin-bottom: 50px;
  }
  form {
    text-align: left;
    padding-left: 100px;
    padding-right: 10px;
  }
  .form-elem {
    padding: 10px;
  }
  input {
    height: 25px;
    padding-left: 10px;
    width: 50%;
  }
  button {
    height: 35px;
    cursor: pointer;
    border: none;
    outline: none;
    background: steelblue;
    color: whitesmoke;
    border-radius: 5px;
    width: 60px;
  }
</style>