<template>
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
      <form action="" class="input-container">
        <input type="text" placeholder="Логин" />
        <input type="text" placeholder="Пароль" />
        <button>Войти</button>
      </form>
    </div>
    <router-link to="/">
      <p>На главную</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "AuthPage",
};
</script>

<style lang="scss" scoped>
h2 {
  margin: 30px;
}
.auth-wrapper {
  display: flex;
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
.auth-page-container {
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
</style>
