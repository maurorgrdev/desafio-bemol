import { defineStore } from 'pinia'
import { api } from 'boot/axios'
import moment from 'moment';

export const useUsuarioStore = defineStore("usuario", {
    state: () => ({
        usuario: {},
        usuarios: [], 
    }),

    getters: {
        getUsuario(state){
            let copyUsuario = state.usuario

            return {
                ...copyUsuario,
                data_nascimento: moment(copyUsuario.data_nascimento +' 00:00:00', 'YYYY-MM-DD HH:mm:ss').format('DD/MMYYYY HH:mm:ss')
            }
        },

        getUsuarios(state){
            let copyUsuarios = state.usuarios.map((usuario) => {
                return {
                    ...usuario,
                    data_nascimento: moment(usuario.data_nascimento +' 00:00:00', 'YYYY-MM-DD HH:mm:ss').format('DD/MMYYYY HH:mm:ss')
                }
            })

           return copyUsuarios
        },
    },

    actions: {
        async loadUsuarios(){
            try {
                const result = await api.get('/users')

                this.usuarios = result.data
            } catch (error) {
                alert(error)
            }
        },

        async loadUsuario(id){
            try {
                const result = await api.get(`/users/${id}`)

                this.usuario = result.data
            } catch (error) {
                alert(error)
            }
        },

        async create(data){
            try {
                let data_nascimento_formated = moment(data.data_nascimento +' 00:00:00', 'DD/MM/YYYY HH:mm:ss').format('YYYY-MM-DD HH:mm:ss')

                const request = {
                    ...data,
                    data_nascimento: data_nascimento_formated,
                }
                const response = await api.post(`/users`, request)

                return response.data
            } catch (error) {
                return error.response
            }
        },

        async update(data){
            try {
                let data_nascimento_formated = moment(data.data_nascimento +' 00:00:00', 'DD/MM/YYYY HH:mm:ss').format('YYYY-MM-DD HH:mm:ss')
                
                const request = {
                    ...data,
                    data_nascimento: data_nascimento_formated,
                }

                console.log(request);
                console.log('hehe');

                const response = await api.put(`/users/${data.id}`, request)

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