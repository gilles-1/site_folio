<template>
   <div style="text-align: center;">

    <!-- Carte Bootstrap avec Image d'Arrière-plan -->
<div class="card">
  <!-- Image d'arrière-plan en entête -->
  <div class="card-header">
    <!-- Image du portefeuille avec bordure arrondie -->
    <p class="m-0 p-0" style="text-align: center;">
    <img v-bind:src="imagePath" class="rounded-circle img-fluid h-50 w-50 " alt="Image Portefolio">
   
</p>
  </div>

  <InfoCom/>

  <div class="card-footer" style="text-align: center;">
    <!-- Liens d'icônes vers les réseaux sociaux et LinkedIn -->
    <a href="#" class="btn btn-outline-primary m-1"><i class="fab fa-facebook"></i></a>
    <a href="#" class="btn btn-outline-secondary m-1"><i class="fab fa-twitter"></i></a>
    <a href="https://github.com/gilles-1/" class="btn btn-outline-info m-1"><i class="fab fa-github"></i></a>
    <a href="https://www.linkedin.com/in/giltrand" class="btn btn-outline-dark m-1" target="_blank"><i class="fab fa-linkedin"></i></a>
  </div>
</div>
<a href="/cv.pdf">Télécharger CV <i class="fas fa-file-pdf"></i></a>
   </div>
    </template>
    
    <script>
import InfoCom from './InfoCom.vue';

    export default {
    data() {
        return {
            // Définir le chemin de l'image en fonction de l'emplacement dans votre projet
            imagePath: require('@/assets/moi.jpg'),
            name: 'AppSidebar', // Définir le nom par défaut
        };
    },
    components: { InfoCom }
}
    </script>

    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style>
    
    </style>
    