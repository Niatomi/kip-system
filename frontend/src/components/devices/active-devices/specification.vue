<template>
  <div class="all-devices-container">
    <InfoFeed>
      <div class="inner-container">
        <select v-model="selected">
          <option value="" disabled hidden>Выберите спецификации</option>
          <option v-for="specification in AVAILABLE_SPECIFICATIONS" :value="specification" :key="Math.random()">
            {{ specification.trim() }}
          </option>
        </select>
        <div class="local-chosen-container">
          <span>
            <h4 class="chosen-text">Выбранные спецификации:</h4>
            <div class="specifications-container">
              <Specification 
              v-for="chosenSpec in arrayOfSpecifications" 
              @delete="deleteSpec(chosenSpec)"
              :key="Math.random()">
                {{ chosenSpec }}
              </Specification>
            </div>

          </span>
        </div>
        <Button class="search-button" @click="findDevices">Поиск</Button>
        <svg width="50%" height="5">
          <rect width="100%" height="5" style="fill: #d9d9d9" />
        </svg>
      </div>
      <Device
      v-if="DEVICES_BY_SPECIFICATIONS.length"
      v-for="item in DEVICES_BY_SPECIFICATIONS"
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
import Specification from '@/components/buttons/specification'
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
    AllDevicePopup,
    Specification
  },
  data() {
    return {
      popupActive: false,
      selected: '',
      arrayOfSpecifications: []
    }
  },
  watch: {
    selected: function(val) {
      // this.GET_DEVICES_BY_RESPONSIBLE(val);
      if (this.selected !== '') {
        let alreayExists = false;
        this.arrayOfSpecifications.forEach(value => {
          if (val === value) {
            alreayExists = true;
          } 
        })
        if (!alreayExists) {
          this.arrayOfSpecifications.push(val);
        }
      }
      this.selected = '';
    },
    arrayOfSpecifications: function(val) {
      if (!(toRaw(val).length)) {
        this.CLEAR_SPECIFICATION_DEVICES()
      }
    }
    
  },
  methods: {
    ...mapActions([
      'GET_DEVICE_FULL_INFO',
      'GET_AVAILABLE_SPECIFICATIONS',
      'GET_DEVICES_BY_SPECIFICATIONS',
      'CLEAR_SPECIFICATION_DEVICES'
    ]),
    openInfo(itemId) {
      this.GET_DEVICE_FULL_INFO(itemId).then(() => {
         this.popupActive = true
      })
    },
    closePopup() {
      this.popupActive = false
    },
    deleteSpec(spec) {
      this.arrayOfSpecifications = this.arrayOfSpecifications.filter(value => value !== spec)
    },
    findDevices() {
      this.GET_DEVICES_BY_SPECIFICATIONS(this.arrayOfSpecifications);
    }
  },
  computed: {
    ...mapGetters([
      'AVAILABLE_SPECIFICATIONS',
      'DEVICES_BY_SPECIFICATIONS'
    ]),
    getPopupState() {
      return this.popupActive
    },
  },
  mounted() {
    this.GET_AVAILABLE_SPECIFICATIONS();
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
  height: 60px;
  font-size: 30px;
  background: $color6;
  font-family: inherit;
  padding-left: 10px;
  border-radius: 20px 20px 0px 0px;
  
}

option {
  border-radius: 20px;
}
.specification {

}
.chosen-text {
  text-align: left;
  margin-bottom: 10px;
}

.specifications-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  flex-wrap: wrap;
  gap: 10px;
}
.local-chosen-container {
  width: 100%;
  text-align: center;
  align-items: center;
}
.search-button {
  width: 95%;
  text-align: center;
  width: 100%;
  padding: 0px;
  padding-top: 10px;
  padding-bottom: 10px;
  background: $color4;
  border-radius: 0 0 20px 20px;
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