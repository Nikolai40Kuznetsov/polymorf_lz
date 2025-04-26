import csv
from collections import defaultdict

def split_dataset(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) 
        data = list(reader)
    
    # Поиск данных банков
    banks_data = defaultdict(list)
    for row in data:
        terminal = row[5]  
        bank_name = terminal.split('-')[0]  # Поиск названия банка
        banks_data[bank_name].append(row)
    
    # Запись данных в отдельные файлы для каждого банка
    for bank_name, bank_rows in banks_data.items():
        output_file = f'{bank_name}.csv'
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(bank_rows)
        print(f'Данные банка записаны в файл {output_file}, всего {len(bank_rows)} записей')