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


*FUNÇÕES AGREGADAS*
    -SERVEM PARA EXECULTAR OPERAÇÕES ARITIMETICAS NAS LINHAS DE UMA COLUNA

    *EXERCICIOS DA AULA*

    --exercicio 1 (contagem de todas as linhas de uma tabela)

    select count (*)
    from sales.funnel

    --exercicio 2 (conte quantos pagamentos foram registrados na tabela sales.funnel)

    select count(paid_date)
    from sales.funnel

    --exercicio 3 (conte todos os produtos distintos visitados em jan/21)

    select count (distinct product_id)
    from sales.funnel
    where visit_page_date between '20210101' and '20210131'

    --exercicio 4 (conte o valor minimo, maximo e medio dos produtos)

    select min(price), max(price), avg(price)
    from sales.products

    --exercicio 5 (informe o veiculo mais caro da tabela products)

    select max(price) from sales.products

    select *
    from sales.products				--isso aqui seria uma sub querie
    where price = (select max(price) from sales.products)


*GROUP BY*
    -AGRUPA REGISTROS SEMELHANTES DE UMA COLUNA

    *EXERCICIOS DA AULA*

    --exercicio 1 (conte a quatidade de clientes da tabela costumers por estado)

    select state, count (*)
    from sales.customers
    group by state
    order by count desc

    --exercicio 2 (conte a quantidade de clientes por estado e status profissional)

    select state, professional_status, count (*)
    from sales.customers
    group by state, professional_status
    order by state, count desc

*HAVING*
    -FILTRA LINHAS DE SELEÇÃO POR UMA COLUNA AGRUPADA

    *EXERCICIOS DA AULA*

    --EXERCICIO 1 calcule o numero de clientes por estado filtrando apeanas nos estados com mais de 100 clientes

    select 
	    state,
	    count(*)
    from sales.customers
    group by state
    having count(*) > 100


*SUBQUERY*
    -servem para consutar dados de outras consultas, e so podem retortar 1 valor no where e no select 
    
    -- exercicio subquery no *SELECT* 
    -- Na tabela sales.funnel crie uma coluna que informa o numero de visitas acumuladas que a loja recebeu ate o momento
    select
	    fun.visit_id,
	    fun.visit_page_date,
	    sto.store_name,
	    (	
		    select count(*)
		    from sales.funnel as fun2
		    where fun2.visit_page_date <= fun.visit_page_date
			    and fun2.store_id = fun.store_id
	    ) as visitas_acumuladas	
	
    from sales.funnel as fun
    left join sales.stores as sto
	    on fun.store_id = sto.store_id
    order by sto.store_name, fun.visit_page_date


    --exercicio 1- subquery no *WITH*
    -analise a recorrencia dos leads, calcule o numero de visitas e diga se foi a primeira visita ou nao

    with primeira_visita as (
	
	    select customer_id, min(visit_page_date) as visita_1
    	from sales.funnel
    	group by customer_id

    )

    select
    	fun.visit_page_date,
    	(fun.visit_page_date <> primeira_visita.visita_1) as lead_recorrente,
    	count(*)

    from sales.funnel as fun
    left join primeira_visita
    	on fun.customer_id = primeira_visita.customer_id
    group by fun.visit_page_date, lead_recorrente
    order by fun.visit_page_date desc, lead_recorrente


exercicio 2
    with preco_medio as(
    
    	select brand, avg(price) as preco_medio_da_marca
    	from sales.products
	    group by brand
    )

    select
	    fun.visit_id,
	    fun.visit_page_date,
	    pro.brand,
	    (pro.price * (1+fun.discount)) as preco_desconto,
	    preco_medio.preco_medio_da_marca,
	    ((prp.price * (1+fun.discount)) - preco_medio.preco_medio_da_marca) as preco_vs_media
    from sales.funnel as fun
    left join sales.products as pro
	    on fun.product_id = pro.product_id
    left join preco_medio
	    on pro.brand = pro.preco_medio.brand


*TRATAMENTO DE DADOS*
    -transformar dados de um tipo em outro

    tipos- -->  "::"  <-- Usando os dois pontos 2 vezes voce consegue dizer depois dele qual tipo de dado aquilo representa

    *EXEMPLO*

    select '2021-10-01'::date - '2021-02-25'::date
    
    -nesse exemplo, se não for dito que oq esta entre parenteses é uma data ira dar erro
        alem de data, pode tranformar em "numeric" ou "text"

    
    porém as vezes os "::" não funcionam por motivos desconhecidos, então
    nos temos que usar a função --> "CAST" <--
    
    select cast('2021-10-01' as date) - cast('2021-02-25' as date)

*CASE WHEN*
    -SELECIONA CASOS

    *EXERCICIOS*

    (DEFINA OS CLIENTES EM CLASSES DE VALOR DE SALARIO DE 0-5000, DE 5000-10000 E 10000-15000)      
    
    with faixa_de_renda as (
	    select
		income,
		case
			when income < 5000 then '0-5000'
			when income >= 5000 and income < 10000 then '5000-10000'
			when income >= 10000 and income < 15000 then '10000-15000'
			else '15000+'
			end as faixa_renda
	from sales.customers

    )

    select faixa_renda, count(*)
    from faixa_de_renda
    group by faixa_renda


*CRIAÇÃO DE FUNÇÃO*

    create function datediff (unidade varchar, data_inicial date, data_final date)
    returns integer 
    language sql

    as 
    $$

		    select
			    case
				    when unidade in ('d', 'day', 'days') then (data_final - data_inicial)
		    		when unidade in ('w', 'week', 'weeks') then (data_final - data_inicial)/7
		    		when unidade in ('m', 'month', 'months') then (data_final - data_inicial)/30
		    		when unidade in ('y', 'year', 'years') then (data_final - data_inicial)/365
		    		end as diferenca_data
    $$


*CRIAÇÃO DE TABELA*

    -CRIACAO DE UMA TABELA A PARTIR DE UMA QUERY

    select 
	    customer_id,
	    datediff('y', birth_date, current_date) as idade_cliente
	    into temp_tables.customers_age
    from sales.customers

    select *
    from temp_tables.customers_age