<template>
  <div class="all-devices-container">
    <InfoFeed>
      <div class="inner-container">
        <select v-model="selected">
          <option value="" disabled hidden>Выберите место установки</option>
          <option v-for="place in AVAILABLE_PLACES" :value="place" :key="Math.random()">
            {{ place }}
          </option>
        </select>

        <svg width="50%" height="5">
          <rect width="100%" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      <Device
      v-if="DEVICES_BY_PLACE.length"
      v-for="item in DEVICES_BY_PLACE"
      :key="item.id"
      :device="item"
      @click="openInfo(item.id)"
      />
    </InfoFeed>
    <Popup 
    v-if="getPopupState" 
    @closePopup="closePopup()"
    >
      <AllDevicePopup :key="Date.now()"/>
    </Popup>
  </div>
</template>

<script>
import FindButton from '@/components/buttons/find-button'
import InfoFeed from '@/components/info-feed/info-feed'
import Button from '@/components/buttons/button'
import Device from '@/components/device/device'
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
      popupActive: false,
      selected: '',
    }
  },
  watch: {
    selected: function(val) {
      console.log(val);
      this.GET_DEVICES_BY_PLACE(val);
    }
  },
  methods: {
    ...mapActions([
      'GET_DEVICE_FULL_INFO',,
      'GET_DEVICES_BY_PLACE',
      'GET_AVAILABLE_PLACES'
    ]),
    openInfo(itemId) {
      this.GET_DEVICE_FULL_INFO(itemId).then(() => {
         this.popupActive = true
      })
    },
    closePopup() {
      this.popupActive = false
    }
  },
  computed: {
    ...mapGetters([
      'AVAILABLE_PLACES',
      'DEVICES_BY_PLACE'
    ]),
    getPopupState() {
      return this.popupActive
    },
  },
  mounted() {
    this.GET_AVAILABLE_PLACES()
  }
}
</script>

<style lang="scss" scoped>
.all-devices-container {
  margin-bottom: 10px;
}

select {
  width: 100%;
  border-radius: 20px;
  height: 45px;
  font-size: 30px;
  background: $color6;
  font-family: inherit;
  padding-left: 10px;
  
}

option {
  border-radius: 20px;
}

.inner-container {
  width: 100%;
  max-width: 97%;
  margin-top: 10px;
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}

.input-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 10px;
}

.search {
  color: $color8;
  padding-left: 15px;
  border: none;
  border-radius: 20px;
}

input {
  color: $color8;
}
</style>