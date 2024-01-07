<template>
    <div class="card">
    <div class="card-header">
      <p>Experience</p>
  </div>

  <div class="card-body bg-dark bg-opacity-10" >

    <div class="row">
    <div v-for="exp in data" :key="exp.id" class="card mb-2 mx-1" style="max-width: 815px;">
            <div class="row no-gutters">
                <!-- Icône FontAwesome -->
                <div class="col-md-12">
                    <div class="card-body">
                      <div class="col-md-12">
                        <h5 class="card-title">{{ exp.title }}</h5>
                      </div>
                        
                      <ul class="" >
                      <li class="" v-for="item in exp.task_set" :key="item.id">
                        {{ item.description }}
                      </li>
                      </ul>
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
    name: 'ExperienceView',
  
  
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
      axios.get('http://localhost:8000/api/experience/')
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
  