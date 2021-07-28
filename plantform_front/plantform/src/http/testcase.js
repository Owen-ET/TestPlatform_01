import axios from "./http"

const testcase = {
    getTestcase(){
        return axios.get("/testcase/get")
    },
    deleteTestCase(nodeid){
        return axios.get("/testcase/delete",{params: nodeid})
    },
    // addTestCase(){
    //     return axios.post("/testcase/add")
    // }
}

export default testcase;