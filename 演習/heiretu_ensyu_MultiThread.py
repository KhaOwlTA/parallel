import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

#処理する内容
def syori(_n):
  s = 0
  for i in range(1,_n+1):
    s+=i
    time.sleep(0.1)
  return s

#シングルプロセス
namber_list = list(np.arange(1,20))
print("シングルプロセスで処理しています...")
start_1 = time.time()

single = []
for i in namber_list:
    single.append(syori(i))

end_1 = time.time()
time_1 = end_1 - start_1
print(time_1,"秒")



#マルチスレッド

#スレッド2
print("スレッド数2で処理しています...")
start_2 = time.time()

with ThreadPoolExecutor(2) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_2 = time.time()
time_2 = end_2 - start_2
print(time_2,"秒")  


#スレッド4
print("スレッド数4で処理しています...")
start_3 = time.time()

with ThreadPoolExecutor(4) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_3 = time.time()
time_3 = end_3 - start_3
print(time_3,"秒")  


#スレッド8
print("スレッド数8で処理しています...")
start_4 = time.time()

with ThreadPoolExecutor(8) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_4 = time.time()
time_4 = end_4 - start_4
print(time_4,"秒")  


#スレッド12
print("スレッド数12で処理しています...")
start_5 = time.time()

with ThreadPoolExecutor(12) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_5 = time.time()
time_5 = end_5 - start_5
print(time_5,"秒")  


#スレッド16
print("スレッド数16で処理しています...")
start_6 = time.time()

with ThreadPoolExecutor(16) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_6 = time.time()
time_6 = end_6 - start_6
print(time_6,"秒")  


#スレッド24
print("スレッド数24で処理しています...")
start_7 = time.time()

with ThreadPoolExecutor(24) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_7 = time.time()
time_7 = end_7 - start_7
print(time_7,"秒")  


#スレッド36
print("スレッド数36で処理しています...")
start_8 = time.time()

with ThreadPoolExecutor(36) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_8 = time.time()
time_8 = end_8 - start_8
print(time_8,"秒")  


#スレッド48
print("スレッド数48で処理しています...")
start_9 = time.time()

with ThreadPoolExecutor(48) as e:
    ret = e.map(syori, namber_list)
sms_multi = [r for r in ret]
  
end_9 = time.time()
time_9 = end_9 - start_9
print(time_9,"秒")  
