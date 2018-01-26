<template>
  <div class="tc-header">
    <div class="tc-menu">
      <img src="../assets/images/hamburger.svg" class="hamburger" />
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
.tc-header {
  height: 800px;
  position: relative;
  background-image: url('../assets/images/background.jpg');
  background-size: 125% 125%;
  background-position: center center;
  background-repeat: no-repeat;

  .tc-menu {
    position: absolute;
    top: 100px;
    right: 70px;

    .hamburger {
      width: 300px;
    }
  }
}
</style>
