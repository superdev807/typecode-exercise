import Vue from 'vue'
import Vuex from 'vuex'

import * as api from '@/api'

Vue.use(Vuex)

const state = {
  blogs: [],
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
  UPDATE_BLOG(state, payload) {
    const blog = state.blogs.find(blog => blog.id === payload.id)

    if (blog) {
      Object.assign(blog, payload)
    }
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
  getBlogs({ commit, getters: { pagination } }) {
    commit('LOADING')
    api
      .getBlogs()
      .then(res => {
        commit('SET_BLOGS', res.data)
        commit('SUCCESS')
      })
      .catch(e => {
        commit('ERROR', e.response.data)
      })
  },

  updateBlog({ commit, dispatch }, payload) {
    commit('LOADING')
    api
      .updateBlog(payload)
      .then(res => {
        commit('SUCCESS')
        commit('UPDATE_BLOG', res.data)
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
