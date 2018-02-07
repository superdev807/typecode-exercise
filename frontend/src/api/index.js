import axios from 'axios'

const client = axios.create({
  baseURL: process.env.BASE_API_URL,
})

export const getBlogs = () => {
  return client.get(`blogs/`)
}

export const getBlog = payload => {
  return client.get(`blogs/${payload.slug}/`)
}

export const updateBlog = payload => {
  return client.patch(`blogs/${payload.slug}/`, payload)
}

export const getSlug = payload => {
  return client.post(`blogs/slug/`, payload)
}
