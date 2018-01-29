<template>
<div class="tc-blog">
  <tc-loading v-if="status.loading" />

  <div v-if="status.error" class="error">
    {{ status.error }}
  </div>

  <div v-if="status.success">
    <tc-header :title="blog.title" editable />

    <div class="blog-content">
      <div class="row">
        <div class="col-xs-2 col-xs-offset-1">
          <div class="blog-info">
            <div class="blog-info-section">
              BY <span class="blog-info-author">{{ blog.author }}</span>
            </div>

            <div class="blog-info-section">
              {{ blogCreated }}
            </div>

            <div class="blog-info-section">
              <div v-for="(tag, index) in blogTags" :key="index" class="blog-info-tag">
                #{{ tag }}
              </div>
            </div>
          </div>
        </div>
        <div class="col-xs-5">
            <p>
              <span class="blog-location">
                {{ blog.location }}
              </span>
              <span v-html="blog.summary"></span>
            </p>

            <h2 class="blog-subtitle">{{ blog.subtitle }}</h2>

            <p v-html="blog.content"></p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import moment from 'moment'

export default {
  computed: {
    ...mapGetters(['blog', 'status']),
    blogCreated() {
      if (!this.blog) {
        return ''
      }

      return moment(this.blog.created).format('MMMM D, YYYY')
    },
    blogTags() {
      if (!this.blog) {
        return []
      }

      return JSON.parse(this.blog.tags)
    },
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
.blog-info {
  padding-right: 30%;
  font-family: Futura, Arial, Helvetica, sans-serif;
  font-size: 0.8rem;

  .blog-info-section {
    color: #b2b2b2;
    padding: 1rem 0 3rem;
    border-top: 1px solid #e5e5e5;

    .blog-info-author {
      color: #6f4f31;
      font-size: 1rem;
    }

    .blog-info-tag {
      margin-bottom: 0.5rem;
      text-transform: uppercase;
    }
  }
}

.blog-content {
  padding-right: 13%;
  font-family: Palatino, serif;

  p {
    margin: 0 0 2rem;
  }

  .blog-location {
    font-family: Futura;
    font-size: 0.9rem;
    margin-right: 1rem;
  }

  .blog-subtitle {
    margin-left: -3rem;
    color: #8a98a6;
  }
}
</style>
