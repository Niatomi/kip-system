<template>
  <div class="device-active-container">

    <InfoFeed>
      <div class="local-navbar">
        <div class="btns">
          <LocalButton 
            ref="Date.now()" 
            :first="true"
            @click="activeDeviceMenu='all'"
            >Все</LocalButton>
          <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'category'"
            >Категория</LocalButton>
          <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'specification'"
            >Спецификация</LocalButton>
          <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'status'"
            >Статус</LocalButton>
          <LocalButton 
            ref="Date.now()" 
            @click="activeDeviceMenu = 'place'"
            >Место</LocalButton>
          <LocalButton 
            ref="Date.now()" 
            :last="true"
            @click="activeDeviceMenu = 'responsible'"
            >Ответственный</LocalButton>
            
        </div>
      </div>
    </InfoFeed>
    <Transition name="fade-slide" appear>
      <AllDevices v-if="activeDeviceMenu === 'all'"/>
    </Transition>
  </div>
</template>

<script>
import InfoFeed from '@/components/info-feed/info-feed.vue'
import LocalButton from '@/components/buttons/local-button'
import AllDevices from './active-devices/all_devices'

export default {
  name: 'ActiveDevices',
  data() {
    return {
      activeDeviceMenu: ''
    }
  },
  components: {
      InfoFeed,
      LocalButton,
      AllDevices,
      
  },
  methods: {
    changeActiveMenu(event) {
      this.activeDeviceMenu = event
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