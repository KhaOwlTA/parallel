import math, time

def is_prime(n):
    """素数判定

    平方根までの数で割り切れるかどうかを調べる。

    Args:
        n (int): 調べたい数字

    Return:
        bool: Trueなら素数、Falseならそうではない。
    """
    ## あらかじめ偶数と1を先に判定する。
    if n <= 1:  ## 1以下は素数ではない。
        return False
    if n == 2:  ## 2は素数である。
        return True
    if n % 2 == 0:  ## 2の倍数は素数ではない。
        return False

    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):  ## 平方根の数までの奇数の範囲繰り返す。
        if n % i == 0:
            return False
    return True

def my_sum(n):
    """総和計算

    1からnまでの数の総和を計算する。
    その際、数字を一つ足すごとに0.1秒スリープさせる。

    Args:
        n (int): 計算する総和の数値

    Return:
        s (int): 1からnまでの数の総和
    """
    s = 0
    for i in range(1, n + 1):
        s += i
        time.sleep(0.1)  ## スリープさせる
    return s

def studentID(name, number):
    """学籍番号と名前の組み合わせを返す関数

    0.51秒スリープさせた後に学籍番号と名前から文を返します。

    Args:
        name (str): 名前
        number (int): 学籍番号の下2桁

    Return:
        studentID (str): 学籍番号と名前から生成した文
    """
    time.sleep(0.51)  ## スリープさせる
    studentID = f"e1957{str(number).zfill(2)} = {name}さん"
    return studentID
