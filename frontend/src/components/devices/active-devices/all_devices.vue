<template>
  <div class="all-devices-container">
    <InfoFeed>
      <div class="inner-container">
        <form @change="getDevicesBySearch" class="input-container" >
          <input type="text" class="search" placeholder="Поиск" v-model="search"/>
        </form>

        <svg width="50%" height="5">
          <rect width="100%" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      <Device
      v-if="filterAllDevicesInfo.length"
      v-for="item in filterAllDevicesInfo"
      :key="item.id"
      :device="item"
      @click="openInfo(item.id)"
      
      />
    </InfoFeed>
    <Popup 
    v-if="getPopupState" 
    @closePopup="closePopup()">
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
    </Popup>
  </div>
</template>

<script>
import FindButton from '@/components/buttons/find-button'
import InfoFeed from '@/components/info-feed/info-feed'
import Button from '@/components/buttons/button'
import Device from '@/components/device/device'
import { mapActions, mapGetters } from 'vuex'
import { toRaw } from 'vue'
import Popup from '@/components/popup/popup'

export default {
  components: {
    InfoFeed,
    Button,
    FindButton,
    Device,
    Popup
  },
  data() {
    return {
      search: '',
      popupActive: false,
    }
  },
  methods: {
    ...mapActions([
      'GET_ACTIVE_DEVICES_IN_PAGES',
      'GET_DEVICE_FULL_INFO'
    ]),
    openInfo(itemId) {
      this.GET_DEVICE_FULL_INFO(itemId)
      this.popupActive = true
    },
    closePopup() {
      this.popupActive = false
    }
  },
  computed: {
    ...mapGetters([
      'ALL_DEVICES_PAGE',
      'ALL_DEVICES_INFO',
      'CHOSEN_DEVICE'
    ]),
    getSpecs() {
      let ar = []
      this.CHOSEN_DEVICE.specifications.forEach(data => {
        ar.push([Object.keys(toRaw(data))[0], Object.values(toRaw(data))[0]]);
      })
      return ar
      // return Object.entries()
    },
    getPopupState() {
      return this.popupActive
    },
    filterAllDevicesInfo() {
      return this.ALL_DEVICES_INFO.sort((a, b) => {
        let comparison = 0;
        if (a.name < b.name) {
          comparison = -1;
        } else if (a.name > b.name) {
          comparison = 1;
        }
        return comparison;
      })
    },
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
    }
  },
  mounted() {
    this.GET_ACTIVE_DEVICES_IN_PAGES()
  }
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

.inner-container {
  width: 100%;
  max-width: 97%;
  margin-top: 10px;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}

.input-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 10px;
}

.search {
  color: $color8;
  padding-left: 15px;
  border: none;
  border-radius: 20px;
}

input {
  color: $color8;
}

</style>