// app.js
Vue.component('index', {
    // Utilisez la fonction `require` pour charger le contenu du fichier
    template: require('./Index.vue').default
  });
  
  new Vue({
    el: '#app',
    template: '<index></index>'
  });