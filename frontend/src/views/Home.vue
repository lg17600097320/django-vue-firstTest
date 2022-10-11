<template>
<BlogHeader />
<ArticlesList />
<BlogFooter />

</template>

<script>

import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue'
import ArticlesList from '@/components/ArticlesList.vue'
export default {
  name:"HomeView",
    components: {
        BlogHeader,
        BlogFooter,
        ArticlesList
    },

};
</script>

<style>

</style>
