<template>
    <div class="device-active-container">
      <Transition name="fade-slide" appear>
        <InfoFeed>
          <div class="local-navbar">
            <div class="btns">
              <LocalButton 
              ref="Date.now()" 
              :first="true"
              @click="activeDeviceMenu='plan'"
              :active="activeDeviceMenu === 'plan' ? true : false"
              >План поверок</LocalButton>
              <LocalButton 
              ref="Date.now()" 
              :last="true"
              @click="activeDeviceMenu = 'on_check'"
              :active="activeDeviceMenu === 'on_check' ? true : false"
              >Поставлены на поверку</LocalButton>
              
            </div>
          </div>
        </InfoFeed>
      </Transition>
      <Transition name="fade-slide" appear>
        <div class="generic-container">
          <PlannedDevices v-if="activeDeviceMenu === 'plan'"/>
          <OnCheckDevices v-if="activeDeviceMenu === 'on_check'"/>
        </div>
      </Transition>
    </div>
  </template>
  
  <script>
  import InfoFeed from '@/components/info-feed/info-feed.vue'
  import LocalButton from '@/components/buttons/local-button'
  import Popup from '@/components/popup/popup'
  import PlannedDevices from './planned-devices'
  import OnCheckDevices from './on-check-devices'
  
  export default {
    name: 'Statuses',
    data() {
      return {
        activeDeviceMenu: 'plan',
        showAdd: false
      }
    },
    components: {
        InfoFeed,
        LocalButton,
        Popup,
        PlannedDevices,
        OnCheckDevices
    },
    methods: {
    }
  }
  </script>
  
  <style lang="scss">
  .device-active-container {
    display: flex;
    width: 100%;
    gap: 10px;
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