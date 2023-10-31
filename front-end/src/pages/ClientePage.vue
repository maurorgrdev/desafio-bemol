<template>
    <q-page>
        <h1>OI</h1>
    </q-page>
</template>

<script>
import {useClienteStore} from 'src/stores/cliente'

export default {
    setup() {
        const clienteStore = useClienteStore()

        return {
            clienteStore
        }
    },

    data() {
        return {

        }   
    },

    async mounted(){
        await this.clienteStore.loadClientes();

        // console.log(this.clienteStore.getClientes);
    },

    methods: {

    }
}

</script>