def etapa_5():
    with open('C:/Users/Wesley Ruan/compass.pb/SPRINT 3/desafioETL/actors.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    actors_data = [line.strip().split(',') for line in lines]
    header = actors_data[0]
    data = actors_data[1:]
    total_gross_index = header.index('Total Gross')
    actor_index = header.index('Actor')
    valid_total_gross_values = []
    for row in data:
        total_gross = row[total_gross_index].replace(',', '').replace('$', '')
        total_gross = ''.join(char for char in total_gross if char.isdigit() or char == '.')
        if total_gross.replace('.', '', 1).isdigit():
            valid_total_gross_values.append((row[actor_index], float(total_gross)))
    sorted_data = sorted(valid_total_gross_values, key=lambda x: x[1], reverse=True)

    with open('etapa-5.txt', 'w', encoding='utf-8') as output_file:
        for row in sorted_data:
            actor, total_gross = row[0], float(row[1])
            output_file.write(f'{actor} - {total_gross:.2f} milhões de dólares.\n')

etapa_5()