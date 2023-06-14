<template>
  <div class="add-device-container">
    <form @submit.prevent="addDeviceToPool" class="form-container">
      <span>
        <label for="text">Назввание:</label>
        <input type="text" v-model="name" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Описание:</label>
        <textarea type="text" v-model="description" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Категория:</label>
        <input type="text" v-model="category" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Цена:</label>
        <input type="text" v-model="price" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Интервал проверок (дни):</label>
        <input type="text" v-model="check_intervals" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Ресурс (года):</label>
        <input type="text" v-model="resource" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Срок полезного использования (года):</label>
        <input type="text" v-model="resource_of_useful_usage" placeholder="Введите значение"/>
      </span>
      <span>
        <label for="text">Спецификации:</label>
        <div class="specification-container" v-for="spec in specifications" :key="spec[0]">
          <input type="text" class="override_input" v-model="spec[1]" placeholder="Введите характеристики" />
          <input type="text" class="override_input" v-model="spec[2]" placeholder="Введите значение" />
          <button class="search_btn" @click="deleteSpecification(spec[0])">
            <i class="material-icons">close</i>
          </button>
        </div>
      </span>
      <button type="add_panel" class="override_btn" @click.prevent="addRow()"><h4>Добавить поле</h4></button>
      
      <button type="submit"><h4>Добавить прибор в базу</h4></button>
    </form>
    <h4 v-if="deviceCreated">Прибор успешно добавлен</h4>
    <h4 v-else>{{ error_msg }}</h4>
  </div>
</template>


<script>
import { mapActions } from 'vuex'

export default {
  name: 'AddDevicePool',
  data() {
    return {
      name: '',
      description: '',
      category: '',
      price: '',
      resource: '',
      check_intervals: '',
      resource_of_useful_usage: '',
      specifications: [[0, '', '']],

      deviceCreated: false,
      error_msg: ''
    }
  },
  computed: {
    getSpecs() {
      return this.specifications
    },
  },
  methods: {
    ...mapActions([
      'ADD_INTO_POOL_DEVICES'
    ]),
    addRow() {
      this.specifications.push([this.specifications.length, '', ''])
    },
    deleteSpecification(key) {
      if (this.specifications.length === 1) {
        return false;
      }

      let arr = []
      this.specifications.forEach(value => {
        if (value[0] !== key) {
          arr.push(value)
        }
      })
      this.specifications = arr
    },
    addDeviceToPool() {
      let data = {}
      let specs = []
      this.specifications.forEach(value => {
        let buf_object = {}
        buf_object[value[1]] = value[2];
        specs.push(buf_object)
      })
      
      let buf_obj = {}

      buf_obj['description'] = this.description
      buf_obj['specifications'] = specs
      data['device_specs'] = buf_obj

      buf_obj = {}
      buf_obj['name'] = this.name
      buf_obj['category'] = this.category
      buf_obj['price'] = this.price
      buf_obj['resource'] = this.resource
      buf_obj['check_intervals'] = this.check_intervals
      buf_obj['resource_of_useful_usage'] = this.resource_of_useful_usage
      
      data['device_info'] = buf_obj
      
      this.ADD_INTO_POOL_DEVICES(data).then((response) => {
        if (response.status === 201) {
          this.deviceCreated = true;
          this.error_msg = ''
          return this.deviceAdded;
        } else {
          this.error_msg = 'Ошибка валидации данных'
          this.deviceCreated = false;
          return this.error_msg;
        }
      })
      this.name=''
      this.description=''
      this.category=''
      this.price=''
      this.resource=''
      this.check_intervals=''
      this.resource_of_useful_usage=''
      this.specifications=[[0, '', '']]
    }
  }
}
</script>

<style lang="scss" scoped>

span {
  display: flex;
  flex-direction: column;
}

.override_btn {
  background: $color7;
  color: $color8;
}

input {
  border-radius: 20px;
  border: none;
  background: $color7;
  padding: 5px;
  padding-left: 10px;
}


.specification-container {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-grow: 0;
  flex-basis: content;
  gap: 10px;
  margin-bottom: 10px;
}
.override_input {
  width: 50%;
}

textarea {
  border-radius: 20px;
  font-size: inherit;
  font-family: inherit;
  border: none;
  background: $color7;
  padding: 5px;
  height: 500px;
  padding-left: 10px;
  overflow: auto;

  overflow-y: auto;
  word-wrap:break-word

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

button {
  border-radius: 20px;
  width: 100%;
}

select {
  width: 100%;
  border-radius: 20px;
  height: 45px;
  font-size: 30px;
  background: $color7;
  font-family: inherit;
  padding-left: 10px;
  border-radius: 20px;
  border: none;
  
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

option {
  border-radius: 20px;
}

.search_btn {
  width: fit-content;
  padding-left: 10px;
  margin: 10px;
  background: #e70f0f;
  padding-right: 10px;
  border-radius: 100%;
}

button {
  border-radius: 20px;
  width: 100%;
}
</style>
