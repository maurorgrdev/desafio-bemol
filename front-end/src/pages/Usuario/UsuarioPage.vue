<template>
    <q-page>
        <q-dialog v-model="showDialogVisualizaEndereco" persistent>
            <q-card class="q-pa-md"
              style="width: 1000px; max-width: 80vw;"
            >
                <div class="title q-pa-sm">
                    <div class="text-h6">Visualização de Endereço</div>
                </div>
                <q-form class="q-gutter-md">
                    <div class="row">
                        <div class="q-pa-xs col-4">
                            <q-input disable outlined bottom-slots v-model="endereco_visualizado.cep" mask="#####-###" label="CEP *" counter maxlength="9" dense :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]">     
                        
                                <template v-slot:after>
                                  <q-btn disable color="primary" @click="validar_cep(endereco_visualizado.cep)" round dense flat icon="place"><q-tooltip> Buscar CEP </q-tooltip></q-btn>
                                </template>
                            </q-input>
                        </div>
                    </div>
                    <div class="row">
                        <div class="q-pa-xs col-8">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.logradouro" 
                                label="Endereço *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-xs col-4">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.tipo" 
                                label="Tipo *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                    </div>
                    <div class="row">
                        <div class="q-pa-xs col-10">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.bairro" 
                                label="Bairro *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-xs col-2">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.numero" 
                                label="Numero ou S/N*" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                    </div>
                    <div class="row">
                        <div class="q-pa-xs col-6">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.complemento" 
                                label="Complemento"
                            />
                        </div>
                        <div class="q-pa-xs col-4">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.localidade" 
                                label="Cidade *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                        <div class="q-pa-xs col-2">
                            <q-input disable
                                outlined 
                                dense
                                v-model="endereco_visualizado.uf" 
                                label="UF *" 
                                :rules="[ 
                                    val => val && val.length > 0 || 
                                    'Obrigatório'
                                ]"
                            />
                        </div>
                    </div>
                </q-form>
                <q-card-actions class="row text-primary">
                    <q-space />
                    <q-btn @click="showDialogVisualizaEndereco = false" outline style=" width: 150px; color: primary;" label="VOLTAR" />
                </q-card-actions>  
            </q-card>
        </q-dialog>

        <q-dialog v-model="showDialogDeleteEndereco" persistent>
            <q-card
              style="width: 550px; max-width: 80vw;"
            >
                <q-card-section>
                    <h6>O endereço selecionado será excluído. Confirmar ação?</h6>
                </q-card-section>
                <q-card-actions class="row text-blue-5">
                    <q-space />
                    <q-btn @click="showDialogDeleteEndereco = false" outline style=" width: 150px;" label="VOLTAR" />
                    <q-btn @click="confirmDeleteEndereco()" style=" width: 150px;" color="blue-5" label="Confirmar" />
                </q-card-actions>  
            </q-card>
        </q-dialog>

        <q-dialog v-model="showDialogDeleteUsuario" persistent>
            <q-card
              style="width: 550px; max-width: 80vw;"
            >
                <q-card-section>
                    <h6>O usuário - {{ usuario_delete.name }} -   será excluído. Confirmar ação?</h6>
                </q-card-section>
                <q-card-actions class="row text-blue-5">
                    <q-space />
                    <q-btn @click="showDialogDeleteUsuario = false" outline style=" width: 150px;" label="VOLTAR" />
                    <q-btn @click="confirmDeleteUsuario" style=" width: 150px;" color="blue-5" label="Confirmar" />
                </q-card-actions>  
            </q-card>
        </q-dialog>

        <q-dialog v-model="showDialogNovoEndereco" persistent>
            <q-card class="q-pa-md"
              style="width: 1000px; max-width: 80vw;"
            >
                <div class="title q-pa-sm">
                    <div class="text-h6">Novo Endereço</div>
                    <div class="text-subtitle2">Cadastro de endereço</div>
                </div>
                <q-form class="q-gutter-md">
                    <div class="row">
                        <div class="q-pa-xs col-4">
                            <q-input outlined bottom-slots v-model="novo_endereco.cep" mask="#####-###" label="CEP *" counter maxlength="9" dense :rules="[ 
                                val => val && val.length > 0 || 
                                'Obrigatório'
                            ]">     
                        
                                <template v-slot:after>
                                  <q-btn color="primary" @click="validar_cep(novo_endereco.cep)" round dense flat icon="place"><q-tooltip> Buscar CEP </q-tooltip></q-btn>
                                </template>
                            </q-input>
                        </div>
                    </div>
                    <div class="row">
                        <div class="q-pa-xs col-8">
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
                        <div class="q-pa-xs col-4">
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
                        <div class="q-pa-xs col-10">
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
                        <div class="q-pa-xs col-2">
                            <q-input 
                                outlined 
                                dense
                                v-model="novo_endereco.numero" 
                                label="Numero ou S/N*" 
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
                                v-model="novo_endereco.complemento" 
                                label="Complemento"
                            />
                        </div>
                        <div class="q-pa-xs col-4">
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
                        <div class="q-pa-xs col-2">
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
                <q-card-actions class="row text-blue-5">
                    <q-space />
                    <q-btn @click="showDialogNovoEndereco = false" outline style=" width: 150px;" label="VOLTAR" />
                    <q-btn @click="confirmSalvarNovoEndereco" style=" width: 150px;" color="blue-5" label="Salvar" />
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
                    table-header-class="bg-blue-5 text-white"
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
                                    <q-btn color="blue-5" class="q-mr-md" size="sm" icon="visibility" @click="openDialogVisualizaEndereco(props.row)"><q-tooltip> Visualizar Endereço </q-tooltip></q-btn>
                                    <q-btn color="red-5" class="q-mr-md" size="sm" icon="delete" @click="openDialogDeleteEndereco(props.row)"><q-tooltip> Deletar Endereço </q-tooltip></q-btn>
                                </q-td>
                            </q-tr>
                        </template>
                        <template v-slot:top>
                            <div class="title q-pa-xs">
                                <div class="text-h6">Endereços</div>
                                <div class="text-subtitle2">Lista dos endereços de {{user_enderecos.name}}</div>
                            </div>
                            <q-space />
                            <q-btn color="blue-5" label="NOVO ENDEREÇO"  @click="openDialogNovoEndereco()"/>
                        </template>
                    </q-table>
                </div>
                <q-card-actions class="row text-blue-5" style="padding-left: 15px; padding-right: 15px;">
                    <q-space />
                    <q-btn @click="showDialogListaEndereco = false" outline style=" width: 150px;" label="VOLTAR" />
                </q-card-actions>     
            </q-card>
        </q-dialog>

        <div class="q-pa-xl">
            <q-table
            flat
                :rows="usuarioStore.getUsuarios" 
                :columns="columns" 
                row-key="id" 
                table-header-class="bg-blue-5 text-white"
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
                            <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="add_location_alt" @click="openDialogListarEndereco(props.row)"><q-tooltip> Listar Endereços </q-tooltip></q-btn>
                            <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="mode_edit" @click="$router.push(`/usuarios/edita/${props.row.id}`)"><q-tooltip> Editar Usuário </q-tooltip></q-btn>
                            <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="visibility" @click="$router.push(`/usuarios/visualiza/${props.row.id}`)"><q-tooltip> Visualizar Usuário </q-tooltip></q-btn>
                            <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="delete" @click="openDialogDeleteUsuario(props.row)"><q-tooltip> Deletar Usuário </q-tooltip></q-btn>

                        </q-td>
                    </q-tr>
                </template>
                <template v-slot:top>
                    <div class="title q-py-xl">
                        <div class="text-h5">Usuários</div>
                        <div class="text-subtitle2">Usuários cadastrados no sistema</div>
                    </div>        
                    <q-space />
                    <q-btn color="blue-5" label="NOVO USUÁRIO"  @click="$router.push('/usuarios/novo')"/>
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
            showDialogDeleteEndereco: false,
            showDialogDeleteUsuario: false,
            showDialogVisualizaEndereco: false,

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

            endereco_delete: {},

            usuario_delete: {},

            messageError: '',

            endereco_visualizado: {},
        }   
    },

    async mounted(){
        await this.usuarioStore.loadUsuarios();
    },

    methods: {
        async confirmSalvarNovoEndereco(){
            if(await this.validar_cep(this.novo_endereco.cep) &&  await this.validarCamposEndereco(this.novo_endereco)){
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
            } else {
                alert(this.messageError)
            }
        },  

        validarCamposEndereco(endereco){
            if((endereco.cep === '') || endereco.cep === null || endereco.cep.length <= 0){
                this.messageError = 'Informe uma CEP válido';
                return false;
            }

            if((endereco.logradouro === '') || endereco.logradouro === null || endereco.logradouro.length <= 0){
                this.messageError = 'Informe um Endereço válido';
                return false;
            }

            if((endereco.tipo === '') || endereco.tipo === null || endereco.tipo.length <= 0){
                this.messageError = 'Informe um Tipo válido';
                return false;
            }

            if((endereco.bairro === '') || endereco.bairro === null || endereco.bairro.length <= 0){
                this.messageError = 'Informe um Bairro válido';
                return false;
            }

            if((endereco.numero === '') || endereco.numero === null || endereco.numero.length <= 0){
                this.messageError = 'Informe um Número válido';
                return false;
            }

            if((endereco.localidade === '') || endereco.localidade === null || endereco.localidade.length <= 0){
                this.messageError = 'Informe uma Cidade válida';
                return false;
            }

            if((endereco.uf === '') || endereco.uf === null || endereco.uf.length <= 0 || endereco.uf.length > 2){
                this.messageError = 'Informe um UF válido';
                return false;
            }

            return true
        },

        async validar_cep(cep){
            const response_cep = await this.addressStore.validarCEP(cep);

            console.log(response_cep)
            if(response_cep.status === 200){
                this.novo_endereco = {
                    ...this.novo_endereco,
                    logradouro: response_cep.data.logradouro,
                    bairro: response_cep.data.bairro,
                    uf: response_cep.data.uf,
                    localidade: response_cep.data.localidade,
                }

                return true
            } else {
                alert(response_cep.data.message)

                return false
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
        },

        openDialogDeleteEndereco(endereco){
            this.endereco_delete = {...endereco}

            this.showDialogDeleteEndereco = true;
        },

        async confirmDeleteEndereco(){
            const response = await this.addressStore.delete(this.endereco_delete.id);

            if(response.status == 201){
                await this.usuarioStore.loadUsuario(this.user_enderecos.id);

                this.user_enderecos = {
                    ...this.usuarioStore.getUsuario
                }

                this.showDialogDeleteEndereco = false
            } else {
                alert('Error ao excluir endereço')
            }
        },

        openDialogDeleteUsuario(usuario){
            this.usuario_delete = {...usuario}

            this.showDialogDeleteUsuario = true
        },

        async confirmDeleteUsuario(){
            const response = await this.usuarioStore.delete(this.usuario_delete.id);

            if(response.status == 201){
                await this.usuarioStore.loadUsuarios();

                this.showDialogDeleteUsuario = false
            } else {
                alert('Error ao excluir endereço')
            }
        },

        openDialogVisualizaEndereco(endereco){
            this.endereco_visualizado = {...endereco}

            this.showDialogVisualizaEndereco = true
        }
    }
}

</script>