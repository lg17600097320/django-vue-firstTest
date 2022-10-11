import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// 这里可以写前端的初始化配置


URLSearchParams.prototype.appendIfExists = function (key,value) {
    if(value !== null && value !== undefined){
        this.append(key,value)
    }
};


createApp(App).mount('#app')
createApp(App).use(router).mount('#app');

