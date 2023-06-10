<template>
  <InfoFeed>
    <div class="local-navbar">
      <div class="btns">
        <div class="btn btn__first">
            <p>Все</p>
        </div>
        <div class="btn">
            <p>Категория</p>
        </div>
        <div class="btn">
            <p>Спецификация</p>
        </div>
        
        <div class="btn">
            <p>Статус</p>
        </div>
        <div class="btn">
            <p>Место</p>
        </div>
        <div class="btn btn__last">
            <p>Ответственный</p> 
        </div>
      </div>
    </div>
  </InfoFeed>
</template>

<script>
import InfoFeed from '@/components/info-feed/info-feed.vue'

export default {
  name: 'ActiveDevices',
  components: {
      InfoFeed
  }
}
</script>

<style lang="scss">
.local-navbar {
  padding: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  display: flex;
  gap: 10px;
  flex-direction: column;
  align-items: center;
  width: 100% - 5;
}

.btns {
  display: flex;
  width: 100%;
  justify-content: space-between;
  flex-direction: row;
}

.btn { 

  color: $color8;

  background: $color6;
  width: 100%;
  display: flex;
  flex: 1;
  justify-content: center;
  padding-left: 10px;
  padding-right: 10px;
  border-left: solid $color7;
  
  
  &__first {
    border-left: none;
    border-radius: 20px 0 0 20px;
  }
  
  &__last {
    border-radius: 0 20px 20px 0;
  }
  
  &:hover {
    background: $color7
  }
  
  
}

</style>