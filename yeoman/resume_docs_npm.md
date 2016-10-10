#Resumo Documentação NPM

Operações básicas
- Instalação - apt-get install nodejs-legacy
- Atualização npm - npm install npm@latest -g
- Corrigir erros -  npm config get prefix && sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
