<template>
  <div class="card">
      <div class="card-header">
        <h6>Implications</h6>
    </div>
  
    <div class="card-body bg-dark bg-opacity-10" >
      <div class="row">
  
         <!-- Vfor -->
      <div v-for="exp in filteredDataEmploi" :key="exp.id"  class="card mb-2 mx-1" style="max-width: 815px;">    
        <div class="row no-gutters">
                  <!-- Icône FontAwesome -->
                  <div class="col-md-12">
                      <div class="card-body">
                        <div class="col-md-12">
                          <h6 class="card-title">{{ exp.title }}</h6>
                        </div>
                        <div class="row">
  
                          <div class="col-md-10">
                          <h7 class="">{{ exp.institution }} ({{ exp.city }}, {{ exp.country }})</h7>
                        </div>
                        <div class="col-md-2">
                          <h7 class="">{{ getYear(exp.started_at) }} - {{ getYear(exp.ended_at) }}</h7>
                        </div>
    
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
      sortedItems() {
      // Utilisez la méthode sort avec une fonction de comparaison pour trier par date
      return this.data.slice().sort((a, b) => {
        return new Date(b.started_at) - new Date(a.started_at);
      });
    },

      filteredDataEmploi() {
        return this.sortedItems.filter(item => item.typ === 'Implication');
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
        axios.get('http://localhost:8000/api/experience/')
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
    