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


**volumes** = forma de persistir dados sem depender de containers, todo dado criado por um container é salvo no próprio, quando o container é removido os dados são perdidos. Então os volumes são necessários para fazer beckups e gerenciar os dados

*tipos*
    *anonimo* = é criado pela flag *"-v"* porem com um nome aleatorio
    *nomeados*
    *bind mounts* = uma fomra de salvar os dados na nossa maquina sem o gerenciamento do docker


**Docker Swarm**

*nodes* = é uma isntancia (maquina) que participa da Swarm
*Manager node* = node que regencia os outros
*worker node* = nodes que trabalham em funcao do menager
*sevice* = Um conjunto de tasks que o manager manda para os workers
*taks* = comandos que são executados pelos nodes
