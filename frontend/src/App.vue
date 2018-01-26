<template>
  <div id="app">
    <div class="header">

    </div>

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
.header {
  height: 800px;
  background-image: url('./assets/images/background.jpg');
  background-size: 125% 125%;
  background-position: center center;
  background-repeat: no-repeat;
}

.body {
  margin: 0 70px;
}
</style>
