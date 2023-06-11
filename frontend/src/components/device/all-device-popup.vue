<template>
    <h2>{{CHOSEN_DEVICE.name}}</h2>
    <svg width="50%" height="5">
      <rect width="100%" height="5" style="fill: #d9d9d9" />
    </svg>
    <p>Текущая аммортизация: {{ fixedAmmortizationNumber }} ₽</p>
    <p>Текущий статус: {{ getStatus }}</p>
    <p>Текущее место установки: {{ CHOSEN_DEVICE.place }}</p>
    <p>Инвентаризационный номер: {{ CHOSEN_DEVICE.invent_number }}</p>
    <p>Серийный номер: {{ CHOSEN_DEVICE.serial_number }}</p>
    <svg width="50%" height="5">
      <rect width="100%" height="5" style="fill: #d9d9d9" />
    </svg>
    <span>
      <p>Описание:</p>
      <p>{{CHOSEN_DEVICE.description}}</p>
    </span>
    <p>Категория: {{ CHOSEN_DEVICE.category }}</p>
    <p>Интервал поверки (дни): {{ CHOSEN_DEVICE.check_intervals }}</p>
    <p>Стоимость: {{ getPrice }} ₽</p>
    <table border="1">
      <caption>Спецификация устройства</caption>
      <tr>
        <th>Характеристики</th>
        <th>Значения</th>
      </tr>
      <tr v-for="spec in getSpecs" :key="Math.random()">
        <td>{{ spec[0] }}</td><td style="text-align: center;">{{ spec[1] }}</td>
      </tr>
    </table>
    <span>
      <h6 style="color: #747474">id: {{CHOSEN_DEVICE.id}}</h6>
      <h6 style="color: #747474">proto_id: {{CHOSEN_DEVICE.device_id}}</h6>
    </span>
</template>

<script>
import { mapGetters } from 'vuex'
import { toRaw } from 'vue'

export default {
  name: 'AllDevicePopup',
  computed: {
    ...mapGetters([
      'CHOSEN_DEVICE'
    ]),
    fixedAmmortizationNumber() {
      return parseFloat(this.CHOSEN_DEVICE.ammortization).toFixed(2);
    },
    getPrice() {
      return this.CHOSEN_DEVICE.price
    },
    getStatus() {
      let status = this.CHOSEN_DEVICE.current_action
      if (status === 'CHECKED') {
        return 'Поверен'
      }
      if (status === 'INSTALLED') {
        return 'Установлен'
      }
      if (status === 'CHEKING') {
        return 'Поверяется'
      }
    },
    getSpecs() {
      let ar = []
      if (typeof(this.CHOSEN_DEVICE.specifications) === undefined) {
        return [['1', '2']]
      } 
      this.CHOSEN_DEVICE.specifications.forEach(data => {
        ar.push([Object.keys(toRaw(data))[0], Object.values(toRaw(data))[0]]);
      })
      return ar
    },

  },
}
</script>

<style lang="scss" scoped>
table {
  border: none;
  border-color: none;
  background: $color7;
  border-radius: 20px;
  border-collapse: separate;
}

tr, td, th {
  padding: 5px;
  border: none;
  border-color: inherit;
}
</style>