Operações Básicas
- Todas as dependencias do app precisam de instalação local
- heroku login
- git clone
- cd caminho_da_pasta_clonada
- heroku create
- git push heroku master
- heroku ps:scale web=1 (caso seja app python) 
- heroku open
- heroku logs --tail (para ver o que ocorre no app)
- Procfile - arquivo que define os comandos no Heroku
- heroku ps:scale web=1 (para escalar sua aplicação aumente o numero depois de web)
- pip install -r requirements.txt (heroku exige o arquivo requirements.txt para sua app python)
- heroku pg:psql (para acessar o postgresql no heroku)

Ambientes de desenvolvimento
- Desenvolvimento
- Teste
- Produção


