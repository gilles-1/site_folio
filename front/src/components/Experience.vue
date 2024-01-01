<template>
    <div v-for="item1 in data" :key="item1.id" class="card mb-3 mt-3 ml-3" style="max-width: 500px;">
            <div class="row no-gutters">
                <!-- Icône FontAwesome -->
                <div class="col-md-2">
                    <i class="fas fa-cloud fa-4x mt-3 ml-3"></i>
                </div>
                <div class="col-md-10">
                    <div class="card-body">
                        <h5 class="card-title">{{ item1.name }}</h5>
                        <p class="card-text">Contenu de la Card. Vous pouvez ajouter du texte ici.</p>
                    </div>
                </div>
            </div>
        </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'Experience',
    props: {
      msg: String
    },

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
  