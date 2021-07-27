import time
import threading

#逐次処理

print("逐次処理の場合")

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



#threadを実装する場合
print("threadを実装する場合")

def gakuseki_2():
  for i in range(26):
    time.sleep(0.5)
    gakusekibanngou_sita = gakuseki_sita + i
    gakusekibanngou = gakusekibanngou_sita
    if (gakusekibanngou < 10):
        print("e19570",gakusekibanngou,"=")
    else:
        print("e1957",gakusekibanngou,"=")

name = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def gakusei_2():
  for i in range(26):
    time.sleep(0.51)
    gakusei_name = name[i]
    print(gakusei_name,"さん\n")

start_2 = time.time()
thread_1 = threading.Thread(target=gakuseki_2)
thread_2 = threading.Thread(target=gakusei_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end_2 = time.time()
time_2 = end_2 - start_2
print(time_2,"秒")

time＿sa = time_1 - time_2
print("threadを実装した結果、逐次処理かかった時間 - thread実装でかかった時間より、 ",time_1,"-",time_2,"=",time＿sa,"秒早くなった。")
