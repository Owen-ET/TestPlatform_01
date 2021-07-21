<template>
  <v-main>
    <div class="loginStyle">
      <h1>注册</h1>
      <v-text-field v-model="username" label="用户名" outlined clearable></v-text-field>
      <v-text-field v-model="password" label="密码" outlined clearable type="password"></v-text-field>
      <v-text-field v-model="email" label="邮箱" outlined clearable></v-text-field>
      <v-btn depressed color="primary" @click="signUp()">注册</v-btn>&#12288;&#12288;
      <v-btn depressed @click="goLogin()">立即登录</v-btn>
    </div>
  </v-main>
</template>


<script>
export default {
  data(){
    return {username: "",password: "",email: ""}
  },
  methods:{
    goLogin(){
      this.$router.push({name: 'Login'})
    },
    signUp(){
      let data = {
        "username": this.username,
        "password": this.password,
        "email": this.email
      }
      // console.log(this.username,this.password,this.email)
      this.$api.user.signUp(data).then(response =>{
        console.log(response)
        if(response.data.errcode == 200){
          this.$router.push({"name": "TestCase"}).catch(()=>{})
        }
      })
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