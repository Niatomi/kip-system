<template>
  <div class="generic-container">
    <div class="popup-container" @click="closePopup">
    </div>
      <div class="content">
        <Button class="override_btn" @click="closePopup">Закрыть</Button>
        <div class="popup-device-info">
          <slot></slot>
        </div>
      </div>
    </div>
</template>

<script>
import Button from '@/components/buttons/button'
export default {
  name: 'Popup',
  components: {
    Button
  },
  data() {
    return {
    }
  },
  methods: {
    closePopup() {
      this.$emit('closePopup')
    }
  }
}
</script>

<style lang="scss" scoped>
.popup-container {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.5);
  transition: opacity 500ms;
  opacity: 1;
}

.popup-device-info {
  display: flex;
  padding-top: 20px;
  flex-direction: column;
  gap: 10px;
}

.content {
  position: fixed;
  overflow: auto;
  left: 40%;
  right: 0;
  top: 0;
  bottom: 0;
  padding: 20px;
  background: #fff;
  color: $color8;
  border-radius: 5px;
  transition: all 5s ease-in-out;

  &::-webkit-scrollbar {
    width: 12px;               /* width of the entire scrollbar */
  }

  &::-webkit-scrollbar-track {
    background: $color7;        /* color of the tracking area */
  }

  &::-webkit-scrollbar-thumb {
    background-color: $color8;    /* color of the scroll thumb */
    border-radius: 20px;       /* roundness of the scroll thumb */
    border: 3px solid $color7;  /* creates padding around scroll thumb */
  }
}

.override_btn {
  display: flex;
  color: $color8;
  background: $color7;
  padding: 2px;
  justify-content: center;
  
  &:hover {
    background: $color5;
  }
}



</style>