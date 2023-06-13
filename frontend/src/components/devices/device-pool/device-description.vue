<template>
  <div class="device-description-container">
    <h2>{{CHOSEN_DEVICE_POOL_DEVICE.name}}</h2>
    <p>Категория: {{ CHOSEN_DEVICE_POOL_DEVICE.category }}</p>
    <p>Интервал поверки: {{ CHOSEN_DEVICE_POOL_DEVICE.check_intervals }} {{ useDayVerb(CHOSEN_DEVICE_POOL_DEVICE.check_intervals) }}</p>
    <p>Стоимость: {{ CHOSEN_DEVICE_POOL_DEVICE.price }} ₽</p>
    <p>Ресурс прибора: {{ CHOSEN_DEVICE_POOL_DEVICE.resource }} {{ useYearVerb(CHOSEN_DEVICE_POOL_DEVICE.resource) }}</p>
    <span>
      <p>Описание:</p>
      <p style="text-align: justify;">{{CHOSEN_DEVICE_POOL_DEVICE.description}}</p>
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
      <h6 style="color: #747474">id: {{CHOSEN_DEVICE_POOL_DEVICE.id}}</h6>
      <h6 style="color: #747474">proto_id: {{CHOSEN_DEVICE_POOL_DEVICE.device_id}}</h6>
    </span>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { toRaw } from 'vue'

export default {
  name: 'DeviceDescription',
  props: {
    device: {
      typeof: Object,
      default() {
        return {}
      }
    }
  },
  computed: {
    ...mapGetters([
      'CHOSEN_DEVICE_POOL_DEVICE'
    ]),
    getSpecs() {
      let ar = []
      if (typeof(this.CHOSEN_DEVICE_POOL_DEVICE.specifications) === undefined) {
        return [['1', '2']]
      } 
      this.CHOSEN_DEVICE_POOL_DEVICE.specifications.forEach(data => {
        ar.push([Object.keys(toRaw(data))[0], Object.values(toRaw(data))[0]]);
      })
      return ar
    },
  },
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
}
</script>

<style lang="scss" scoped>
table {
  border: none;
  border-color: none;
  background: $color7;
  border-radius: 20px;
  width: 100%;
  border-collapse: separate;
}

tr, td, th {
  padding: 5px;
  border: none;
  border-color: inherit;
}

.device-description-container {
  width: 100%;
}
</style>