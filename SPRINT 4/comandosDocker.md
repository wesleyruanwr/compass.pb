*run* = inicia um container

*start* = reiniciar um container

*stop* = para o container

*ps* = mostra a lista de containers ativos

*-d* = flag que faz o container rodar em background

*-p* = flag que dita a porta que o container vai usar

*--name* = flag que define um nome do container, se nao for usado recebe um nome aleatorio

*logs* = verificar o que esta acontecendo com os containers

*-rm* = remove o container da maquina
    se estiver rodando o container no momento, usar o *-f* para forcar a remocao

**imagem**

*from* = ter uma imagem base

*workdir* = diz o diretorio que a imagem vai trabalhar

*expose* = expoe a porta da aplicação

*copy* = copia arquivos para a imagem


**layer** = cada instrução do Docker é uma layer
        quando algo é atualizado apenas as layers depois da linha atualizada sao refeitas, o resto fica em cache deixando o bild mais rapidos


*pull* = baixar uma imagem para ser rodada localmente

*--help* = todas as opcoes disponiveis nos comandos