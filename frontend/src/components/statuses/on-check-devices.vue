<template>
  <div class="all-devices-container">
    <InfoFeed>
      <div class="inner-container">
        <svg width="50%" height="5">
          <rect width="100%" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      <Device
      v-if="ON_CHECK_DEVICES.length"
      v-for="item in ON_CHECK_DEVICES"
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
import Device from './on-check-device-status-item'
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
  methods: {
    ...mapActions([
      'GET_DEVICE_FULL_INFO',
      'GET_DEVICE_BY_SEARCH',
      'GET_ON_CHECK_DEVICES'
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
      'ON_CHECK_DEVICES',
    ]),
  },
  mounted() {
    this.GET_ON_CHECK_DEVICES().then(() => {})
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