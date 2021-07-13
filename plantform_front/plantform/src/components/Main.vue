<!-- App.vue -->
<template>
    <v-app>
        <v-navigation-drawer app clipped>
            <!-- -->
            <MainLeftLists />
        </v-navigation-drawer>


        <!-- 根据应用组件来调整你的内容 -->
        <v-main>

            <!-- 给应用提供合适的间距 -->
            <v-container fluid>

            <!-- 如果使用 vue-router -->
            <router-view></router-view>
            </v-container>
        </v-main>

        <v-footer app>
            <!-- -->
        </v-footer>
    </v-app>
</template>

<script>
import MainLeftLists from "./MainLeftLists.vue"
export default {
    components:{
        MainLeftLists,
    }
}
</script>

<style scoped>

</style>
