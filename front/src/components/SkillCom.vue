<template>
  <div class="row">
  <div v-for="skill in data" :key="skill.id" class="card mb-1 mx-1" style="max-width: 400px;">
          <div class="row no-gutters">
              <!-- Icône FontAwesome -->
              <div class="col-md-2 mt-2">
                  <i :class="skill.font_awesome"></i>
              </div>
              <div class="col-md-10">
                  <div class="card-body">
                      <h5 class="card-title">{{ skill.name }}</h5>
                      <ul class="list-inline" v-for="item in skill.item_set" :key="item.id">
                        <li class="list-inline-item">{{ item.name }}</li>
                      </ul>
                  </div>
              </div>
          </div>
      </div>
      </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'SkillCom',


  data() {
  return {
    data: [],
  };
},
mounted() {
  this.fetchData();
},
methods: {
  fetchData() {
    axios.get('http://localhost:8000/api/skill/')
      .then(response => {
        this.data = response.data;
      })
      .catch(error => {
        console.error('Erreur lors de la requête API', error);
      });
  }
}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
