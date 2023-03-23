from random import randint
import time
start_time = time.time() # 측정 시작

array = []

for k in range(10000):
    array.append(randint(1, 100))

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑


end_time = time.time() #측정 종료

print("time :", end_time - start_time)