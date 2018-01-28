<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapActions(['getBlogs']),
  },
  created() {
    this.getBlogs()
  },
}
</script>

<style style="scss">

</style>
