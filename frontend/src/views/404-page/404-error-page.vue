<template>
    <v-error-container>
        <div class="content-container">
            <img
              :src="require('@/assets/errors/404.svg/')"
              alt="Logo"
              height="300"
            /> 
            
            <div class="text-container">
                <h2>Что-то пошло не так....</h2>
                <svg width="500" height="5">
                    <rect width="500" height="5" style="fill: #d9d9d9" />
                </svg>
                <router-link to="/">
                    <h1>На главную</h1>
                </router-link>
            </div>
        </div>
    </v-error-container>

</template>

<script>
export default {
    name: 'Error404Page',
}
</script>


<style lang="scss">

.text-container {
    margin-top: 50px;
    display: flex;
    justify-content: center;
    gap: 40px;
    align-items: center;
    flex-direction: column;
}

.content-container {
    display: flex;
    margin-top: 20vh;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.v-error-container {
    height: 100vh;
}

</style>