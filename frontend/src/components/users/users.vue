<template>
  <div class="users-container">
    <InfoFeed>
      <div class="local-navbar">
        <AddDeviceButton 
          ref="Date.now()" 
          @click="showAdd = true"
          >Добавить сотрудника</AddDeviceButton>
      </div>
    </InfoFeed>
    <Transition name="fade-slide" appear>
      <InfoFeed>
        <div class="generic-container">
          <div class="generic-content">
            <select v-model="selected">
              <option value="" disabled hidden>Выберите роль</option>
              <option value="ALL">Все</option>
              <option v-for="role in USER_ROLES" :value="role" :key="Math.random()">
                {{ rolesFormat(role) }}
              </option>
            </select>
            <svg width="50%" height="5">
              <rect width="100%" height="5" style="fill: #d9d9d9" />
            </svg>
            <UserItem v-for="user in USERS" :user="user" :key="Math.random()"/>
          </div>
        </div>
      </InfoFeed>
    </Transition>
    <Popup @closePopup="closeAddUser" v-if="showAdd"><AddUser/></Popup>
  </div>
</template>

<script>
import InfoFeed from '@/components/info-feed/info-feed.vue'
import LocalButton from '@/components/buttons/local-button'
import AddDeviceButton from '@/components/buttons/add-device-button'
import Popup from '@/components/popup/popup'
import { mapGetters, mapActions } from 'vuex'
import { toRaw } from 'vue'
import UserItem from './users-item'
import AddUser from './add-user'


export default {
  name: 'Users',
  components: {
    InfoFeed,
    AddDeviceButton,
    LocalButton,
    Popup,
    UserItem,
    AddUser
  },
  data() {
    return {
      selected: '',
      showAdd: false
    }
  },
  watch: {
    selected: function(val) {
      if (val === 'ALL') {
        this.GET_ALL_USERS()
      } else {
        this.GET_USERS_BY_ROLE(val)
      }
    }
  },
  computed: {
    ...mapGetters([
      'USER_ROLES',
      'USERS'
    ]),
  },
  methods: {
    ...mapActions([
      'GET_USER_ROLES',
      'GET_ALL_USERS',
      'GET_USERS_BY_ROLE'
    ]),
    rolesFormat(val) {
      let value = toRaw(val)
      if (value === 'ADMIN') {
        return 'Администратор'
      } 
      if (value === 'WORKER') {
        return 'Работник'
      } 
      if (value === 'CHIEF') {
        return 'Начальник'
      } 
      return value.charAt(0) + value.slice(1).toLowerCase()
    },
    closeAddUser() {
      this.showAdd = false;
    }
  },
  mounted() {
    this.GET_USER_ROLES()
    this.GET_ALL_USERS()
  }
}
</script>

<style lang="scss" scoped>
.users-container {
  display: flex;
  width: 100%;
  gap: 10px;
  flex-direction: column;
  margin-bottom: 10px;
}

.generic-container {
  width: 100%;
}

.generic-content {
  margin: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

select {
  width: 100%;
  border-radius: 20px;
  height: 45px;
  font-size: 30px;
  background: $color6;
  font-family: inherit;
  padding-left: 10px;
  border-radius: 20px;
  
}

option {
  border-radius: 20px;
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
</style>