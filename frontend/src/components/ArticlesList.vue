<template>
  <!-- 内容 -->
  <div v-for="article in info.results" v-bind:key="article.url" id="articles">

    <div class="grid" :style="gridStyle(article)">

    <div>
      <img :src="imageIfExists(article)" alt="" class="image">
    </div>
    <div>

   
    <div>
      <span v-if="article.category != null"
      class="category">
      {{ article.category.title }}
      </span>
      <span v-for="tag in article.tag" v-bind:key="tag" class="tag">
        {{ tag }}
      </span>
    </div>
    <!-- <div class="article-title">{{ article.title }}</div> -->
    <router-link
      :to="{ name: 'ArticleDetail', params: { id: article.id } }"
      class="article-title"
    >
      {{ article.title }}
    </router-link>
    <div>{{ formatted_time(article.created) }}</div>
  </div>
  </div>
  </div>

  <!-- 翻页 -->
  <div id="paginator">
    <span v-if="isPageExists('previous')">
      <router-link :to="getPath('previous')"> Prev </router-link>
    </span>
    <span class="current-page">
      {{ getPageParam() }}
    </span>
    <span v-if="isPageExists('next')">
      <router-link :to="getPath('next') "> Next </router-link>
    </span>
  </div>
</template>

<script>

import { ref } from '@vue/reactivity';
import { useRoute } from 'vue-router';
import getArticleDate from '@/composables/getArticleData'
import pagination from '@/composables/pagination'
export default {
  name: "ArticlesList",
  setup() {
    // 所有文章数据变量
    const info = ref(''); //ref将 info 变量 包装成一个响应式得,而不是普通的字符串了
    //创建路由
    const route = useRoute();
     // 获取文章列表数据
     getArticleDate(info,route)
    //分页
    const {
        isPageExists,
        getPageParam,
        getPath
    }  = pagination(info,route);

     // 格式化日期
    const formatted_time = (iso_date_string) => {
      const date = new Date(iso_date_string);
      return date.toLocaleDateString();
    };

     // 判断开题图是否存在
    const imageIfExists = (article) => {
      if(article.avatar){
        return article.avatar.content
      }
    };
    // 样式网格
    const gridStyle = (article) => {
          if(article.avatar){
        return {
          display: 'grid',
          gridTemplateColumns: '1fr 4fr'
        }
      }
    };

    return {
      // 注入到this里
      info,
      isPageExists,
      getPageParam,
      getPath,
      formatted_time,
      imageIfExists,
      gridStyle
    }
  }};
</script>

<style scoped>
#articles {
  padding: 10px;
}
.article-title {
  font-size: large;
  font-weight: bolder;
  color: black;
  text-decoration-line: none;
  padding: 5px 0 5px 0;
}
.tag {
  padding: 2px 5px 2px 5px;
  margin: 5px 5px 5xp 0;
  font-family: Georgia, Arial, sans-serif;
  font-size: small;
  background-color: #4e4e4e;
  color: whitesmoke;
  /* 圆形边框 */
  border-radius: 5px;
}
#paginator {
  text-align: center;
  padding-top: 50px;
  margin-bottom: 50px;
}
a {
  color: black;
}
.current-page {
  font-size: x-large;
  font-weight: bold;
  padding-left: 10px;
  padding-right: 10px;
}

.category {
    padding: 5px 10px 5px 10px;
    margin: 5px 5px 5px 0;
    font-family: Georgia, Arial, sans-serif;
    font-size: small;
    background-color: darkred;
    color: whitesmoke;
    border-radius: 15px;
  }

  .image {
    width: 180px;
    border-radius: 10px;
    box-shadow: darkslategrey 0 0 12px;
  }
  .image-container {
    width: 200px;
  }
  .grid {
    padding-bottom: 10px;
  }

</style>