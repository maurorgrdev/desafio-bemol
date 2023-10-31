import { defineStore } from 'pinia'
import { api } from 'boota/axios'

export const useAddressStore = defineStore("address", {
    state: () => ({
        address: {},
    }),

    getters: {
        getAddress(state){
            return state.address
        },
    },

    actions: {
        async loadAddress(id){
            try {
                const response = await api.get(`/addresses/${id}`)

            } catch (error) {
                alert(error)
            }
        },

        async create(data){
            try {
                const response = await api.post('/addresses', data)
            } catch (error) {
                alert(error)
            }
        },

        async update(data){
            try {
                const response = await api.post(`/addresses/${data.id}`, data)

                return response
            } catch (error) {
                alert(error)
            }
        },

        async delete(id){
            try {
                const result = await api.delete(`/addresses/${id}`)

                return result.data
            } catch (error) {
                alert(error)
            }
        }
    }
})