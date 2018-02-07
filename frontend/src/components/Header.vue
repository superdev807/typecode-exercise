<template>
  <div class="tc-header">
    <div class="tc-menu">
      <img src="../assets/images/hamburger.svg" class="hamburger" />
    </div>

    <div v-show="!inEdit" class="tc-title">
      <div class="tc-title-back-wrap">
        <div class="tc-title-back">{{ title }}</div>

        <div v-if="editable && !inEdit" class="tc-title-start-edit-button" @click="startEdit"></div>
      </div>

      <div class="tc-title-text-wrap">
        <div class="tc-title-text">{{ title }}</div>
      </div>
    </div>

    <div v-show="inEdit" class="tc-title-edit">
      <input
        v-show="editable"
        placeholder="Enter title"
        v-model="titleInEdit"
        class="tc-title-input"
        :class="{ empty: isTitleEmpty }"
        @input="debouncedInput"
        @keyup.esc="cancelEdit"
        @keydown.enter="finishEdit"
      >

      <div class="tc-slug-in-edit">
        <span class="tc-slug-head">slug:&nbsp;</span>

        {{ slugInEdit }}

        <div class="tc-title-edit-button finish" @click="finishEdit"></div>
        <div class="tc-title-edit-button cancel" @click="cancelEdit"></div>
      </div>
    </div>

  </div>
</template>

<script>
import debounce from 'lodash/debounce'

import { getSlug } from '@/api'

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
  computed: {
    isTitleEmpty() {
      return this.inEdit && this.titleInEdit === ''
    },
  },
  methods: {
    debouncedInput: debounce(function(e) {
      const value = e.target.value

      this.titleInEdit = value

      if (this.titleInEdit === this.title) {
        this.slugInEdit = this.slug
      } else {
        getSlug({ title: this.titleInEdit }).then(response => {
          this.slugInEdit = response.data.slug
        })
      }
    }, 100),

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
      if (this.titleInEdit === '') {
        return
      }

      this.inEdit = false

      if (this.titleInEdit !== this.title) {
        this.$emit('changed', this.titleInEdit)
      }
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

  .tc-title {
    font-size: 5rem;
    line-height: 1.3;

    .tc-title-back-wrap {
      position: absolute;
      left: 12.5%;
      right: 32.5%;
      bottom: -2.5rem;

      .tc-title-back {
        display: inline;
        background: #fff;
        color: transparent;

        box-shadow: 1rem 0 #fff, -1rem 0 #fff;
        padding: 1rem 0;
      }

      .tc-title-start-edit-button {
        position: absolute;
        width: 40px;
        height: 40px;
        top: calc(-40px - 0.5rem);
        left: calc(-40px - 1rem);
        background: #f3e13b url('../assets/images/pencil.svg') center center
          no-repeat;

        &:hover {
          cursor: pointer;
        }
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
        padding-left: 12.5%;
        padding-right: 32.5%;
        padding-bottom: calc(100px - 2.5rem);
      }
    }
  }

  .tc-title-edit {
    position: absolute;
    left: 12.5%;
    right: 32.5%;
    bottom: 0;
    background: #fff;
    padding: 2rem 2rem 0;

    .tc-title-input {
      color: #1a1a1a;
      background: #f9f9f9;
      box-sizing: border-box;
      border: 1px solid #cbcbcb;
      font-size: 3rem;
      padding: 1rem;
      margin-bottom: 1rem;
      width: 100%;

      &:focus {
        color: #495057;
        background-color: #fff;
        border-color: #80bdff;
        outline: 0;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
      }

      &.empty {
        border-color: #dc3545;

        &:focus {
          border-color: #dc3545;
          box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25);
        }
      }
    }

    .tc-slug-in-edit {
      color: #666;
      font-family: Futura, Arial, Helvetica, sans-serif;
      font-size: 1rem;

      .tc-slug-head {
        color: #b2b2b2;
      }
    }

    .tc-title-edit-button {
      position: absolute;
      width: 40px;
      height: 40px;
      left: -40px;

      &:hover {
        cursor: pointer;
      }

      &.finish {
        top: -40px;
        background: #a2d05a url('../assets/images/checkmark.svg') center
          center/80% 80% no-repeat;
      }

      &.cancel {
        top: -81px;
        background: #e56d3e url('../assets/images/close.svg') center center/80%
          80% no-repeat;
      }
    }
  }
}
</style>
