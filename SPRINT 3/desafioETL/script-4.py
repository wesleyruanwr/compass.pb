def etapa_4():
    with open('C:/Users/Wesley Ruan/compass.pb/SPRINT 3/desafioETL/actors.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    actors_data = [line.strip().split(',') for line in lines]
    header = actors_data[0]
    data = actors_data[1:]
    num1_movie_index = header.index('#1 Movie')

    movies_count = {}
    for row in data:
        movie = row[num1_movie_index]
        if movie != '':
            movies_count[movie] = movies_count.get(movie, 0) + 1
    sorted_movies = sorted(movies_count.items(), key=lambda x: x[1], reverse=True)

    with open('etapa-4.txt', 'w', encoding='utf-8') as output_file:
        for movie, count in sorted_movies:
            output_file.write(f'{movie} aparece {count} vez(es) no dataset.\n') 

etapa_4()