import axios from 'axios'
import router from '../router/index.js'
// 创建实例
const instance = axios.create({
  // 基础URL
  baseURL: 'http://127.0.0.1:5000/',
  // 超时时间
  timeout: 1000,
  // 头信息
  headers: {'content-type': 'application/json'}
});

// 发送请求前主动调用此函数
instance.interceptors.request.use(function(config){
  // 
  if(localStorage.getItem('token') && config.url != '/login'){
    config.auth = {username: localStorage.getItem('token'),password:''}
  }
  return config;
});

instance.interceptors.response.use(
  (response) => {
  return response
  },
  (error) => {
    // console.log("ZC")
    // console.log(error)
    if(error.response){
      if(error.response.status == 401){
        console.log('hello')
        localStorage.removeItem('token')
        router.replace({name:'Login'})
        return Promise.reject(error)
      }
    }
    
  }
)

// 导入实例
export default instance;