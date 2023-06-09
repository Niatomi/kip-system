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
    <div class="btns-container" v-if="!IS_LOGGED_IN">
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
    <div class="btns-container" v-else>
      <h4>{{ userRole }}: {{ userFio }}</h4>
      <Button @click="logout">Выход</Button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Button from "@/components/buttons/button";

export default {
  name: "navbar",
  components: {
    Button,
  },
  methods: {
    ...mapActions([
      'LOGOUT'
    ]),
    logout() {
      if (this.LOGOUT()) {
        this.$router.push('/')
      }
    }
  },
  computed: {
    ...mapGetters([
      'USER',
      'IS_LOGGED_IN'
    ]),
    currentRouteName() {
      return this.$route.name;
    },
    userRole() {
      if (this.USER.role === 'ADMIN') {
        return 'Администратор';
      }
      if (this.USER.role === 'CHIEF') {
        return 'Начальник';
      }
      if (this.USER.role === 'WORKER') {
        return 'Работник';
      }
      return 'Роль неизвестна';
    },
    userFio() {
      console.log();
      let fio = ''
      if (this.USER.first_name !== undefined) {
        fio = this.USER.second_name;
        fio += ' ' + this.USER.first_name[0] + '. '
        if (this.USER.first_name !== '') {
          fio += ' ' + this.USER.third_name[0] + '. '
        }
      }
      return fio;
    }
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
  margin-bottom: 30px;
  
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
  align-items: center;
  margin-right: 15px;
}
</style>
