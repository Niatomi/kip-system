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
    <p>Ресурс прибора к следующей поверке: {{ CHOSEN_DEVICE.resourceOnNextCheck }} {{ useYearVerb(CHOSEN_DEVICE.resourceOnNextCheck) }}</p>
    <p>Время наработки: {{ convertTimeInUsage(CHOSEN_DEVICE.timeInUse) }}</p>
    <svg width="50%" height="5">
      <rect width="100%" height="5" style="fill: #d9d9d9" />
    </svg>
    <p>Категория: {{ CHOSEN_DEVICE.category }}</p>
    <p>Интервал поверки: {{ CHOSEN_DEVICE.check_intervals }} {{ useDayVerb(CHOSEN_DEVICE.check_intervals) }}</p>
    <p>Стоимость: {{ getPrice }} ₽</p>
    <p>Ресурс прибора: {{ CHOSEN_DEVICE.resource }} {{ useYearVerb(CHOSEN_DEVICE.resource) }}</p>
    <span>
      <p>Описание:</p>
      <p style="text-align: justify;">{{CHOSEN_DEVICE.description}}</p>
    </span>
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
  methods: {
    useYearVerb(valu) {
      let val = valu % 10
      let godaArr = [2, 3, 4]
      let result = 'лет';
      if (val === 1) {
        result = 'год';
      }
      godaArr.forEach(value => {
        if (val === value) {
          result = 'года';
        }
      })
      if (valu >= 5) {
        result = 'лет'
      }
      return result;
    },
    useDayVerb(valu) {
      let val = valu % 10
      let daysArr = [2, 3, 4]
      let result = 'дней'
      if (val === 1) {
        result = 'день';
      }
      daysArr.forEach(value => {
        if (val === value) {
          result = 'дня';
        }
      })
      return result;
    },
    convertTimeInUsage(val) {
      let seconds = Number(val);

      if (seconds === 0) {
        return 'Отсутствует'
      }
      let y = Math.floor(seconds / (3600*24*365));
      let d = Math.floor((seconds - (y * (3600*24*365))) / (3600*24));

      let year = y > 0 ? y + ' ' + this.useYearVerb(y) + ' ': ''
      let days = d > 0 ? d + ' ' + this.useDayVerb(d) + ' ': ''

      return year + days
    }
  },
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
      if (status === 'REGISTRED') {
        return 'Зарегистрирован'
      }
      status = status.charAt(0) + status.toLowerCase().slice(1)
      return status
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