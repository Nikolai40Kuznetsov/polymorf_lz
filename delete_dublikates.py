import csv

class Dataset:
    def __init__(self, data=None, header=None):
        self.data = data if data is not None else []
        self.header = header if header is not None else []
        self.duplicates_count = 0
    
    def __neg__(self):
        """Перегрузка унарного оператора - для удаления дубликатов"""
        unique_data = []
        seen = set()
        duplicates_count = 0
        
        for row in self.data:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
            else:
                duplicates_count += 1
        
        result = Dataset(unique_data, self.header)
        result.duplicates_count = duplicates_count
        return result
    
    @classmethod
    def from_csv(cls, filename):
        """Создание Dataset из CSV файла"""
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
        return cls(data, header)
    
    def to_csv(self, filename):
        """Сохранение Dataset в CSV файл"""
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
            writer.writerows(self.data)