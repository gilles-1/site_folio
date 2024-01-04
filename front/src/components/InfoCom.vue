<template>
    <div class="card-body bg-dark bg-opacity-10" style="text-align: center;">
    <!-- Informations personnelles dans le corps -->
    <h5 class="card-title">Gilles Ngangue</h5>
    <p class="card-title">Analyste informatique</p>
    <p class="card-title">Montreal (Canada)</p>
    <p class="card-title">ngangueg@gmail.com</p>
    <p class="card-title">Tel : +1 873 660 1968</p>
    
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
  