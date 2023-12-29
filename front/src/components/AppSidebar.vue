<template>
   <div >

    <!-- Carte Bootstrap avec Image d'Arrière-plan -->
<div class="card">
  <!-- Image d'arrière-plan en entête -->
  <div class="card-header">
    <!-- Image du portefeuille avec bordure arrondie -->
    <p class="m-0 p-0" style="text-align: center;">
    <img v-bind:src="imagePath" class="rounded-circle img-fluid h-50 w-50 " alt="Image Portefolio">
   
</p>
  </div>

  <div class="card-body">
    <!-- Informations personnelles dans le corps -->
    <h5 class="card-title">Nom Prénom</h5>
    <p class="card-text">Poste / Profession</p>
    <p class="card-text">Description personnelle ou professionnelle.</p>
  </div>

  <div class="card-footer">
    <!-- Liens d'icônes vers les réseaux sociaux et LinkedIn -->
    <a href="#" class="btn btn-outline-primary"><i class="fab fa-facebook"></i></a>
    <a href="#" class="btn btn-outline-secondary"><i class="fab fa-twitter"></i></a>
    <a href="#" class="btn btn-outline-info"><i class="fab fa-instagram"></i></a>
    <a href="https://www.linkedin.com/in/votreprofil" class="btn btn-outline-dark" target="_blank"><i class="fab fa-linkedin"></i></a>
  </div>
</div>

   </div>
    </template>
    
    <script>
    export default {

        data() {
    return {
      // Définir le chemin de l'image en fonction de l'emplacement dans votre projet
      imagePath: require('@/assets/noir.png'),
      name: 'AppSidebar', // Définir le nom par défaut
    };
  }
      
      
      

      
      
    }
    </script>

    

    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style>
    
    </style>
    