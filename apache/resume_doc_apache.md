#Resumo da Documentação do Apache

##Operações básicas

Usando o apachectl [ httpd-argument ]
- apachectl -k start
- apachectl -k stop
- apachectl -k restart
- apachectl status
- apachectl graceful (reinicia sem perder as conexões abertas)
- apachectl -k graceful-stop (para sem perder as conexões abertas)
- apachectl -t ou apachectl configtest (testa a configuração e retorna informações)
- apachectl startssl (inicia com suporte a ssl)
