<template>
  <nav class="navbar navbar-expand-md fixed-top navbar-light bg-light">
      
      <div class="container">
        <a class="navbar-brand text-uppercase fw-bold" href="#">
          <span class="bg-primary bg-gradient p-1 rounded-3 text-light">Ngan</span> gue
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
                <!-- Liens de navigation -->
        <slot></slot>
        
      </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'AppHeader',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>
  