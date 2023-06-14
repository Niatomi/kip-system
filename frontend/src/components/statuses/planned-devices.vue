<template>
  <div class="all-devices-container">
    <InfoFeed>
      <div class="inner-container">
        <div class="checkbox-container" @click="changeShowOnlyNeedToCheck" :class="showOnlyNeedToCheck ? 'checkboxActive' : ''">
          <h4>Показывать только просроченные</h4>
        </div >
        <svg width="50%" height="5">
          <rect width="100%" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      <Device
      v-if="formDevices.length"
      v-for="item in formDevices"
      :key="item.id"
      :device="item"
      @click="openInfo(item.id)"
      
      />
    </InfoFeed>
    <Popup 
    v-if="popupActive" 
    @closePopup="closePopup()"
    >
      <AllDevicePopup :key="123"/>
    </Popup>
  </div>
</template>

<script>
import FindButton from '@/components/buttons/find-button'
import InfoFeed from '@/components/info-feed/info-feed'
import Button from '@/components/buttons/button'
import Device from './device-status-item'
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
      showOnlyNeedToCheck: false
    }
  },
  watch: {
    showOnlyNeedToCheck: function(val) {
      // console.log(this.showOnlyNeedToCheck);
    }
  },
  methods: {
    ...mapActions([
      'GET_PLANED_DEVICES',
      'GET_DEVICE_FULL_INFO',
      'GET_DEVICE_BY_SEARCH',
      'GET_PLANED_DEVICES'
    ]),
    changeShowOnlyNeedToCheck() {
      this.showOnlyNeedToCheck = !this.showOnlyNeedToCheck
    },
    openInfo(itemId) {
      this.GET_DEVICE_FULL_INFO(itemId).then(() => {
         this.popupActive = true
      })
    },
    closePopup() {
      this.popupActive = false
    },
  },
  computed: {
    ...mapGetters([
      'PLANED_DEVICES',
    ]),
    formDevices() {
      let array = []
      if (this.showOnlyNeedToCheck) {
        this.PLANED_DEVICES.forEach(value => {
          if (value.next_check_time === 'NEEDS_CHECK') {
            array.push(value)
          }
        })
        return array;
      } 
      return this.PLANED_DEVICES;
    }
  },
  mounted() {
    this.GET_PLANED_DEVICES().then(() => {})
  }
}
</script>

<style lang="scss" scoped>
.checkbox-container {
  width: 100%;
  background: $color6;
  color: $color8;
  border-radius: 20px;
  padding-left: 15px;
  align-items: center;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  
  &:hover {
    background: $color7;
  }
}

.checkboxActive {
  background: $color4;

  &:hover {
    background: $color4;
  }
}

.all-devices-container {
  margin-bottom: 10px;
}
.inner-container {
  width: 100%;
  max-width: 96%;
  margin-top: 10px;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}

input {
  color: $color8;
}

</style>