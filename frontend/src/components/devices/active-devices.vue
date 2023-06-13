<template>
  <div class="device-active-container">

    <InfoFeed>
      <div class="local-navbar">
        <div class="btns">
          <LocalButton 
            ref="Date.now()" 
            :first="true"
            @click="activeDeviceMenu='all'"
            :active="activeDeviceMenu === 'all' ? true : false"
            >Все</LocalButton>
            <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'category'"
            :active="activeDeviceMenu === 'category' ? true : false"
            >Категория</LocalButton>
            <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'specification'"
            :active="activeDeviceMenu === 'specification' ? true : false"
            >Спецификация</LocalButton>
            <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'status'"
            :active="activeDeviceMenu === 'status' ? true : false"
            >Статус</LocalButton>
            <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'place'"
            :active="activeDeviceMenu === 'place' ? true : false"
            >Место</LocalButton>
            <LocalButton 
            ref="Date.now()" 
            :last="true"
            @click="activeDeviceMenu = 'responsible'"
            :active="activeDeviceMenu === 'responsible' ? true : false"
            >Ответственный</LocalButton>
            
          </div>
          <AddDeviceButton 
          ref="Date.now()" 
          @click="showAdd = true"
          >Добавить устройство</AddDeviceButton>
      </div>
    </InfoFeed>
    <Popup @closePopup="closeAddDevice" v-if="showAdd"><AddDevice></AddDevice></Popup>
    <Transition name="fade-slide" appear>
      <div class="generic-container">
        <AllDevices v-if="activeDeviceMenu === 'all'"/>
        <CategorizedDevices v-if="activeDeviceMenu === 'category'"/>
        <StatusedDevices v-if="activeDeviceMenu === 'status'"/>
        <PlacedDevices v-if="activeDeviceMenu === 'place'"/>
        <ResponsiblesDevices v-if="activeDeviceMenu === 'responsible'"/>
        <SpecificationsDevices v-if="activeDeviceMenu === 'specification'"/>
      </div>
    </Transition>
  </div>
</template>

<script>
import InfoFeed from '@/components/info-feed/info-feed.vue'
import LocalButton from '@/components/buttons/local-button'
import AllDevices from './active-devices/all_devices'
import CategorizedDevices from './active-devices/category'
import StatusedDevices from './active-devices/status'
import PlacedDevices from './active-devices/place'
import ResponsiblesDevices from './active-devices/responsible'
import SpecificationsDevices from './active-devices/specification'
import Popup from '@/components/popup/popup'
import AddDevice from '@/components/device/add-device'
import AddDeviceButton from '@/components/buttons/add-device-button'

export default {
  name: 'ActiveDevices',
  data() {
    return {
      activeDeviceMenu: 'all',
      showAdd: false
    }
  },
  components: {
      InfoFeed,
      LocalButton,
      AllDevices,
      CategorizedDevices,
      StatusedDevices,
      PlacedDevices,
      ResponsiblesDevices,
      SpecificationsDevices,
      Popup,
      AddDevice,
      AddDeviceButton
  },
  methods: {
    changeActiveMenu(event) {
      this.activeDeviceMenu = event
    },
    closeAddDevice() {
      this.showAdd = false
    }
  }
}
</script>

<style lang="scss">
.device-active-container {
  display: flex;
  width: 100%;
  gap: 10px;
  // flex-grow: 0;     /* do not grow   - initial value: 0 */
  flex-direction: column;
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

.override_button {
  border: none;
  border-radius: 20px;
  padding: 0;
  margin: 0;
  width: 100%;
}

.btns {
  display: flex;
  width: 100%;
  justify-content: space-between;
  flex-direction: row;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease-in-out;
  transform: translateY(0px);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(100px);
}

.fadeHeight-enter-active,
.fadeHeight-leave-active {
  transition: all 2s;
  height: 100vh;
}
.fadeHeight-enter-from,
.fadeHeight-leave-to
{
  opacity: 0;
  max-height: 0px;
}

</style>