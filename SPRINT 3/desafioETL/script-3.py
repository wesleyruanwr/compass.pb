def etapa_3():
    with open('C:/Users/Wesley Ruan/compass.pb/SPRINT 3/desafioETL/actors.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    actors_data = [line.strip().split(',') for line in lines]
    header = actors_data[0]
    data = actors_data[1:]

    average_per_movie_index = header.index('Average per Movie')
    sorted_data = sorted(data, key=lambda x: float(x[average_per_movie_index]), reverse=True)
    actor, average_per_movie = sorted_data[0][0], sorted_data[0][average_per_movie_index]

    with open('etapa-3.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(f'O ator/atriz com a maior média de receita de bilheteria bruta por filme é {actor} com uma média de {average_per_movie} milhões de dólares por filme.')

etapa_3()