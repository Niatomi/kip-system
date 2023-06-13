<template>
  <div class="add-device-container">
    <h2>Добавить сотрудника</h2>
    <form @submit.prevent="signUpUser" class="form-container">
      <span>
        <label for="text">Логин:</label>
        <input type="text" v-model="username" placeholder="Введите значение"/>
        
      </span>
      <span>
        <label for="text">Пароль:</label>
        <input type="text" v-model="password" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Почта:</label>
        <input type="text" v-model="email" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Имя:</label>
        <input type="text" v-model="first_name" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Фамилия:</label>
        <input type="text" v-model="second_name" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Отчество:</label>
        <input type="text" v-model="third_name" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Роль:</label>
        <select v-model="role">
          <option value="" disabled hidden>Выберите роль</option>
          <option value="ALL">Все</option>
          <option v-for="role in USER_ROLES" :value="role" :key="Math.random()">
            {{ rolesFormat(role) }}
          </option>
        </select>
      </span>
      <button type="submit"><h4>Добавить сотрудника</h4></button>
    </form>
    <h4 v-if="userAdded">Сотрудник успешно добавлен</h4>
    <h4 v-else>{{ error_msg }}</h4>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { toRaw } from 'vue'
export default {
  name: 'AddDevice',
  data() {
    return {
      username: '',
      password: '',
      email: '',
      first_name: '',
      second_name: '',
      third_name: '',
      role: '',

      userAdded: false,
      error_msg: ''
    }
  },
  computed: {
    ...mapGetters([
      'USER_ROLES'
    ])
  },
  methods: {
    ...mapActions([
      'SIGN_UP_USER'
    ]),
    rolesFormat(val) {
      let value = toRaw(val)
      if (value === 'ADMIN') {
        return 'Администратор'
      } 
      if (value === 'WORKER') {
        return 'Работник'
      } 
      if (value === 'CHIEF') {
        return 'Начальник'
      } 
      return value.charAt(0) + value.slice(1).toLowerCase()
    },
    signUpUser() {
      let data = {}
      Object.assign(data, {'username': this.username});
      Object.assign(data, {'password': this.password});
      Object.assign(data, {'email': this.email});
      Object.assign(data, {'first_name': this.first_name});
      Object.assign(data, {'second_name': this.second_name});
      Object.assign(data, {'third_name': this.third_name});
      Object.assign(data, {'role': this.role});
      this.SIGN_UP_USER(data).then((response) => {
        console.log(response);
        if (response.status === 201) {
          this.userAdded = true;
          this.error_msg = ''
          return this.deviceAdded;
        } else {
          this.error_msg = 'Ошибка валидации данных'
          this.userAdded = false;
          return this.error_msg;
        }
      })
      this.username = ''
      this.password = ''
      this.email = ''
      this.first_name = ''
      this.second_name = ''
      this.third_name = ''
      this.role = ''
    }
  }
}
</script>

<style lang="scss" scoped>
span {
  display: flex;
  flex-direction: column;
}

input {
  border-radius: 20px;
  border: none;
  background: $color7;
  padding: 5px;
  padding-left: 10px;
}

label {
}

.add-device-container {
  padding-left: 10px;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

button {
  border-radius: 20px;
  width: 100%;
}

select {
  width: 100%;
  border-radius: 20px;
  height: 45px;
  font-size: 30px;
  background: $color7;
  font-family: inherit;
  padding-left: 10px;
  border-radius: 20px;
  border: none;
  
}

option {
  border-radius: 20px;
}
</style>