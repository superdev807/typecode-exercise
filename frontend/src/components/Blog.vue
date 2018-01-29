<template>
<div class="tc-blog">
  <tc-loading v-if="status.loading" />

  <div v-if="status.error" class="error">
    {{ status.error }}
  </div>

  <div v-if="status.success">
    <tc-header :title="blog.title" />

    <div class="content">
      <div class="row">
        <div class="col-xs-8
                    col-sm-6
                    col-md-4
                    col-lg-3">
            <p v-html="blog.summary"></p>

            <h2>{{ blog.subtitle }}</h2>

            <p v-html="blog.content"></p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters(['blog', 'status']),
  },
  created() {
    this.fetch()
  },
  watch: {
    $route: 'fetch',
  },
  methods: {
    fetch() {
      const { slug } = this.$route.params

      this.getBlog({ slug })
    },
    ...mapActions(['getBlog']),
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

</style>
