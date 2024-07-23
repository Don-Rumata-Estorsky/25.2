"""
функция создаёт 100000 файлов с задеркой 1 секунда и записывает 
в него случайное число после замер времени всего процесса
""" 
import time
import random

def create_file_with_random_number(filename):
  
  random_number = random.randint(1, 100)  
  with open(filename, 'w') as file:
    file.write(str(random_number)) 
  time.sleep(1)

start_time = time.time() 
for i in range(4): # 1000 оченнь много
  create_file_with_random_number(f"file_{i}.txt")  
end_time = time.time()  

total_time = end_time - start_time
print(f"весь процесс занял: {total_time} секунд")
