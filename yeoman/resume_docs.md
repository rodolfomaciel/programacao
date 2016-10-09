#Resumo da Documentação Yeoman

Yeoman é um sistema scaffolding para construção rápida de qualquer tipo de aplicação web, em qualquer linguagem de programação.

É um conjunto de três softwares que juntos podem construir com rapidez uma aplicação. Exemplo: Yeoman, Gulpe NPM.

##Primeiros passos
Para instalar você deve usar o gerenciador de pacotes npm com o seguinte comando:
- $ npm install -g yo
  
Além disso, você deve usar um gerador como mostra o exemplo abaixo:
- $ npm install -g generator-webapp

O gerador fornece rapidamente a base para você iniciar seu projeto.

Inicie um novo projeto com o seguinte comando:
- $ yo webapp

Para obter ajuda sobre a configuração do projeto use:
- $ yo webapp --help

Se quiser ir direto para o site do gerador para obter mais informações use:
- $ npm home generator-webapp

Geradores complexos podem usar subgeradores para adicionar outros recursos a aplicação. Veja o comando abaixo:
- $ yo angular:controller MyNewController

No exemplo acima vimos como adicionar um novo controller numa aplicação angular.

Outros comandos úteis:
- $ yo --help Acesse a tela de ajuda completo
- $ yo --generators Listar todos os geradores instalados
- $ yo --version Obter a versão
