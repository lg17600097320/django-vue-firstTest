const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  //  跨域问题 设置代理
  devServer:{
    proxy:{
      '/api':{
        target:'http://127.0.0.1:8000/api',
        changeOrigin:true,
        pathRewrite:{
          '^/api': ''
        }
      }
    }
  }
})
