<template>
  <div class="auth-page-container">
    <div class="inputs-container">
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
.inputs-container {
  background: #d9d9d9;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.auth-page-container {
  text-align: center;
}

input {
  appearance: none;
  width: 100%;
  border: 0;
  height: 50px;
  color: black;
  font-size: 3rem;
  padding-left: 10px;
  border-radius: 20px;
}
.input-container {
  display: flex;
  gap: 5px;
  flex-direction: column;
  align-content: center;
  align-items: center;
}

p {
  background: rgb(189, 104, 104);
}
</style>
