<template>
    <div class="chief-container">
        <div class="menu-container">
            <h4>Меню</h4>
            <Button class="btn_override" ref="Date.now()" @click="menu='activeDevices'">Приборы</Button>
            <Button class="btn_override" ref="Date.now()" @click="menu='users'">Сотрудники</Button>
            <Button class="btn_override" ref="Date.now()" @click="menu='devicePool'">БД Приборов</Button>
        </div>
        <Transition name="fade-slide" appear>
            <ActiveDevices v-if="menu === 'activeDevices'"/>
        </Transition>
    </div>
</template>

<script>
import Button from '@/components/buttons/button.vue'
import ActiveDevices from '@/components/devices/active-devices'
import { Transition } from "vue";

export default {
    name: "ChiefPage",
    components: {
        Button,
        ActiveDevices
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
    gap: 1%;
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


</style>
