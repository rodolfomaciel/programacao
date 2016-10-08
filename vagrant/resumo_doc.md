#Resumo da Documentação Vagrant

##Passos Básicos em Vagrant

Iniciando uma máquina virtual
- $ vagrant init hashicorp/precise64
- $ vagrant up

Configurando projeto
- $ mkdir vagrant_getting_started
- $ cd vagrant_getting_started
- $ vagrant init

Instale uma box(imagem base de um sistema)
- $ vagrant box add hashicorp/precise64

Você pode encontrar diversas imagens de sistemas diferentes em https://atlas.hashicorp.com/boxes/search

Edite o arquivo Vagrantfile e adicione a box escolhida ou indique a url

    Vagrant.configure("2") do |config|
        config.vm.box = "hashicorp/precise64"
        config.vm.box_version = "1.1.0"
        config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    end

Inicie e acesse a sua máquina virtual com esses dois comandos
- $ vagrant up
- $ vagrant ssh

Para encerrar o acesso faça:
- $ logout ou CTRL+D

Você pode também encerrar a máquina virtual com
- $ vagrant destroy

Para eliminar o arquivo baixado da box faça:
- $ vagrant box remove
