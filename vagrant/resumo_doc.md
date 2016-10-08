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

Edite o arquivo Vagrantfile e adicione a box escolhida

'''javascript
Vagrant.configure("2") do |config|
    config.vm.box = "hashicorp/precise64"
end
'''

