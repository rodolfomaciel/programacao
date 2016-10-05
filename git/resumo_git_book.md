
#Resumo Git Book

##Primeiros passos
Tres estados de operação
- área de trabalho - onde você realiza modificações nos arquivos
- área de seleção - quando você usa git add e seleciona os arquivos para commit
- área do repositorio git - quando você usa git commit e adiciona ao repositório

![Tres estados de operação](https://git-scm.com/figures/18333fig0106-tn.png "Tres estados de trabalho no repositório")

##Instalação e Configuração
Instalaçao
- Fedora - yum install git-core
- Ubuntu - apt-get install git

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

![Ciclo de trabalho no git](https://git-scm.com/figures/18333fig0201-tn.png "Ciclo de trabalho no git")

Monitorando arquivos
- Verificando status dos arquivos - $ git status
- Ignorando arquivos automaticamente - crie um arquivo .gitignore e adicione referencias aos arquivos que deseja ignorar
 - Exemplos: *.[oa], *~
- Verificando arquivos modificados e não selecionados - $ git diff
- Verificando arquivos modificados e selecionados - $ git diff --cached
- Enviando arquivos para o repositório - $ git commit -m "Story 182: Fix benchmarks for speed"
- Selecionando e enviando os arquivos ao repositório - $ git commit -a -m 'added new benchmarks'
- Tirando arquivos da seleção - $ git reset HEAD <file>...
- Removendo arquivos da seleção e do diretório - $ git rm grit.gemspec
 - Removendo somente da seleção - $ git rm --cached readme.txt
- Renomeando arquivos na área de seleção - $ git mv arquivo_origem arquivo_destino




