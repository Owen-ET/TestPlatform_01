<template>
  <div class="loginStyle">
    <h1>注册</h1>
    <v-text-field v-model="message4" label="用户名" outlined clearable></v-text-field>
    <v-text-field v-model="message4" label="密码" outlined clearable type="password"></v-text-field>
    <v-text-field v-model="message4" label="邮箱" outlined clearable></v-text-field>
    <v-btn depressed color="primary">注册</v-btn>&#12288;&#12288;
    <v-btn depressed @click="goLogin()">立即登录</v-btn>
  </div>
</template>


<script>
export default {
  methods:{
    goLogin(){
      this.$router.push({name: 'Login'})
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