<template>
  <div class= "m-0 p-0">
  <div class="container  " >
  <div class="col-md-12 ">

    <AppHeader>
    
        <li class="nav-item">
          <router-link to="/" class="nav-link">Compétence</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/experience" class="nav-link">Expérience</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/formation" class="nav-link">Formation</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/projet" class="nav-link">Projet</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/certification" class="nav-link">Certification</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/implication" class="nav-link">Implication</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about" class="nav-link">A propos</router-link>
        </li>
        <li class="nav-item">
          
          <router-link to="/about" class="nav-link"></router-link>
          <i class="fa fa-file-pdf-o" aria-hidden="true"></i>
        </li>
  </AppHeader>
</div>
<div class="row" style="margin-top: 70px; margin-bottom: 30px;"  id="app">
      <div class="col-md-3 ">
      <AppSidebar/>
    </div>
  <div class="col-md-9">
    <router-view/>
  </div>
    
</div>
</div>
<AppFooter/>
</div>
</template>

<script>
// @ is an alias to /src
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
import AppSidebar from '@/components/AppSidebar.vue'

export default {
  name: 'HomeView',
  components: {
    AppHeader,
    AppFooter,
    AppSidebar
  }
}
</script>

<style>

</style>
