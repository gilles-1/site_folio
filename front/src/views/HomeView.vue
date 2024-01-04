<template>
 
     <!--<img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to my portfolio"/> -->
    
    <div class="card">
    <div class="card-header">
      <p>Competences</p>
  </div>

  <div class="card-body bg-dark bg-opacity-10" >
    <SkillCom/>
  </div> 
  </div>

</template>

<script>
// @ is an alias to /src
//mport HelloWorld from '@/components/HelloWorld.vue'
import SkillCom from '@/components/SkillCom.vue'

export default {
  name: 'HomeView',
  components: {
    SkillCom
  }
}
</script>
