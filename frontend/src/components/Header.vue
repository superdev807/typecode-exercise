<template>
  <div class="tc-header">
    <div class="tc-menu">
      <img src="../assets/images/hamburger.svg" class="hamburger" />
    </div>

    <div class="tc-title-back-wrap">
      <div class="tc-title-back">{{ title }}</div>
    </div>

    <div class="tc-title-text-wrap">
      <div class="tc-title-text">{{ title }}</div>
    </div>

    <input
      v-show="editable"
      placeholder="Enter title"
      v-model="titleInEdit"
      @input="debouncedInput"
      @keyup.esc="cancelEdit"
      @blur="cancelEdit"
      @keydown.enter="finishEdit"
    >
  </div>
</template>

<script>
import debounce from 'lodash/debounce'

export default {
  props: {
    title: String,
    slug: String,
    editable: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      inEdit: false,
      titleInEdit: '',
      slugInEdit: '',
    }
  },
  computed: {},
  methods: {
    debouncedInput: debounce(e => {
      const value = e.target.value
    }, 1000),

    startEdit() {
      if (this.editable) {
        this.inEdit = true
        this.titleInEdit = this.title
        this.slugInEdit = this.slug
      }
    },

    cancelEdit() {
      this.inEdit = false
    },

    finishEdit() {
      this.inEdit = false

      this.$emit('changed', this.titleInEdit)
    },
  },
}
</script>

<style lang="scss" scoped>
.tc-header {
  height: 800px;
  position: relative;
  background-image: url('../assets/images/background.jpg');
  background-size: 125% 1000px;
  background-position: center -100px;
  background-repeat: no-repeat;
  margin-bottom: 150px;
  margin-left: -70px;
  margin-right: -70px;

  .tc-menu {
    position: absolute;
    top: 100px;
    right: 70px;

    .hamburger {
      width: 300px;
    }
  }

  .tc-title-back-wrap {
    position: absolute;
    left: 10%;
    right: 30%;
    bottom: -2.5rem;

    .tc-title-back {
      display: inline;
      background: #fff;
      color: transparent;
      font-size: 5rem;
      box-shadow: 1rem 0 #fff, -1rem 0 #fff;
      padding: 1rem 0;
    }
  }

  .tc-title-text-wrap {
    position: absolute;
    left: 0;
    right: 0;
    bottom: -100px;

    .tc-title-text {
      background-image: url('../assets/images/background.jpg');
      background-size: 125% 1000px;
      background-position: center bottom;
      background-repeat: no-repeat;
      -webkit-text-fill-color: transparent;
      -webkit-background-clip: text;
      font-size: 5rem;
      padding-left: 10%;
      padding-right: 30%;
      padding-bottom: calc(100px - 2.5rem);
    }
  }
}
</style>
