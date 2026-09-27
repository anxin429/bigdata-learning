import datetime

def add(a, b):
    return a + b

def now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":

    print("=== myutils.py 自己在跑 ===")
    print("1 + 2 =", add(1, 2))
    print("现在时间:", now_str())
