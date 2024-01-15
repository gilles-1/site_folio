<template>
    <div>
    <div v-for="item in data" :key="item.id" class="card-body bg-dark bg-opacity-10" style="text-align: center;">
    <!-- Informations personnelles dans le corps -->
    <h5 class="card-title">{{ item.name }}</h5>
    <p class="card-title">{{ item.title }}</p>
    <p class="card-title">{{ item.city }} ({{ item.country }})</p>
    <p class="card-title">{{ item.email }}</p>
    <p class="card-title">Tel : {{ item.telephone }}</p>
    
  </div>

</div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'InfoCom',
  
  
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
      axios.get('http://localhost:8000/api/info/')
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
  