<template>
    <div class="cookie_container" v-if="!isAccepted">
        <p>Мы используем куки, надеюсь вы непротив...</p>
        <Button @click="acceptCookie">Ок</Button>
    </div>
</template>

<script>
import button from '@/components/buttons/button.vue'
import Button from '@/components/buttons/button.vue'
export default {
    name: 'CookieNotifier',
    components: {
        Button
    },
    data() {
        return {
            isAccepted: false
        }
    },
    methods: {
        acceptCookie() {
            this.isAccepted = true;
        }
    }
}
</script>

<style lang="scss" scoped>
.cookie_container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 20px;
    position: absolute;
    bottom: 8px;
    gap: 30px;
    border-radius: 20px;
    left: 8px;
    font-size: 18px;
    align-items: center;
    font-size: 20px;
    background: $color3;
} 
</style>

