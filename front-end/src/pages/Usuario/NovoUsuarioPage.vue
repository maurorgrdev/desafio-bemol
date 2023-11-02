<template>
    <q-page>
        <q-card-section>
            <q-form class="q-gutter-md">
                <div class="title q-pa-md">
                    <div class="text-h6">Cadastro de Usuário</div>
                    <div class="text-subtitle2">Cadastrando novo usuário no sistema</div>
                </div> 
                <div class="row">
                    <div class="q-pa-xs col-12">
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
                    <div class="q-pa-xs col-4">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.cpf" 
                            label="CPF *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                            mask="###.###.###-##"
                        />
                    </div>
                    <div class="q-pa-xs col-4">
                        <q-input dense outlined label="Data nascimento *" v-model="dadosUsuario.data_nascimento" mask="##/##/####">
                            <template v-slot:append>
                                <q-icon name="event" class="cursor-pointer">
                                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                                    <q-date v-model="dadosUsuario.data_nascimento" mask="DD/MM/YYYY">
                                    <div class="row items-center justify-end">
                                        <q-btn v-close-popup label="Fechar" color="primary" flat />
                                    </div>
                                    </q-date>
                                </q-popup-proxy>
                                </q-icon>
                            </template>
                        </q-input>      
                    </div>
                </div>
                <div class="row">
                    <div class="q-pa-xs col-6">
                        <q-input 
                            outlined 
                            dense
                            type="email"
                            v-model="dadosUsuario.email" 
                            label="Email *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                        />
                    </div>
                    <div class="q-pa-xs col-6">
                        <q-input 
                            outlined 
                            dense
                            type="email"
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
                    <div class="q-pa-xs col-6">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.password" 
                            label="Senha de acesso*" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                            :type="isPwdPrincipal ? 'password' : 'text'"
                        >
                            <template v-slot:append>
                                <q-icon
                                :name="isPwdPrincipal ? 'visibility_off' : 'visibility'"
                                class="cursor-pointer"
                                @click="isPwdPrincipal = !isPwdPrincipal"
                                />
                            </template>
                        </q-input>

                    </div>
                    <div class="q-pa-xs col-6">
                        <q-input 
                            outlined 
                            dense
                            v-model="dadosUsuario.confirm_password" 
                            label="Confirme sua senha *" 
                            :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]"
                            :type="isPwdSecundario ? 'password' : 'text'"
                        >
                            <template v-slot:append>
                                <q-icon
                                :name="isPwdSecundario ? 'visibility_off' : 'visibility'"
                                class="cursor-pointer"
                                @click="isPwdSecundario = !isPwdSecundario"
                                />
                            </template>
                        </q-input>
                    </div>
                </div>
            </q-form>
        </q-card-section>

        <q-card-actions class="row text-blue-5" style="padding-left: 25px; padding-right: 25px;">
            <q-space />
            <q-btn @click="clickCancel" outline style=" width: 150px;" label="Cancelar" />
            <q-btn @click="clickSubmit" style=" width: 150px;" color="blue-5" label="Salvar" />
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

            isPwdPrincipal: true,
            isPwdSecundario: true,

            proxyDataNascimento: '',
        }
    },

    methods: {

        clickCancel(){
            this.$router.push('/usuarios')
        },

        async clickSubmit(){
            if(await this.validarFormulario_NovoUsuario()){
                let response = await this.usuarioStore.create(this.dadosUsuario)

                if(response.status === 201){
                    this.$router.push('/usuarios')
                } else {
                    alert(response.data.message)
                }
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