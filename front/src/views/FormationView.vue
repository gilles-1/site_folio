<template>
    <div class="card">
    <div class="card-header">
      <p>Formation</p>
  </div>

  <div class="card-body bg-dark bg-opacity-10" >

    <div class="row">
    <div v-for="exp in data" :key="exp.id" class="card mb-2 mx-1" style="max-width: 400px;">
            <div class="row no-gutters">
                <!-- Icône FontAwesome -->
                <div class="col-md-2">
                    <i class="fas fa-cloud fa-3x"></i>
                </div>
                <div class="col-md-10">
                    <div class="card-body">
                        <h5 class="card-title">{{ exp.name }}</h5>
                        <p class="card-text">Contenu de la Card. Vous pouvez</p>
                    </div>
                </div>
            </div>
        </div>
        </div>

      </div> 
  </div>

  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'FormationView',
  
  
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
      axios.get('http://localhost:8000/api/formation/')
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
  