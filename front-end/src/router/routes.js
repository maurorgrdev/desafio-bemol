
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') }
    ]
  },
  {
    path: '/usuarios',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Usuario/UsuarioPage.vue') },
      { path: 'novo', component: () => import('pages/Usuario/NovoUsuarioPage.vue') },
      { path: 'edita/:usuario_id', component: () => import('pages/Usuario/EdicaoUsuarioPage.vue'), props: true},
      { path: 'visualiza/:usuario_id', component: () => import('pages/Usuario/VisualizacaoUsuarioPage.vue'), props: true},
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
