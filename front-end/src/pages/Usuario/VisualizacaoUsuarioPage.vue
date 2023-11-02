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
                                  <q-btn disable color="primary" @click="validar_cep(endereco_visualizado.cep)" round dense flat icon="place" />
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
        
        <q-card-section>
            <q-form class="q-gutter-md">
                <div class="row">
                    <div class="q-pa-sm col-12">
                        <q-input 
                            disable
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
                            disable
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
                    <div class="q-pa-sm col-4">
                        <q-input disable dense outlined label="Data nascimento *" v-model="dadosUsuario.data_nascimento" mask="##/##/####">
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
                        <!-- <q-input dense outlined v-model="dadosUsuario.data_nascimento"  :rules="['date']">
                            <template v-slot:append>
                              <q-icon name="event" class="cursor-pointer">
                                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                                  <q-date mask="DD/MM/YYYY" v-model="dadosUsuario.data_nascimento" @input="() => $refs.qDateProxy.hide()" ></q-date>
                                </q-popup-proxy>
                              </q-icon>
                            </template>
                          </q-input> -->
                    </div>
                </div>
                <div class="row">
                    <div class="q-pa-sm col-6">
                        <q-input 
                            disable
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
                    <div class="q-pa-sm col-6">
                        <q-input 
                            disable
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
            </q-form>
            <div class="q-pa-md">
                <q-table
                flat bordered 
                title="Endereços" 
                :rows="dadosUsuario.addresses" 
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
                            </q-td>
                        </q-tr>
                    </template>
                    <template v-slot:top>
                        <div class="title q-pa-xs">
                            <div class="text-h6">Endereços</div>
                            <div class="text-subtitle2">Lista dos endereços de {{dadosUsuario.name}}</div>
                        </div>
                        <q-space />
                    </template>
                </q-table>
            </div>
        </q-card-section>

        <q-card-actions class="row text-blue-5" style="padding-left: 25px; padding-right: 25px;">
            <q-space />
            <q-btn @click="clickCancel" outline style=" width: 150px;" label="VOLTAR" />
          </q-card-actions>
    </q-page>
</template>

<script>
import { useUsuarioStore } from 'src/stores/usuario';

export default {
    props: ['usuario_id'],


    setup(){
        const usuarioStore = useUsuarioStore()

        return {
            usuarioStore,
        }
    },

    async mounted() {
        await this.usuarioStore.loadUsuario(this.usuario_id);

        this.dadosUsuario = {...this.usuarioStore.getUsuario}
    },

    data() {
        return {
            showDialogVisualizaEndereco: false,

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

            columnsEndereco: [
                { name: 'tipo', align: 'center', label: 'Tipo endereço', field: 'tipo', sortable: true },
                { name: 'cep', align: 'center', label: 'CEP', field: 'cep', sortable: true },
                { name: 'logradouro', align: 'center', label: 'Dados endereço', field: 'logradouro', sortable: true },
                { name: 'actions', align: 'center', label: 'Ações'},
            ],

            isPwdPrincipal: true,
            isPwdSecundario: true,

            endereco_visualizado: {},

            proxyDataNascimento: '',
        }
    },

    methods: {

        clickCancel(){
            this.$router.push('/usuarios')
        },

        openDialogVisualizaEndereco(endereco){
            this.endereco_visualizado = {...endereco}

            this.showDialogVisualizaEndereco = true
        }
    }
}

</script>