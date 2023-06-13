<template>
  <div class="all-devices-container">
    <InfoFeed>
      <div class="inner-container">
        <select v-model="selected">
          <option value="" disabled hidden>Выберите категорию</option>
          <option v-for="category in AVAILABLE_CATEGORIES" :value="category" :key="Math.random()">
            {{ category }}
          </option>
        </select>

        <svg width="50%" height="5">
          <rect width="100%" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      <Device
      v-if="CATEGORIZED_DEVICES.length"
      v-for="item in CATEGORIZED_DEVICES"
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
      this.GET_DEVICES_BY_CATEGORY(val);
    }
  },
  methods: {
    ...mapActions([
      'GET_AVAILABLE_CATEGORIES',
      'GET_DEVICES_BY_CATEGORY',
      'GET_DEVICE_FULL_INFO'
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
      'AVAILABLE_CATEGORIES',
      'CATEGORIZED_DEVICES'
    ]),
    getPopupState() {
      return this.popupActive
    },
  },
  mounted() {
    this.GET_AVAILABLE_CATEGORIES()
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