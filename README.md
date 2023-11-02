<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Desafio Bemol - Street</h3>


---


## 📝 Índice

- [Sobre Started](#about)
- [Getting Started](#getting_started)
- [Authors](#authors)

## 🧐 Sobre <a name = "about"></a>

Projeto desenvolvido para o desafio Bemol, consiste em desenvolver e implementar a feature de Cadastro de Usuários, software Web, com acesso a consulta de CEP de uma API externa. O sistema contará com as seguintes camada: Interface (front-end), Regras de negócio (back-end) e Banco de Dados.

- ## 🏁 Getting Started <a name = "getting_started"></a>

Instruções para ter uma cópia do repositório.

### Pré-requisitos

-   **Python - Supported Versions:** >= 3.10
-   **Database:** MySQL
-   **Run-time environment:**: Flask, npm & Quasar Framework

### Instalação

- Clone

O repositório onde se encontra o código fonte da aplicação está na branch **master**. Logo:

```bash
$ git clone https://github.com/maurorgrdev/desafio-bemol.git
$ cd desafio-bemol
$ git checkout master
```

-   **Back-end**

Estas ações devem ser realizadas dentro da pasta /back-end.

- Configuração

Acesse a venv disponível:

```bash
$ source venv/bin/activate
```

Uma lista completa dos requisitos para execução dessa aplicação está disponível no arquivo
**requirements.txt**

Para instalá-los basta utilizar o **pip**:

```bash
$ pip install r- requirements.txt
```
É recomendado que seja feito esse processo, mesmo que seja apenas para verificação de pacotes.

- Database

Acesse a o diretório /src/server e abra o arquivo **instancy.py**. 
Na linha 16 altere os parametros **root** para suas credenciais de acesso (usuário:senha) do banco de dados:

Altere o seguinte atributo:

```bash
self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/street'
```

Caso tenha interesse, existe um script de criação da base de dados em infrastructure/database/create_db.py, basta editar as linhas 9 e 10 
colocando seu usuário e senha do banco de dados e executar:

```bash
$ python3 src/infrastructure/database/create_db.py
```

Caso não deseje ou não consiga executar esse script, será necessário criar a base de dados manualmente por meio do seu MySQL.

- Server

Para executar o server da aplicação basta estar na raiz do diretório /back-end, com a (venv) ligada e executar:

```bash
$ python3 src/app.py
```

O servidor deverá abrir em modo DEV. Esse servidor disponibiliza os endpoints para testes por meio do Swagger 
que pode ser acessado em **localhost:8000/api/doc** no seu navegador.

-   **Front-end**

Estas ações devem ser realizadas dentro da pasta /fron-end.

- Configuração

Instale todas as depedências:

```bash
$ npm install
```

- Iniciar app em modo de desenvolvimento

```bash
$ quasar dev
```

A Lista de Tarefas deverá aparecer no seu navegador.

---
---

## Diagrama de notacao C4 MODEL <a name = "diagrama"></a>

#### Modelo Diagrama Visualização da Arquitetura C4:

![](https://github.com/maurorgrdev/desafio-bemol/blob/master/documentação/Visualização%20da%20arquitetura.drawio.png)
_Imagem 01 - Diagrama Visualização da Arquitetura_


#### Modelo Diagrama Design da Solução:

![](https://github.com/maurorgrdev/desafio-bemol/blob/master/documentação/Design%20de%20solucao.drawio.png)
_Imagem 02 - Diagrama Design da Solução_

--- 
---

## Layout da Aplicação**

![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/01%20-%20Listagem%20de%20Usuarios.png)
_Imagem 03 - Listagem de Usuários_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/02%20-%20Cadastro%20de%20Usuario.png)
_Imagem 04 - Cadastro de Usuário_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/03%20-%20Edicao%20de%20Usuario.png)
_Imagem 05 - Edição de Usuário_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/04%20-%20Exclusao%20de%20Usuario.png)
_Imagem 06 - Exclusão de Usuário_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/05%20-Listagem%20de%20Endereco.png)
_Imagem 07 - Listagem de Endereços_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/06%20-%20Novo%20Endereco.png)
_Imagem 08 - Cadastro de Endereço_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/07%20-%20Visualizacao%20de%20Endereco.png)
_Imagem 09 - Visualização de Endereço_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/08%20-%20Excluir%20Endereco.png)
_Imagem 10 - Exclusão de Endereço_


![](https://github.com/maurorgrdev/desafio-bemol/blob/master/imagens/09%20-%20Visualizacao%20de%20Usuario.png)
_Imagem 11 - Visualização de Usuario


## ✍️ Authors <a name = "authors"></a>

- [@maurorgrdev](https://github.com/maurorgrdev) - Developer - mauroroger2020@gmail.com
