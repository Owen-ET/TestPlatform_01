<template>
  <div class="loginStyle">
    <h1>登录</h1>
    <v-text-field v-model="username" label="用户名" outlined clearable></v-text-field>
    <v-text-field v-model="password" label="密码" outlined clearable type="password"></v-text-field>
    <v-btn depressed color="primary" @click="login()">登录</v-btn>&#12288;&#12288;
    <v-btn depressed @click="goSignUp()">注册</v-btn>
  </div>
</template>


<script>
export default {
  data(){
    return {
      'username': '',
      'password': ''
    }
  },
  methods:{
    goSignUp(){
      this.$router.push({name: 'SignUp'})
    },
    login(){
      let loginData = {
        username: this.username,
        password: this.password
      };
      this.$api.user.login(loginData).then(res=>{
        // localStorage存储到浏览器中的数据
        localStorage.setItem('token', res.data.access_token)
        console.log(res);
      });


      // testcase新用例接口
      this.$api.testcase.getTestcase().then(res=>{
        console.log(res)
      });
    }
  }

};
</script>


<style scoped>
    .loginStyle{
        width: 500px;
        margin: 0 auto;
        /* 将文本和按钮居中 */
        text-align: center;
    }
</style>