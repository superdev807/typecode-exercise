import axios from 'axios'

const client = axios.create({
  baseURL: process.env.BASE_API_URL,
})

export const getBlogs = () => {
  return client.get(`blogs/`)
}

export const updateBlog = payload => {
  return client.patch(`blogs/${payload.id}/`, payload)
}
