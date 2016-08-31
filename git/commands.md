#Principais comandos Git

- git init - para iniciar um repositorio vazio
- git status - verificar a situação atual do repositorio
- git add * - adiciona todos os novo arquivos e diretorios no rastreamento do git
- git rm --cached <file> - retira arquivos do rastreamento
- git commit -m "Descricao das mudancas" - este comando adiciona os arquivos rastreados ao repostiorio
- git log - mostra tudo o que foi modificado no repositorio em ordem de tempo
- git remote add origin https://gthub.com/try-git/try_git.git - adiciona um repositorio no Github vazio
- git push -u origin master - esse comando envia todos arquivos do repositorio local para o repositorio no Github
- git diff HEAD - exibe as mudanças realizadas nos arquivos
- git diff --staged - mostra as diferencas rastreadas
- git reset octofamily/octodog.txt - retirar um arquivo do rastreamento
- git checkout -- octocat.txt - retorna um arquivo especifico a situação anterior
- git branch clean_up - cria uma ramificação do projeto para separar os rastreamentos no repositorio - clean_up é o nome da ramificacao
- git checkout clean_up - muda de ramificacao
- git rm '*.txt' - remove os arquivo do disco e também o rastreamento
- git checkout master - muda a ramificacao para o branch principal
- git merge clean_up - mescla o branch indicado com o atual
- git branch -d clean_up - deleta um ramo
