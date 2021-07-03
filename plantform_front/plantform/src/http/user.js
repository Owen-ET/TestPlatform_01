import axios from "./http"

const user = {
    login(loginData){
        // 使用axios的get方法
        return axios.get("/login", {auth: loginData});
    }
}


export default user;