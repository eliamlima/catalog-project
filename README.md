Este projeto corresponde a um catalogo de produtos similar a uma loja de esportes.

REQUISITOS:
- Maquina Virtual Vagrant instalada juntamente ao VirtualBox. Essas instruções são encontradas no curso Udacity.
- Verifice se na pasta já existem os arquivos "catalogwithusers.db" e "database_setup.pyc".
  - Se SIM: basta executar "python project.py" para rodar o servidor e abrirá a pagina com as categorias. Pois o banco ja estára populado.
  - Se NÃO: é necessário executar os arquivos database_setup.py e populate.py para popular o Banco de dados.

PAGINA INICIAL:
- Acessada pelo endereço localhost:8000 ou localhost:8000/catalog.
- Nela existe um header com o título da App e no canto superior direito o botão para Login.
- Na parte principal da pagina inicial encontram-se todas as categorias existentes.
- Ao clicar em alguma categoria, uma pagina se abre com os itens desta categoria.
- Ao clicar em algum item, uma outra pagina se abre com a descrição do produto.

ADIÇÃO DE ITENS:
- Só é possível com Login, que é efetuado apenas com API Google nesta versão do projeto.
- Ao estar logado, um link "Add Item" é mostrado ao lado das categorias. Clicando nele é possível adicionar um item na página que se abre.

EDIÇÃO E DELETE:
- Também só possível com usuário logado.
- Ao logar-se e clicar em um item específico, abaixo da descrição encontram-se links para edição e delete. Em cada um é aberta uma nova pagina para edição ou delete conforme o caso.

JSON API:
- Para acessar os dados em JSON acessar http://localhost:8000/catalog/JSON
