<template>
  <div class="navbar-container" v-if="!(currentRouteName === 'auth' || currentRouteName === '404Error')">
    <router-link to="/">
      <div class="logo-container">
        <img
          :src="require('@/assets/logo/Logo-darker.svg/')"
          alt="Logo"
          height="70"
        />
        <h3>КИП Геофизика</h3>
      </div>
    </router-link>
    <div class="btns-container">
      <router-link to="jobPage">
        <h4 v-if="currentRouteName === 'jobPage'" style="color: #cacaca">
          Вакансии
        </h4>
        <h4 v-else>Вакансии</h4>
      </router-link>
      <router-link to="aboutCompany">
        <h4 v-if="currentRouteName === 'aboutPage'" style="color: #cacaca">
          О компании
        </h4>
        <h4 v-else>О компании</h4>
      </router-link>
      <router-link to="/auth">
        <Button>Войти</Button>
      </router-link>
    </div>
  </div>
</template>

<script>
import Button from "@/components/buttons/button";
export default {
  name: "navbar",
  components: {
    Button,
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    },
  },
};
</script>

<style lang="scss" scoped>
h3 {
  margin: 30px;
}
.navbar-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background: $color2;
  width: 100%;
}

.logo-container {
  margin-left: 15px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}

.btns-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
  margin-right: 15px;
  align-items: center;
}
</style>
