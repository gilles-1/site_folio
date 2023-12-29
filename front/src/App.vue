<template>
  <div class= "m-0 p-0">
  <div class="container  " >
  <div class="col-md-12 ">

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
