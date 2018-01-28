<template>
  <div class="tc-home">
    <tc-header title="Type/Code Blogs" />

    <div class="content">
      <div class="row">
        <div class="col-xs-7 col-xs-offset-1">
          <ul>
            <li v-for="{slug, title, id} in blogs" :key="id">
              <router-link :to="{ name: 'Blog', params: { slug }}">{{ title }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(['blogs']),
  },
}
</script>

<style lang="scss" scoped>
.content {
  font-size: 20px;
  margin-bottom: 100px;

  ul {
    list-style: none;

    li {
      padding: 15px;
    }
  }
}
</style>
