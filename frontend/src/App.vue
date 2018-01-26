<template>
  <div id="app">
    <tc-header></tc-header>

    <div class="body">
      <div class="container-fluid">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style style="scss">
.body {
  margin: 0 70px;
}
</style>
