import { defineStore } from 'pinia'
import { api } from 'boot/axios'

export const useClienteStore = defineStore("cliente", {
    state: () => ({
        cliente: {},
        clientes: [], 
    }),

    getters: {
        getCliente(state){
            return state.cliente
        },

        getClientes(state){
            return state.clientes
        },
    },

    actions: {
        async loadClientes(){
            try {
                const result = await api.get('/users')

                this.clientes = result.data
            } catch (error) {
                alert(error)
            }
        },

        async loadCliente(id){
            try {
                const result = await api.get(`/users/${id}`)

                this.cliente = result.data
            } catch (error) {
                alert(error)
            }
        },

        async create(data){
            try {
                const response = await api.post(`/users`, data)

                return response
            } catch (error) {
                alert(error)
            }
        },

        async update(data){
            try {
                const response = await api.post(`/users/${data.id}`, data)

                return response
            } catch (error) {
                alert(error)
            }
        },

        async delete(id){
            try {
                const result = await api.delete(`/users/${id}`)

                return result.data
            } catch (error) {
                alert(error)
            }
        }
    }

  });