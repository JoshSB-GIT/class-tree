import os
import random
import string

class CsvTools():
    def generate_file_hash(self, file_name):
        name, extention = os.path.splitext(file_name)
        
        hash = ''.join(
            random.choices(string.ascii_letters + string.digits, k=30))
        
        new_file_name = f"{name}-{hash}{extention}"
        
        return new_file_name


# csv = CsvTools()
# file_name = 'archivo.txt'
# hash_value = csv.generate_file_hash(file_name)
# print(hash_value)