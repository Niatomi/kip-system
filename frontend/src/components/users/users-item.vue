<template>
  <div class="user-item-container">
    <div class="user-item-content">
      <p>{{ user.full_name }}</p>
      <p>Роль: {{ rolesFormat }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserItem',
  props: {
    user: {
      typeof: Object,
      default: {}
    }
  },
  computed: {
    rolesFormat() {
      if (this.user.role === 'ADMIN') {
        return 'Администратор'
      } 
      if (this.user.role === 'WORKER') {
        return 'Работник'
      } 
      if (this.user.role === 'CHIEF') {
        return 'Начальник'
      } 
      return this.user.role.charAt(0) + this.user.role.slice(1).toLowerCase()
    }
  },
  methods: {
  }
}
</script>

<style lang="scss">
.user-item-container {
  background: $color6;
  color: $color8;
  width: 100%;
  border-radius: 20px;
}

.user-item-content {
  padding: 10px;
}
</style>