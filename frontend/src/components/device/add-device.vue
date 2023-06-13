<template>
  <div class="device-container">
    <div class="device-content-container">
      <h2>Добавить устройство</h2>
      <form class="input-container" @submit.prevent="addDevice">
        <span>
          <label for="text">Регистрируемый прибор:</label>
          <select v-model="selectedDeviceId">
            <option value="" disabled hidden>Выберите прибор</option>
            <option v-for="device in DEVICE_POOL_ADD" :value="device.id" :key="Math.random()">
              {{ device.name }}
            </option>
          </select>
        </span>
        <span>
          <label for="text">Отвественный за прибор:</label>
          <select v-model="selectedPersonId">
            <option value="" disabled hidden>Выберите ответственного</option>
            <option v-for="user in ALL_USERS" :value="user.id" :key="Math.random()">
              {{ user.full_name }}
            </option>
          </select>
        </span>
        <span>
          <label for="text">Инвентаризационный номер:</label>
          <input type="text" placeholder="Введите значение" v-model="inventNumber"/>
        </span>
        <span>
          <label for="text">Серийный номер:</label>
          <input type="text" placeholder="Введите значение" v-model="serialNumber"/>
        </span>
        <span>
          <label for="text">Место установки:</label>
          <input type="text" placeholder="Введите значение" v-model="installationPlace"/>
        </span>
        <button type="submit"><h4>Добавить устройство</h4></button>
      </form>
    </div>
  </div>
  <h4 style="text-align: center;" v-if="deviceAdded">Устройство добавлено</h4>
  <h4 style="text-align: center;" v-else>{{ error_msg }}</h4>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'AddDevice',
  data() {
    return {
      inventNumber: '',
      serialNumber: '',
      installationPlace: '',
      selectedDeviceId: '',
      selectedPersonId: '',
      deviceAdded: false,
      error_msg: ''
    }
  },
  computed: {
    ...mapGetters([
      'ALL_USERS',
      'DEVICE_POOL_ADD'
    ]),
  },
  methods: {
    ...mapActions([
      'GET_USERS',
      'GET_DEVICE_POOL_ADD',
      'ADD_ACTIVE_DEVICE'
    ]),
    addDevice() {
      let data = {}
      Object.assign(data, {'invent_number': this.inventNumber});
      Object.assign(data, {'serial_number': this.serialNumber});
      Object.assign(data, {'place': this.installationPlace});
      Object.assign(data, {'device_id': this.selectedDeviceId});
      Object.assign(data, {'selectedPersonId': this.selectedPersonId});
      this.ADD_ACTIVE_DEVICE(data).then((response) => {
        if (response.code === "ERR_BAD_REQUEST") {
          this.error_msg = 'Ошибка валидации данных'
          return this.error_msg;
        };
        this.deviceAdded = true;
      })
      this.inventNumber = '';
      this.serialNumber = '';
      this.installationPlace = '';
      this.selectedDeviceId = '';
      this.selectedPersonId = '';
    }
  },
  mounted() {
    this.GET_USERS();
    this.GET_DEVICE_POOL_ADD()
  }
}
</script>

<style lang="scss" scoped>
.device-container {
  background: $color6;
  color:$color8;
  width: 100%;
  max-width: 97%;
  margin-bottom: 10px;
  border-radius: 20px;
  padding-bottom: 10px;
  
}

h2 {
  margin-bottom: 10px;
}

span {
  display: flex;
  flex-direction: column;
}

input {
  width: 100%;
  border-radius: 20px;
  border: none;
  background: $color7;
  padding: 5px;
  padding-left: 15px;
}

select {
  border: none;
  background: $color7;
  height: 50px;
  padding-left: 10px;
  border-radius: 20px;
  font-family: inherit;
  font-size: inherit;
}

button {
  border-radius: 20px;
  width: 102%;
}
.device-content-container {
  margin-left: 15px; 
}

.input-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>