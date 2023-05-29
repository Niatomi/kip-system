<template>
  <div class="auth-wrapper">
    <div class="logo-container">
      <img
        :src="require('@/assets/logo/Logo-lighter.svg/')"
        alt="Logo"
        height="150"
      />
      <h1>КИП Геофизика</h1>
      <svg width="400" height="5">
        <rect width="500" height="5" style="fill: #d9d9d9" />
      </svg>
    </div>
    <div class="auth-page-container">
      <h1>Вход</h1>
      <form action="" class="input-container">
        <input type="text" placeholder="Логин" />
        <input type="text" placeholder="Пароль" />
        <button>Войти</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthPage",
};
</script>

<style lang="scss" scoped>
.auth-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.logo-container {
  margin-top: 3%;
  margin-bottom: 5%;

  display: flex;
  flex-direction: column;
  align-items: center;
}
.auth-page-container {
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;

  background: #d9d9d9;
  padding-bottom: 3%;
  width: 50%;
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
  background: #9ece9a;
}
</style>
