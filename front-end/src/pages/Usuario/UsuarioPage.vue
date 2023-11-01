<template>
    <q-page>
        <q-dialog v-model="showDialogNovoEndereco" persistent>
            <q-card
              style="width: 1000px; max-width: 80vw;"
            >
                <q-form class="q-gutter-md">
                    <div class="row">
                        <div class="q-pa-sm col-4">
                            <q-input outlined bottom-slots v-model="novo_endereco.cep" label="CEP *" counter maxlength="8" dense :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]">     
                        
                                <template v-slot:after>
                                  <q-btn @click="validar_cep()" round dense flat icon="place" />
                                </template>
                            </q-input>
                        </div>
                    </div>
                    <div class="row">
                        <div class="q-pa-sm col-8">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.logradouro" 
                                label="Endereço *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-sm col-4">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.tipo" 
                                label="Tipo *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                    </div>
                    <div class="row">
                        <div class="q-pa-sm col-10">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.bairro" 
                                label="Bairro *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-sm col-2">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.numero" 
                                label="Numero *" 
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
                                v-model="novo_endereco.complemento" 
                                label="Complemento *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-sm col-4">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.localidade" 
                                label="Cidade *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-sm col-2">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.uf" 
                                label="UF *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                    </div>
                </q-form>
                <q-card-actions class="row text-primary" style="padding-left: 15px; padding-right: 15px;">
                    <q-space />
                    <q-btn @click="showDialogNovoEndereco = false" outline style=" width: 150px; color: primary;" label="VOLTAR" />
                    <q-btn @click="clickSalvarNovoEndereco" style=" width: 150px;" color="primary" label="Salvar" />
                </q-card-actions>  
            </q-card>
        </q-dialog>

        <q-dialog v-model="showDialogListaEndereco" persistent>
            <q-card
              style="width: 1000px; max-width: 80vw;"
            >
                <div class="q-pa-md">
                    <q-table
                    flat bordered 
                    title="Endereços" 
                    :rows="user_enderecos.addresses" 
                    :columns="columnsEndereco" 
                    row-key="id" 
                    >
                        <template v-slot:body="props">
                            <q-tr :props="props">
                                <q-td key="tipo" :props="props">
                                    {{ props.row.tipo }}
                                </q-td>
                                <q-td key="cep" :props="props">
                                    {{ props.row.cep }}
                                </q-td>
                                <q-td key="logradouro" :props="props">
                                    {{ props.row.logradouro }}
                                </q-td>
                                <q-td key="actions" :props="props">
                                    <q-btn  icon="mode_edit" @click="teste()"></q-btn>
                                    <q-btn  icon="delete" @click="teste()"></q-btn>
                                </q-td>
                            </q-tr>
                        </template>
                        <template v-slot:top>
                            <q-space />
                            <q-btn color="primary" label="NOVO ENDEREÇO"  @click="openDialogNovoEndereco()"/>
                        </template>
                    </q-table>
                </div>
                <q-card-actions class="row text-primary" style="padding-left: 15px; padding-right: 15px;">
                    <q-space />
                    <q-btn @click="showDialogListaEndereco = false" outline style=" width: 150px; color: primary;" label="VOLTAR" />
                </q-card-actions>     
            </q-card>
        </q-dialog>

        <div class="q-pa-xl">
            <div class="title q-py-xl">
                <div class="text-h6">Usuários</div>
                <div class="text-subtitle2">Cadastrado de usuários</div>
            </div>

            <q-table
             bordered 
            :rows="usuarioStore.getUsuarios" 
            :columns="columns" 
            row-key="id" 
            >
                <template v-slot:body="props">
                    <q-tr :props="props">
                        <q-td key="id" :props="props">
                            {{ props.row.id }}
                        </q-td>
                        <q-td key="name" :props="props">
                            {{ props.row.name }}
                        </q-td>
                        <q-td key="email" :props="props">
                            {{ props.row.email }}
                        </q-td>
                        <q-td key="actions" :props="props">
                            <q-btn round icon="mode_edit" @click="$router.push(`/usuarios/edita/${props.row.id}`)"></q-btn>
                            <q-btn round icon="map" @click="openDialogListarEndereco(props.row)"></q-btn>
                        </q-td>
                    </q-tr>
                </template>
                <template v-slot:top>
                    <q-space />
                    <q-btn color="primary" label="NOVO USUÁRIO"  @click="$router.push('/usuarios/novo')"/>
                </template>
            </q-table>
        </div>
    </q-page>
</template>

<script>
import {useUsuarioStore} from 'src/stores/usuario'
import { useAddressStore } from 'src/stores/address'

export default {
    setup() {
        const usuarioStore = useUsuarioStore()
        const addressStore = useAddressStore()

        return {
            usuarioStore,
            addressStore
        }
    },

    data() {
        return {
            showDialogListaEndereco: false,
            showDialogNovoEndereco: false,

            user_enderecos: {},

            novo_endereco: {
                cep: '',
                logradouro: '',
                tipo: '',
                bairro: '',
                numero: '',
                complemento: '',
                localidade: '',
                uf: '',
            },

            columns: [
                {
                    name: 'id',
                    label: 'Código',
                    align: 'center',
                    field: 'Código',
                    sortable: true
                },
                { name: 'name', align: 'center', label: 'Nome', field: 'name', sortable: true },
                { name: 'email', align: 'center', label: 'Email', field: 'email', sortable: true },
                { name: 'actions', align: 'center', label: 'Ações'},
            ],

            columnsEndereco: [
                { name: 'tipo', align: 'center', label: 'Tipo endereço', field: 'tipo', sortable: true },
                { name: 'cep', align: 'center', label: 'CEP', field: 'cep', sortable: true },
                { name: 'logradouro', align: 'center', label: 'Dados endereço', field: 'logradouro', sortable: true },
                { name: 'actions', align: 'center', label: 'Ações'},
            ],
        }   
    },

    async mounted(){
        await this.usuarioStore.loadUsuarios();
    },

    methods: {
        async clickSalvarNovoEndereco(){
            const dados_endereco = {
                ...this.novo_endereco,
                user_id: this.user_enderecos.id,
            }

            const response_endereco = await this.addressStore.create(dados_endereco);

            if(response_endereco.status === 201){
                await this.usuarioStore.loadUsuario(this.user_enderecos.id);

                this.user_enderecos = {
                    ...this.usuarioStore.getUsuario
                }

                this.showDialogNovoEndereco = false
            } else {
                alert('nao deu pra adicionar')
            }
        },  

        async validar_cep(){
            const response_cep = await this.addressStore.validarCEP(this.novo_endereco.cep);

            if(response_cep){
                this.novo_endereco = {
                    ...this.novo_endereco,
                    logradouro: response_cep.logradouro,
                    bairro: response_cep.bairro,
                    uf: response_cep.uf,
                    localidade: response_cep.localidade,
                }
            } else {
                alert('cep inválido')
            }
        },  

        openDialogNovoEndereco(){
            this.novo_endereco = {
                cep: '',
                logradouro: '',
                tipo: '',
                bairro: '',
                numero: '',
                complemento: '',
                localidade: '',
                uf: '',
            },

            this.showDialogNovoEndereco = true
        },

        async openDialogListarEndereco(user){
            await this.usuarioStore.loadUsuario(user.id);

            this.user_enderecos = {
                ...this.usuarioStore.getUsuario
            }

            this.showDialogListaEndereco = true;
        }
    }
}

</script>