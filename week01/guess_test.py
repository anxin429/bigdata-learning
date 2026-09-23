# 单独的猜数字测试，排除 day03.py 里其他代码干扰
import random

answer = random.randint(1, 100)
max_tries = 7
tries = 0

print("=== 游戏开始，答案是 1-100 之间的某个数 ===")
while tries < max_tries:
    guess = int(input(f"第{tries+1}次,猜1-100的数:"))
    tries += 1
    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print(f"恭喜,用了{tries}次猜中!")
        break
else:
    print(f"次数用尽,答案是{answer}")
