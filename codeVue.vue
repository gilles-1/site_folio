<template>
  <div class="row">
  <div v-for="skill in data" :key="skill.id" class="card mb-1 mx-1" style="max-width: 400px;">
          <div :class="{ 'bg-primary bg-opacity-10 row no-gutters': isHovered }" @mouseover="setHover(true)" @mouseout="setHover(false)">
              <!-- Icône FontAwesome -->
              <div class="col-md-2 mt-2" >
                  <i :class="skill.font_awesome"></i>
              </div>
              <div class="col-md-10">
                  <div class="card-body">
                      <h5 class="card-title">{{ skill.name }}</h5>
                      <ul class="list-inline custom-list" >
                      <li class="list-inline-item" v-for="item in skill.item_set" :key="item.id">
                        {{ item.name }}
                      </li>
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
    data: [], isHovered: false,
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
  },

  setHover(value) {
      this.isHovered = value;
    },

},


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Supprimer les puces par défaut et ajouter des puces personnalisées */
.custom-list {
  list-style: none;
}

.custom-list li::before {
  content: "\2022"; /* Utilisation du caractère de puce (bullet) Unicode */
  color: #3d556e; /* Couleur de la puce */
  font-size: 1.5em; /* Taille de la puce */
  margin-right: 0em; /* Espacement entre la puce et le texte */
}

</style>



//////////////////////////////////////////////////////////////////////////

<template>
  <div>
    <ul>
      <!-- Utilisation de v-for pour générer une liste d'éléments -->
      <li v-for="(item, index) in items" :key="index" @click="handleItemClick(index)">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: ['Élément 1', 'Élément 2', 'Élément 3'],
    };
  },
  methods: {
    handleItemClick(index) {
      // Effectuez l'action souhaitée sur l'élément spécifique
      console.log(`Élément cliqué : ${this.items[index]}`);
      // Vous pouvez effectuer d'autres actions ici
    },
  },
};
</script>





//////////////////////////////////////


<template>
  <div>
    <ul>
      <!-- Utilisation de v-for pour générer une liste d'éléments -->
      <li v-for="(item, index) in items" :key="index" @mouseover="handleMouseOver(index)" @mouseout="handleMouseOut(index)" :class="{ 'bg-info': isHovered[index] }">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: ['Élément 1', 'Élément 2', 'Élément 3'],
      isHovered: Array(3).fill(false), // Initialisation du tableau de survol avec la même longueur que le tableau d'éléments
    };
  },
  methods: {
    handleMouseOver(index) {
      // Marquer l'élément comme survolé lors du survol
      this.$set(this.isHovered, index, true);
    },
    handleMouseOut(index) {
      // Annuler le survol lorsque la souris quitte l'élément
      this.$set(this.isHovered, index, false);
    },
  },
};
</script>


///////////////////////////////////////////////////////////////////////////////////////////////


<!-- votre_template.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Action sur un élément avec Vue.js</title>

  <!-- Inclure le fichier CSS de Bootstrap -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>

  <div id="app" class="container mt-5">
    <div v-for="element in elements" :key="element.id">
      <!-- Utilisation de la classe Bootstrap pour styliser l'élément -->
      <div class="card mb-3" @click="effectuerAction(element.id)">
        <div class="card-body">
          {{ element.nom }}
        </div>
      </div>
    </div>
  </div>

  <!-- Inclure Vue.js et le fichier JS de Bootstrap (jQuery inclus) -->
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

  <!-- Inclure Vue.js -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>

  <script>
    new Vue({
      el: '#app',
      data: {
        elements: {{ elements|safe }}, // Charger les éléments depuis Django
      },
      methods: {
        effectuerAction(id) {
          // Mettez ici votre logique pour effectuer une action sur l'élément spécifié par son ID
          console.log('Action effectuée sur l\'élément avec ID :', id);
        },
      },
    });
  </script>
</body>
</html>
