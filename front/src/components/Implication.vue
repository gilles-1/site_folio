<template>
    <div class="card">
      <div class="card-header">
        <p>{{ msg }}</p>
    </div>
  
    <div class="card-body">
        <p>{{ msg }}</p>
    </div>
   
      
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>
  