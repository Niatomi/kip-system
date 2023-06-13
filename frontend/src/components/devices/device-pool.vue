<template>
  <div class="users-container">
    <InfoFeed>
      <div class="local-navbar">
        <AddDeviceButton 
          ref="Date.now()" 
          @click="showAdd = true"
          >Добавить устройство</AddDeviceButton>
      </div>
    </InfoFeed>
    <Transition name="fade-slide" appear>
      <InfoFeed>
        <div class="generic-container">
          <div class="generic-content">
            <svg width="50%" height="5">
              <rect width="100%" height="5" style="fill: #d9d9d9" />
            </svg>
            <DevicePoolItem 
            v-for="device in DEVICE_POOL" 
            :device="device" 
            :key="device.id"
            @click="openPopupDeviceDescription(device.id)"/>
          </div>
        </div>
      </InfoFeed>
    </Transition>
    <Popup @closePopup="closeAddDevice" v-if="showAdd"><AddDevicePool/></Popup>
    <Popup @closePopup="closeDescDevice" v-if="showDesc"><DeviceDescription/></Popup>
  </div>
</template>

<script>
import InfoFeed from '@/components/info-feed/info-feed.vue'
import LocalButton from '@/components/buttons/local-button'
import AddDeviceButton from '@/components/buttons/add-device-button'
import Popup from '@/components/popup/popup'
import { mapGetters, mapActions } from 'vuex'
import AddDevicePool from '@/components/devices/device-pool/add-device-form'
import DevicePoolItem from '@/components/devices/device-pool/device-item'
import DeviceDescription from '@/components/devices/device-pool/device-description.vue'

export default {
  name: 'DevicePool',
  components: {
    InfoFeed,
    AddDeviceButton,
    LocalButton,
    Popup,
    AddDevicePool,
    DevicePoolItem,
    DeviceDescription
  },
  data() {
    return {
      selected: '',
      showAdd: false,
      showDesc: false
    }
  },
  watch: {
    selected: function(val) {
      if (val === 'ALL') {
        this.GET_ALL_USERS()
      } else {
        this.GET_USERS_BY_ROLE(val)
      }
    }
  },
  computed: {
    ...mapGetters([
      'DEVICE_POOL',
    ]),
  },
  methods: {
    ...mapActions([
      'GET_POOL_DEVICES',
      'GET_DEVICE_POOL_BY_ID_TO_CHOSE_API'
    ]),
    closeAddDevice() {
      this.showAdd = false;
    },
    closeDescDevice() {
      this.showDesc = false;
    },
    openPopupDeviceDescription(deviceId) {
      this.GET_DEVICE_POOL_BY_ID_TO_CHOSE_API(deviceId).then(() => {
        this.showDesc = true
      })
    }
  },
  mounted() {
    this.GET_POOL_DEVICES()
  }
}
</script>

<style lang="scss" scoped>
.users-container {
  display: flex;
  width: 100%;
  gap: 10px;
  flex-direction: column;
  margin-bottom: 10px;
}

.generic-container {
  width: 100%;
}

.generic-content {
  margin: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

select {
  width: 100%;
  border-radius: 20px;
  height: 45px;
  font-size: 30px;
  background: $color6;
  font-family: inherit;
  padding-left: 10px;
  border-radius: 20px;
  
}

option {
  border-radius: 20px;
}

.local-navbar {
  padding: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  display: flex;
  gap: 10px;
  flex-direction: column;
  align-items: center;
  width: 100% - 3;
}
</style>