import time, string
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import function as f

#全て素数であることがわかっている数リスト(調べた)
NUMBER1 = [9007199254740881,7365373222715531,583964556541679,92709568269121,112272535095293]
#全て素数でないことがわかっている数リスト(１の位が偶数だから)
NUMBER2 = [4567876543234562,13456767689342,2345689302394586794,12039485780398342,12304596875940348578]
#上二つの混合リスト
NUMBER3 = [12039485780398342,9007199254740881,4567876543234562,7365373222715531,13456767689342,583964556541679,2345689302394586794,92709568269121,112272535095293,12304596875940348578]

def func_1(numbers):
    start = time.time() ## 処理開始時間
    ##============計算処理==============
    for number, result in zip(numbers, map(f.is_prime, numbers)):
        print(f"{number} は素数ですか？: {result}")
    ##=================================
    end = time.time()  ## 処理終了時間
    print(f"実行時間:{end - start}")
    print("==============================")

print("シングルプロセスでの素数判断処理")
func_1(NUMBER1)
func_1(NUMBER2)
func_1(NUMBER3)

def func_2(numbers):
    start = time.time() ## 処理開始時間
    ##============計算処理==============
    with ProcessPoolExecutor(max_workers=3) as e:
        for number, result in zip(numbers, e.map(f.is_prime, numbers)):
            print(f"{number} は素数ですか？: {result}")
    ##=================================
    end = time.time()  ## 処理終了時間
    print(f"実行時間:{end - start}")
    print("==============================")

print("マルチプロセスでの素数判断処理")
func_2(NUMBER1)
func_2(NUMBER2)
func_2(NUMBER3)

print("シングルスレッドでの総和計算")

start = time.time() ## 処理開始時間
##============計算処理==============
number = 20
ret = map(f.my_sum, range(1, number + 1))
result = [r for r in ret]
print(f"{number}までの総和: {result}")
##=================================
end = time.time()  ## 処理終了時間
print(f"実行時間:{end - start}")

print("マルチスレッドでの総和計算")

for i in [2,4,8,12,16,24,36,48,96]:
    print(f"スレッド数{i}で処理しています...")
        
    start = time.time() ## 処理開始時間
    ##============計算処理==============
    number = 20
    with ThreadPoolExecutor(max_workers=i) as e:
        ret = e.map(f.my_sum, range(1, number + 1))
    result = [r for r in ret]
    print(f"{number}までの総和: {result}")
    ##=================================
    end = time.time()  ## 処理終了時間
    print(f"実行時間:{end - start}")
    print("==============================")

print("逐次処理")

start = time.time() ## 処理開始時間
##============計算処理==============
names = list(string.ascii_uppercase)
results = []
for name, number in zip(names, range(1, len(names) + 1)):
    time.sleep(0.5)
    results.append(f.studentID(name, number))
for i in results:
    print(i)
##=================================
end = time.time()  ## 処理終了時間
print(f"実行時間:{end - start}")

print("並列処理")

start = time.time() ## 処理開始時間
##============計算処理==============
names = list(string.ascii_uppercase)
results = []
with ThreadPoolExecutor(3) as e:
    for name, number in zip(names, range(1, len(names) + 1)):
        time.sleep(0.5)
        results.append(e.submit(f.studentID, name, number))
for i in results:
    print(i.result())
##=================================
end = time.time()  ## 処理終了時間
print(f"実行時間:{end - start}")
