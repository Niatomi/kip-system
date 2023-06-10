<template>
    <div class="chief-container">
        <div class="menu-container">
            <h4>Меню</h4>
            <Button class="btn_override">Приборы</Button>
            <Button class="btn_override">Сотрудники</Button>
            <Button class="btn_override">БД Приборов</Button>
        </div>
        <ActiveDevices/>
    </div>
</template>

<script>
import Button from '@/components/buttons/button.vue'
import ActiveDevices from '@/components/devices/active-devices'

export default {
    name: "ChiefPage",
    components: {
        Button,
        ActiveDevices
    },
    data() {
        return {
            
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
}

.btn_override {
    width: 75%;
    padding-left: 10px;
}


</style>
