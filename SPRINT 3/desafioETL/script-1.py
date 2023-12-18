
def etapa_1():
    with open('C:/Users/Wesley Ruan/compass.pb/SPRINT 3/desafioETL/actors.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    actors_data = [line.strip().split(',') for line in lines]
    header = actors_data[0]
    data = actors_data[1:]
    num_movies_index = header.index('Number of Movies')
    data = [(row[0], float(row[num_movies_index].strip())) for row in data]
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

    actor, num_movies = sorted_data[0]

    with open('etapa-1.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(f'O ator/atriz com maior número de filmes é {actor} com {num_movies} filmes.')

etapa_1()
