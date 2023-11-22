**COMANDOS**

*SELECT*
    -SELECIONA COLUNAS DE TABELAS (COMANDO MAIS UTILIZADO)
    "SELECT COLUNA_1, COLUNA_2, COLUNA_3
     FROM SCHEMA_1.TABELA_1"

    *EXERCICIOS DA AULA*
    -- exemplo 1 (buscando email)

    select email
    from sales.customers

    -- exemplo 2 (buscando email e nome)

    select email, first_name, last_name
    from sales.customers

    -- exemplo 3 (selecionando todas as colunas da tabela)

    select * 
    from sales.customers

*DISTINCT*
    -REMOVE LINHAS DUPLICADAS E MOSTRA APENAS AS LINHAS DISTINTAS

    *EXERCICIOS DA AULA*
    --Exercicio 1(selecione todas as marcas de carro)

    select brand
    from sales.products

    --exercicio 2(fazer a mesma selecao pegando apenas as marcas de carro distintas)

    select distinct brand
    from sales.products

    --exercicio 3(Selecao de mais de uma coluna usando o distinct)

    select distinct brand, model_year
    from sales.products					-- vai achar todas as COMBINACOES distintas das duas colunas


*WHERE*
    -FILTRAR AS LINHAS DA TABELA DE ACORDO COM ALGUMA CONDICAO

    *EXERCICIOS DA AULA*

    --exercicio 1 (listar todos os emails de clientes de santa catarina)
    select email
    from sales.customers
    where state = 'SC'

    --exercicio 2 (listar todos os emails de clientes de santa catarina e mato grosso do sul)
    select email, state
    from sales.customers
    where state = 'SC' or state = 'MS'


    --exercicio 2 (listar todos os emails de clientes de santa catarina e mato grosso do sul com mais de 30 anos)
    select email, state
    from sales.customers
    where (state = 'SC' or state = 'MS') and birth_date > '1993-11-21'

*ORDER BY*
    -ORDENA SELECAO DE ACORDO COM A REGUA DEFINIDA

    *EXERCICIOS DA AULA*

    --exercicio 1 (listar os produtor pelo preco com ordem crescente)

    select *
    from sales.products
    order by price --se quisesse o decrecente era so colocar 'desc' depois de 'price'

    --exercicio2(listar os estados distintos na ordem crescente)
    select distinct state
    from sales.customers
    order by state		-- ordenacao de texto se baseia na ordem alfabetica

*LIMIT*
    -LIMITA O NUMERO DE LINHAS QUE APARECE NA CONSULTA

     *EXERCICIOS DA AULA*
    --exemplo 1(10 primeiras linhas da tabela funnel)

    select * 
    from sales.funnel
    limit 10

    --exemplo 2(listar os 10 produtos masi caros da tabela products)

    select * 
    from sales.products
    order by price desc
    limit 10

*OPERADORES ARITIMETICOS*
    -SERVEM PARA EXECULTAR OPERAÇÕES, MUITO USADO PARA CRIAR COLUNAS CALCULADAS

    *EXERCICIOS DA AULA*
    --exercicio 1 (criacao de uma coluna calculada, contendo o contendo a idade do cliente da tabela sales.customers)

    select * 
    from sales.customers
    limit 10

    select
	    email,
	    birth_date,
	    (current_date - birth_date) / 365  as "idade do cliente" --ou idade_do_cliente para nao usar aspas
	
	    --"current_date" retorna a data atual

    from sales.customers 


    --exercicio 2 utilização da coluna calculada nas queries, listar os 10 clientes mais novos da tabela customers

    select
	    email,
	    birth_date,
	    (current_date - birth_date) / 365  as "idade do cliente"
    from sales.customers
    order by "idade do cliente"


    --exercicio 3 criacao de coluna calculada com strings crie a coluna "nome_completo" contendo o nome completo do cliente

    select 
	    first_name || ' ' || last_name as "nome completo" --o simbolo de duas barras retas "||" concatena strings e as aspas no meio e para dar espaço
    from sales.customers
    order by "nome completo"


*OPERADORES DE COMPARAÇÃO*
    -COMPARAM DOIS VALORES RETORNANDO TRUE OU FALSE, BASTANTE USADO EM CONJUNTO COM A FUNÇÃO WHERE PARA FILTRAR LINHAS DE UMA SELEÇÃO

    *EXERCICIOS DA AULA*
    --exercicio 1 uso de operadores como flag, crie uma coluna que retorne true sempre que um cliente for um profissional CLT

    select 
	    customer_id,
	    first_name,
	    (professional_status = 'CLT') as "status profissional"
    from sales.customers

*OPERADORES LOGICOS*
    -utilizados para unir uma exmpressao simples em uma composta

    *exercicios da aula*

    --exrcicio 1 uso do comand BETWEEN, selecione veiculos entre 100k e 200k

    select *
    from sales.products
    where price >= 100000 and <= 200000

    -- com o BETWEEN FICA:

    --exercicio 2 selecionar produtos que nao estejam entre 100k e 200k

    select *
    from sales.products
    where price between 100000 and 200000

    -- pode ser usado o " NOT BETWEEN " para selecionar tudo que nao esteja entre 100k e 200k

    --exercicio 3 comando "IN" selecione os produtos da marca honda toyota e renault

    select *
    from sales.products
    where brand in (HONDA, TOYOTA, RENAULT)


    --exercicio 4 comando "LIKE" selecione os primeiros nomes distintos da tabela que começam com a inicial "ANA"

    select *
    from sales.customers
    where first_name like 'ANA%'
					    --a "%" indica pro comando LIKE que depois de ANA pode ter qualquer outro resto de nome
					    --se quiser ignorar se as letras sao maiusculas ou minusculas é so usar o "ILIKE"
