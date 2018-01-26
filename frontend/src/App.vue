<template>
  <div id="app">
    <tc-header></tc-header>

    <div class="content">
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
.content {
  margin: 0 70px;
}
</style>
