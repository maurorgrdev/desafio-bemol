import { defineStore } from 'pinia'
import { api } from 'boot/axios'

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
        async validarCEP(cep){
            try {
                const data = {
                    'cep': cep
                }
                const response = await api.post('/check-cep', data)

                return response.data
            } catch (error) {
                alert(error)
            }
        },

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

                return response
            } catch (error) {
                return error.response
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