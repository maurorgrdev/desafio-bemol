<template>
    <q-page>
        <q-card-section>
            <q-form ref="myForm" class="q-gutter-md">
                <div class="row">
                    <div class="q-pa-sm col-12">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.name" 
                            label="Nome Completo*" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                </div>
                <div class="row">
                    <div class="q-pa-sm col-4">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.cpf" 
                            label="CPF *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                    <div class="q-pa-sm col-4">
                        <q-input dense outlined v-model="dadosUsuario.data_nascimento" :rules="['date']">
                            <template v-slot:append>
                                <q-icon name="event" class="cursor-pointer">
                                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                                    <q-date v-model="dadosUsuario.data_nascimento" mask="DD/MM/YYYY">
                                    <div class="row items-center justify-end">
                                        <q-btn v-close-popup label="Close" color="primary" flat />
                                    </div>
                                    </q-date>
                                </q-popup-proxy>
                                </q-icon>
                            </template>
                        </q-input>            
                    </div>
                </div>
                <div class="row">
                    <div class="q-pa-sm col-6">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.email" 
                            label="Email *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                    <div class="q-pa-sm col-6">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.confirm_email" 
                            label="Confirmação de Email *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                </div>
                <div class="row">
                    <div class="q-pa-sm col-6">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.password" 
                            label="Senha de acesso*" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                    <div class="q-pa-sm col-6">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.confirm_password" 
                            label="Confirme sua senha *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                </div>
            </q-form>
        </q-card-section>

        <q-card-actions class="row text-primary" style="padding-left: 15px; padding-right: 15px;">
            <q-space />
            <q-btn @click="clickCancel" outline style=" width: 150px; color: primary;" label="Cancelar" />
            <q-btn @click="clickSubmit" style=" width: 150px;" color="primary" label="Salvar" />
          </q-card-actions>
    </q-page>
</template>

<script>
import { useUsuarioStore } from 'src/stores/usuario';

export default {
    setup(){
        const usuarioStore = useUsuarioStore()

        return {
            usuarioStore,
        }
    },

    data() {
        return {
            messageError: '',

            dadosUsuario: {
                name: '',
                cpf: '',
                email: '',
                confirm_email: '',
                password: '',
                confirm_password: '',
                data_nascimento: '',
            },

            proxyDataNascimento: '',
        }
    },

    methods: {

        clickCancel(){
            this.$router.push('/usuarios')
        },

        async clickSubmit(){
            if(await this.validarFormulario_NovoUsuario()){
                let response = this.usuarioStore.create(this.dadosUsuario)

                this.$router.push('/usuarios')

                // aqui
                // console.log(response)
                // console.log(response.status)
                // if(response.status === 201){
                //     this.$router.push('/usuarios')
                // } else {
                //     alert('Deu ruim')
                //     console.log(response)
                // }
            } else {
                alert(this.messageError)
            }
        },

        // Validar campos preenchidos pelo usuário
        validarFormulario_NovoUsuario(){
            if((this.dadosUsuario.name === '') || this.dadosUsuario.name === null || this.dadosUsuario.name.length <= 0){
                this.messageError = 'Informe uma nome válido';
                return false;
            }

            if((this.dadosUsuario.cpf === '') || this.dadosUsuario.cpf === null || this.dadosUsuario.cpf.length <= 0){
                this.messageError = 'Informe uma cpf válido';
                return false;
            }

            if((this.dadosUsuario.data_nascimento === '') || this.dadosUsuario.data_nascimento === null || this.dadosUsuario.data_nascimento.length <= 0){
                this.messageError = 'Informe uma data de nascimento válida';
                return false;
            }

            if((this.dadosUsuario.email === '') || this.dadosUsuario.email === null || this.dadosUsuario.email.length <= 0){
                this.messageError = 'Informe um e-mail válido';
                return false;
            }

            if((this.dadosUsuario.confirm_email === '') || this.dadosUsuario.confirm_email === null || this.dadosUsuario.confirm_email.length <= 0 || !(this.dadosUsuario.confirm_email === this.dadosUsuario.email)){
                this.messageError = 'Emails não coincidem';
                return false;
            }

            if((this.dadosUsuario.password === '') || this.dadosUsuario.password === null || this.dadosUsuario.password.length <= 0 ){
                this.messageError = 'Informe uma senha';
                return false;
            }

            if((this.dadosUsuario.confirm_password === '') || this.dadosUsuario.confirm_password === null || this.dadosUsuario.confirm_password.length <= 0 || !(this.dadosUsuario.confirm_password === this.dadosUsuario.password)){
                this.messageError = 'Senhas não coincidem';
                return false;
            }



            return true;
        },
    }
}

</script>