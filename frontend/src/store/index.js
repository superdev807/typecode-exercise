import Vue from 'vue'
import Vuex from 'vuex'

import * as api from '@/api'

Vue.use(Vuex)

const state = {
  blogs: [],
  blog: {},
  status: {
    loading: false,
    success: false,
    error: false,
  },
}

const getters = {
  blogs: state => {
    return state.blogs
  },
  blog: state => {
    return state.blog
  },
  getBlogById: state => id => {
    return state.blogs.find(blog => blog.id === id)
  },
  getBlogBySlug: state => slug => {
    return state.blogs.find(blog => blog.slug === slug)
  },
  status: state => {
    return state.status
  },
}

const mutations = {
  SET_BLOGS(state, payload) {
    state.blogs = payload
  },
  SET_BLOG(state, payload) {
    state.blog = payload
  },
  LOADING(state) {
    state.status = {
      loading: true,
      success: false,
      error: false,
    }
  },
  SUCCESS(state) {
    state.status = {
      loading: false,
      success: true,
      error: false,
    }
  },
  ERROR(state, payload) {
    state.status = {
      loading: false,
      success: false,
      error: payload,
    }
  },
  CLEAR_ERROR(state) {
    state.status = {
      loading: false,
      success: false,
      error: false,
    }
  },
}

const actions = {
  getBlogs({ commit }) {
    commit('LOADING')

    return api
      .getBlogs()
      .then(res => {
        const blogs = res.data

        commit('SUCCESS')
        commit('SET_BLOGS', blogs)

        return blogs
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },

  getBlog({ commit }, payload) {
    commit('LOADING')

    return api
      .getBlog(payload)
      .then(res => {
        const blog = res.data

        commit('SUCCESS')
        commit('SET_BLOG', blog)

        return blog
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },

  setBlog({ commit }, payload) {
    commit('SET_BLOG', payload)
  },

  updateBlog({ commit, dispatch }, payload) {
    commit('LOADING')

    return api
      .updateBlog(payload)
      .then(res => {
        const blog = res.data

        commit('SUCCESS')
        commit('SET_BLOG', blog)

        return blog
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },

  clearError({ commit }) {
    commit('CLEAR_ERROR')
  },
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions,
})
