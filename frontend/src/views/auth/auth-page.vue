<template>
  <Transition name="fade-slide" appear>
    <div class="auth-wrapper">
      <div class="logo-container">
        <router-link to="/">
          <img
          :src="require('@/assets/logo/Logo-lighter.svg/')"
          alt="Logo"
          height="150"
          />
        </router-link>
        <h2>КИП Геофизика</h2>
        <svg width="380" height="5">
          <rect width="500" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      
      <div class="auth-page-container">
        <h2>Вход</h2>
        <form @submit.prevent="signIn" class="input-container" >
          <input type="text" placeholder="Логин" v-model="login"/>
          <input type="password" placeholder="Пароль" v-model="password"/>
          <div class="error-message" v-if="error_msg.length">
            <p>{{ error_msg }}</p>
          </div>
          <button type="submit">Войти</button>
        </form>
      </div>
      <router-link to="/">
        <p>На главную</p>
      </router-link>
    </div>
  </Transition>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import { isProxy, toRaw } from 'vue';
export default {
  name: "AuthPage",
  data() {
    return {
      login: '',
      password: '',
      data: {},
      error_msg: ''
    }
  },
  methods: {
    ...mapActions([
      'SET_LOGIN'
    ]),
    signIn(values) {
      this.data = {
        'username': this.login,
        'password': this.password,
        'grant_type': 'password',
        'scope': '',
        'client_id': '',
      }
      this.SET_LOGIN(toRaw(this.data))
      .then((response) => {
        if (response.code === "ERR_BAD_REQUEST") {
          this.error_msg = 'Пользователь не найден'
        };
        if (response.status === 200) {
          this.$router.push('/chiefPage')
        }
      })
      this.password = ''
      this.login = ''
      this.data = {}
    }
  }
};
</script>

<style lang="scss" scoped>
h2 {
  margin: 30px;
}
.auth-wrapper {
  display: flex;
  margin-top: 5vh;
  flex-direction: column;
  align-items: center;
}
.logo-container {
  margin-top: 3%;
  margin-bottom: 3%;

  display: flex;
  flex-direction: column;
  align-items: center;
}
.error-message {
  display: flex;
  flex-direction: row;
  justify-content: center;
  color: rgb(150, 3, 3);
}
.auth-page-container {
  min-width: 50vh;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: $color8;

  background: $color7;
  padding-bottom: 3%;
  width: 50%;
  margin-bottom: 2%;
  color: $secondary_textcolor;
}

.input-container {
  display: flex;
  flex-direction: column;
  width: 90%;
  gap: 20px;
}

input {
  border: none;
  height: 50px;
  font-size: 30px;
  border-radius: 20px;
  padding-left: 20px;
}

button {
  border: None;
  font-size: 40px;
  border-radius: 15px;
  height: 80px;
  color: $textcolor;
  font-family: inherit;
  background: $color4;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 1s ease, transform 1s ease-in-out;
  transform: translateY(0px);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(40px);
}
</style>
