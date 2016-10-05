
#Resumo Git Book

##Primeiros passos
Tres estados de operação
- diretorio de trabalho - onde você realiza modificações nos arquivos
- área de seleção - quando você usa git add e seleciona os arquivos para commit
- repositorio git - quando você usa git commit e adiciona ao repositório

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

##Git Essecial

Iniciando repositórios git
- Local - $ git init
- Remoto - $ git clone git://github.com/schacon/grit.git
- Nomeando repositório - $ git clone git://github.com/schacon/grit.git mygrit

Adicionando arquivos para serem monitorados
- $ git add *.c
- $ git add README
- $ git commit -m 'initial project version'

Verificando alterações nos arquivos

![Ciclo de trabalho no git](https://git-scm.com/figures/18333fig0201-tn.png "Ciclo de trabalho no git")


