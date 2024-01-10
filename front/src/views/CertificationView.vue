<template>
  <div class="card">
      <div class="card-header">
        <p>Formation</p>
    </div>
  
    <div class="card-body bg-dark bg-opacity-10" >
      <div class="row">
  
         <!-- Vfor -->
      <div v-for="forma in filteredData" :key="forma.id"  class="card mb-2 mx-1" style="max-width: 815px;">    
        <div class="row no-gutters">
                  <!-- Icône FontAwesome -->
                  <div class="col-md-12">
                      <div class="card-body">
                        <div class="col-md-12">
                          <h6 class="card-title">{{forma.title }}</h6>
                        </div>
                        <div class="row">
                          <div class="col-md-10">
                          <h6 class="">{{ forma.name }} <span v-if="forma.in_progress === true"><i>(En cours)</i></span> <span v-else></span></h6>
                        </div>
                        <div class="col-md-2">
                          <h6 class="">{{ getYear(forma.started_at) }} - {{ getYear(forma.ended_at) }}</h6>
                        </div>
                        <div class="col-md-12">
                          <h7 class="">{{ forma.institution }} ({{ forma.city }}, {{ forma.country }})</h7>
                        </div>
                        </div>
                          
                      </div>
                  </div>
              </div>
          </div>
           <!-- Vfor -->
  
  
  
  
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
  
    computed: {
      filteredData() {
        return this.data.filter(item => item.typ === 'Certification');
      },
      filteredDataStage() {
        return this.data.filter(item => item.typ === 'Stage');
      },
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
      },
  
      getYear(date) {
        return new Date(date).getFullYear();
      },
  
     
    }
    
    }
    </script>
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style scoped>
    
    </style>
    