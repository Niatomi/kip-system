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
    @closePopup="closePopup()"
    >
      <AllDevicePopup/>
    </Popup>
  </div>
</template>

<script>
import FindButton from '@/components/buttons/find-button'
import InfoFeed from '@/components/info-feed/info-feed'
import Button from '@/components/buttons/button'
import Device from '@/components/device/device'
import AllDevicePopup from '@/components/device/all-device-popup'
import { mapActions, mapGetters } from 'vuex'
import { toRaw } from 'vue'
import Popup from '@/components/popup/popup'

export default {
  components: {
    InfoFeed,
    Button,
    FindButton,
    Device,
    Popup,
    AllDevicePopup
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