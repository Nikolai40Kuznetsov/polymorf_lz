import dividing_class as d_c
import delete_dublikates as d_d

if __name__ == "__main__": 
    input_filename = 'var6.csv'  # Имя исходного файла
    output_filename = 'var6_no_dublikates.csv'  # Имя итогового файла
    dataset = d_d.Dataset.from_csv(input_filename)
    unique_dataset = -dataset
    unique_dataset.to_csv(output_filename)
    print(f"Количество удалённых дубликатов: {unique_dataset.duplicates_count}")
    input_filename = 'var6_no_dublikates.csv' # имя нового исходного файла
    d_c.split_dataset(input_filename)
