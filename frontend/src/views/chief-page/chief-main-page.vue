<template>
  <Transition name="fade-slide1" appear>
    <div class="chief-container">
      <div class="menu-container">
        <h4>Меню</h4>
        <Button 
        class="btn_override" 
        ref="Date.now()" 
        @click="menu='activeDevices'"
        :active="menu === 'activeDevices' ? true : false">
        Приборы</Button>
        <Button 
        class="btn_override" 
        ref="Date.now()" 
        @click="menu='users'"
        :active="menu === 'users' ? true : false"
        >Сотрудники</Button>
        <Button 
        class="btn_override" 
        ref="Date.now()" 
        @click="menu='devicePool'"
        :active="menu === 'devicePool' ? true : false"
        >БД Приборов</Button>
      </div>
      <Transition name="fade-slide" appear>
        <div class="generic-container">
          <ActiveDevices v-if="menu === 'activeDevices'"/>
          <Users v-if="menu === 'users'"/>
          <DevicePool v-if="menu === 'devicePool'"/>
        </div>
      </Transition>
    </div>
  </Transition>
</template>

<script>
import Button from '@/components/buttons/button.vue'
import ActiveDevices from '@/components/devices/active-devices'
import DevicePool from '@/components/devices/device-pool'
import Users from '@/components/users/users'
import { Transition } from "vue";


export default {
  name: "ChiefPage",
  components: {
    Button,
    ActiveDevices,
    Transition,
    Users,
    DevicePool
  },
  data() {
    return {
      menu: ''
    }
  }
}
</script>

<style lang="scss" scoped>


.chief-container {
    display: flex;
    gap: 10px;
}

.generic-container {
  width: 100%;
}

.menu-container {
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    background: $color2;
    width: 20%;
    gap: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
    height: fit-content;
    align-items: center;
    justify-content: center;
    flex-grow: 0; 
    flex-shrink: 0;
}

.btn_override {
    width: 75%;
    padding-left: 10px;
}


.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease-in-out;
  transform: translateX(0px);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(100px);
}


.fade-slide1-enter-active,
.fade-slide1-leave-active {
  transition: opacity 1s ease, transform 1s ease-in-out;
  transform: translateY(0px);
}

.fade-slide1-enter-from,
.fade-slide1-leave-to {
  opacity: 0;
  transform: translateY(40px);
}

</style>
