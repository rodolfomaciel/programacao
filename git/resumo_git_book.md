
#Resumo Git Book

##Primeiros passos
Tres estados de operação
- área de trabalho - onde você realiza modificações nos arquivos
- área de seleção - quando você usa git add e seleciona os arquivos para commit
- área do repositorio - quando você usa git commit e adiciona ao repositório

![Tres estados de operação](https://git-scm.com/book/en/v2/book/01-introduction/images/areas.png "Tres estados de trabalho no repositório")

##Instalação e Configuração
Instalaçao
- Fedora - $ sudo yum install git-all
- Ubuntu - $ sudo apt-get install git-all

Algumas configurações básicas
- Nome - $ git config --global user.name "John Doe"
- Email - $ git config --global user.email johndoe@example.com
- Editor - $ git config --global core.editor emacs
- Ferramenta diff - $ git config --global merge.tool vimdiff
- Listando configuração - $ git config --list

Obtendo ajuda
- $ git help <verb>
- $ git <verb> --help
- $ man git-<verb>

##Git Essencial

Iniciando repositórios git
- Local - $ git init
- Remoto - $ git clone git://github.com/schacon/grit.git
- Nomeando repositório - $ git clone git://github.com/schacon/grit.git mygrit

Adicionando arquivos para serem monitorados
- $ git add *.c
- $ git add README
- $ git commit -m 'initial project version'

![Ciclo de trabalho no git](https://git-scm.com/book/en/v2/book/02-git-basics/images/lifecycle.png "Ciclo de trabalho no git")

Monitorando arquivos
- Verificando status dos arquivos - $ git status, $ git status -s 
- Ignorando arquivos automaticamente - crie um arquivo .gitignore e adicione referencias aos arquivos que deseja ignorar
 - Exemplos: *.[oa], *~
- Verificando arquivos modificados e não selecionados - $ git diff
- Verificando arquivos modificados e selecionados - $ git diff --cached
- Enviando arquivos para o repositório - $ git commit -m "Story 182: Fix benchmarks for speed"
- Selecionando e enviando os arquivos ao repositório - $ git commit -a -m 'added new benchmarks'
- Removendo arquivos da seleção e do diretório - $ git rm grit.gemspec
 - Removendo somente da seleção - $ git rm --cached readme.txt
- Renomeando arquivos na área de seleção - $ git mv arquivo_origem arquivo_destino

Histórico de Commits
- Visualizando histórico - $ git log
- Visualizando as modificações e limitando a quantidade - $ git log -p -2
- Incluindo estatisticas - $ git log --stat
- Visualizando saidas em formatos diferentes - $ git log --pretty=oneline
- Limitando o período de visualização - $ git log --since=2.weeks
 - Outras opções:
  - -(n) 	Mostra somente os últimos n commits.
  - --since, --after 	Limita aos commits feitos depois da data especificada.
  - --until, --before 	Limita aos commits feitos antes da data especificada.
  - --author 	Somente mostra commits que o autor casa com a string especificada.
  - --committer 	Somente mostra os commits em que a entrada do commiter bate com a string especificada.
  
Alterando commits
- Modificando seu ultimo commit - $ git commit --amend
- Tirando arquivos da seleção - $ git reset HEAD nome_arquivo
- Reverter alterações para o último commit - $ git checkout -- nome_arquivo

Repositórios remotos
- Listando os repositórios remotos - $ git remote -v
- Adicionando remotos - $ git remote add pb git://github.com/paulboone/ticgit.git
- Obtendo arquivos atualizados -git fetch git://github.com/paulboone/ticgit.git
- Obtem arquivos atualizados e mescla com repositorio local  - $ git push origin master
- Inspeciona e mostra informações sobre o remoto - $ git remote show origin
- Renomeando remotos - $ git remote rename pb paul

Tagging
- Listando tags - $ git tag
- Especificando tags - $ git tag -l 'v1.4.2.*'
- Criando tag anotada - $ git tag -a v1.4 -m 'my version 1.4'
- Exibindo tag junto com commit - $ git show v1.4
- Criando tag assinada - $ git tag -s v1.5 -m 'my signed 1.5 tag'
- Criando tag leve - $ git tag v1.4-lw
- Verificando uma tag - $ git tag -v v1.4.2.1
- Criando tag num commit anterior - $ git tag -a v1.2 9fceb02
- Compartilhando tags no remoto
 - Compartilhando tag especifica - $ git push origin v1.5
 - Compartilhando todas as tag - $ git push origin --tags
 
Atalhos no git

Você pode criar atalhos no git sem precisar usar o comando completo:
- Criando atalho para checkout - $ git config --global alias.co checkout
- Criando atalho para branch - $ git config --global alias.br branch
- Criando atalho para commit - $ git config --global alias.ci commit
- Criando atalho para status -  $ git config --global alias.st status

##Ramificação no Git

Operações básicas com ramificações
- Criando um novo branch chamado testing - $ git branch testing
- Mudando para outro branch de trabalho - $ git checkout testing
- Criando e mudando para um novo branch - $ git checkout -b iss53

- Para fundir branchs faça - $ git branch iss53 e depois $ git checkout iss53
- Deletando branch - $ git branch -d iss53
- Listando branchs ativos - $ git branch , opções -v --merged --no-merged
- Deletando branch a força - git branch -D testing

Fluxo de trabalho com branchs
- Utilização de tres branchs
 - Master - para codigo estável
 - Develop - para código em desenvolvimento
 - Topic - para teste de alguma funcionalidade
 
Branchs remotos

- Listando os branches no remoto - $ git remote show [remote]
- Sincronizando os arquivos - $ git fetch origin
- Compartilhando seu projeto num branch chamado serverfix - $ git push origin serverfix
- Criando um upstream dum branch - $ git checkout --track origin/serverfix
- Fazendo sincronização e fusão com remoto - $ git pull
- Deletando um branch no servidor - $ git push origin --delete serverfix

