<template>
  <div id="app">

    <AppHeader>
    
      <li class="nav-item">
        <router-link to="/" class="nav-link" active>Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/" class="nav-link">Experience</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about" class="nav-link">About</router-link>
        </li>
      
    
  </AppHeader>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
import AppHeader from '@/components/AppHeader.vue'

export default {
  name: 'HomeView',
  components: {
    AppHeader
  }
}
</script>

<style>

</style>
