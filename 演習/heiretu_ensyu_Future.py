from concurrent.futures import ThreadPoolExecutor
import time


#逐次処理
print("逐次処理の場合の処理速度")

gakuseki_sita = 0
name = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def gakuseki_1():
  for i in range(26):
    time.sleep(0.5)
    gakusekibanngou_sita = gakuseki_sita + i
    gakusekibanngou = gakusekibanngou_sita

    time.sleep(0.51)
    gakusei_name = name[i]

    if (gakusekibanngou < 10):
      print("e19570",gakusekibanngou,"=",gakusei_name,"さん\n") 
    else:
      print("e1957",gakusekibanngou,"=",gakusei_name,"さん\n")      


start_1 = time.time()
gakuseki_1()
end_1 = time.time()
time_1 = end_1 - start_1
print(time_1,"秒\n")



#ThreadPoolExecutorの実装(戻り値もらえる)
print("ThreadPoolExecutorを実装した場合の処理速度")

gakuseki_sita = 0
names =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
executor = ThreadPoolExecutor(max_workers=2)
futures = []

def gakuseki_2(name, gakusekibanngou):
  time.sleep(0.51)

  if (gakusekibanngou < 10):
    gakuseki_gakusei = "e19570" + str(gakusekibanngou) + "=" + name + "さん"
    return gakuseki_gakusei
  else:
    gakuseki_gakusei = "e1957" + str(gakusekibanngou) + "=" + name + "さん" 
    return gakuseki_gakusei

start_2 = time.time()
for i in range(26):
  time.sleep(0.5)
  gakusekibanngou_sita = gakuseki_sita + i
  gakusekibanngou = gakusekibanngou_sita
  
  future = executor.submit(gakuseki_2, names[i], gakusekibanngou)
  futures.append(future) 

for future in futures:
  print(future.result())
end_2 = time.time() 
time_2 = end_2 - start_2
print(time_2,"秒\n")
executor.shutdown()

time＿sa = time_1 - time_2
print("ThreadPoolExecutorを実装した結果、逐次処理かかった時間 - thread実装でかかった時間より、 ",time_1,"-",time_2,"=",time＿sa,"秒早くなった。")



