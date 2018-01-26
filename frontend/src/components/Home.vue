<template>
  <div class="tc-home">
    <tc-header title="Type/Code Blogs" />

    <div class="content">
      <div class="row">
        <div class="col-xs-4 col-xs-offset-1">
          <ul>
            <li>
              <router-link :to="{ name: 'blog', params: { slug: 'slug-1' }}">Blog 1</router-link>
            </li>
            <li>
              <router-link :to="{ name: 'blog', params: { slug: 'slug-2' }}">Blog 2</router-link>
            </li>
            <li>
              <router-link :to="{ name: 'blog', params: { slug: 'slug-3' }}">Blog 3</router-link>
            </li>
            <li>
              <router-link :to="{ name: 'blog', params: { slug: 'slug-4' }}">Blog 4</router-link>
            </li>
            <li>
              <router-link :to="{ name: 'blog', params: { slug: 'slug-5' }}">Blog 5</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
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
