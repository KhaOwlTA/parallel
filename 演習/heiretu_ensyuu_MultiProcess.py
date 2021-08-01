import math
import time
import concurrent.futures


#全て素数であることがわかっている数リスト(調べた)
#NUMBER = [9007199254740881,7365373222715531,583964556541679,92709568269121,112272535095293]

#全て素数でないことがわかっている数リスト(１の位が偶数だから)
#NUMBER = [4567876543234562,13456767689342,2345689302394586794,12039485780398342,12304596875940348578]

#上二つの混合リスト
NUMBER = [12039485780398342,9007199254740881,4567876543234562,7365373222715531,13456767689342,583964556541679,2345689302394586794,92709568269121,112272535095293,12304596875940348578]

#シングルプロセス

def What_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  sqrt_n = int(math.floor(math.sqrt(n)))
  for i in range(3, sqrt_n + 1, 2):
    if n % i == 0:
        return False
  return True

def main():
  start_1 = time.time()
  for number, prime in zip(NUMBER, map(What_prime, NUMBER)):
    print(f'{number} は素数ですか？: {prime}')
  end_1 = time.time()
  time_1 = end_1 - start_1
  print (f'全ての数の判断にかかった時間は:{time_1}秒です。')

if __name__ == '__main__':
  print("シングルプロセスでの素数判断処理")
  main()
  print("\n")



# #マルチプロセス
def what_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  sqrt_n = int(math.floor(math.sqrt(n)))
  for i in range(3, sqrt_n + 1, 2):
    if n % i == 0:
        return False
  return True

def main():
  start_2 = time.time()
  with concurrent.futures.ProcessPoolExecutor() as executor:
    for number, prime in zip(NUMBER, executor.map(what_prime, NUMBER)):
      print(f'{number} は素数ですか？: {prime}')
  end_2 = time.time()
  time_2 = end_2 - start_2
  print (f'全ての数の判断にかかった時間は:{time_2}秒です。')

if __name__ == '__main__':
  print("マルチプロセスでの素数判断処理")
  main()