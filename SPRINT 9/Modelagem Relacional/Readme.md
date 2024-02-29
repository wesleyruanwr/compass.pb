**IMPORTANTE**

Eu estava fazendo o exercício e adicionando as informações na Udemy, porém sem querer eu cliquei em *Submit* ao inves *Save draf*, o que me fez enviar a resposta antes de estar pronta. Por isso a resposta da Udemy está diferente daqui, peço mil perdões e espero que entenda.


**PEQUENO RESUMO DO MEU PENSAMENTO**

Primeiro separei os atributos em entidades individuais para que contenha um valor único e indivisível, que é o que pede a 1 FN, valores repetidos como *idCliente*, *nomeCliente*, *cidadeCliente*, *estadoCliente*. Isso foi o que formou as 5 tabelas presentes.
Depois que as tabelas já estavam separadas foi mais fácil para eu garanti que todos os atributos de todas as tabelas estivessem totalmente ligados as suas respectivas chaves primarias.
E por ultimo, assim como pede a 3FN, análisei as tabelas e fiz com que um atributo não chave de uma tabela não dependa de outro atributo não chave **(dependência transitiva)**, como por exemplo o atributo *kmCarro* dependia da *idLocacao*.