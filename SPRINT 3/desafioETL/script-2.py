def etapa_2():
    with open('C:/Users/Wesley Ruan/compass.pb/SPRINT 3/desafioETL/actors.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    actors_data = [line.strip().split(',') for line in lines]
    header = actors_data[0]
    data = actors_data[1:]
    gross_index = header.index('Gross')
    valid_gross_values = [float(row[gross_index]) for row in data if row[gross_index].replace('.', '', 1).isdigit()]
    total_gross = sum(valid_gross_values)
    average_gross = total_gross / len(valid_gross_values)

    with open('etapa-2.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(f'A média de receita de bilheteria bruta dos principais filmes é {average_gross:.2f} milhões de dólares.')


etapa_2()