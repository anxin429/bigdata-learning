# Day 3 · 条件 / 循环 / 控制流
# 用时约 120 分钟
# 运行：python day03.py

# ===== 任务 1：条件判断 ============================================
# 输入一个分数(0-100)，输出等级：
#   >=90 优秀 / >=80 良好 / >=60 及格 / <60 不及格
# 要求用 if-elif-else，并且要处理输入不在 0-100 的情况
# 提示：注意 input 转 int，非法输入用 try 或 isdigit 判断
s = input("请输入分数(0-100):")
try:
    score = int(s)
except ValueError:
    print("输入错误:分数必须在0-100之间")
else:
    if score < 0 or score > 100:
        print("输入错误:分数必须在0-100之间")
    elif score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
# ===== 任务 2：九九乘法表 ==========================================
# 输出标准九九乘法表，要求对齐：
#   1*1=1
#   1*2=2  2*2=4
#   ...
# 提示：双重 for；内层 range(1, i+1)；print(..., end="\t")
for i in range(1,10):
    for j in range(1,1+i):
        print(f"{j}*{i}={i*j}",end="\t")
    print()

# ===== 任务 3：break / continue / else ============================
# 3.1 遍历 1-20，遇到第一个能被 7 整除的数就停下（break）
# 3.2 打印 1-20 中所有奇数（用 continue 跳过偶数）
# 3.3 判断 97 是不是质数，用 for-else 写法
# 提示：for 循环正常结束（没 break）才会执行 else
for n in range(1,21):
    if n % 7 ==0:
        print("第一个被7整除的是:",n)
        break
    print("检查:",n)
for n in range(1,21):
    if n % 2 == 0:
        continue
    print(n)
num = 97
for i in range(2,int(num**0.5)+1):
    if num % i == 0:
        print(num,"不是质数,能被",i,"整除")
        break
else:
    print(num,"是质数")


# ===== 任务 4：enumerate / zip / range ============================
names = ["张三", "李四", "王五"]
scores = [88, 95, 72]
# 4.1 用 enumerate 打印带序号的姓名（从 1 开始）
# 4.2 用 zip 把 names 和 scores 配对，输出 "张三: 88"
# 4.3 用 range 生成 10, 8, 6, 4, 2（倒序步长）
# 提示：enumerate(x, start=1) / zip(a, b) / range(10, 0, -2)
names = ["张三","李四","王五"]
scores = [88, 95, 72]
for idx, name in enumerate(names, start=1):
    print(f"{idx}. {name}")
for name, score in zip(names,scores):
    print(f"{name}:{score}")
print(list(range(10,0,-2)))

# ===== 任务 5：while 循环 ==========================================
# 计算 1+2+...+100 的和，分别用 while 和 for 各写一遍
# 再用 sum(range(1,101)) 写第三遍，体会 Python 的简洁
total = 0
i = 1
while i<=100:
    total += i
print("sum结果:",total)
total = 0
for i in range(1,101):
    total += i
print("for 结果:",total)
total = sum(range(1,101))
print("结果:",total)
# ===== 任务 6：综合练习 · 猜数字游戏 ==============================
# 程序随机生成 1-100 的整数，用户反复猜：
#   猜大了 → 提示"大了"
#   猜小了 → 提示"小了"
#   猜对了 → 打印"恭喜，用了 N 次"并结束
# 加分：最多猜 7 次，超过就公布答案
# 提示：import random; random.randint(1, 100)
import random
answer = random.randint(1,100)
max_tries = 7
tries = 0
while tries < max_tries:
    guess = int(input(f"第{tries+1}次,猜1-100的数:"))
    tries += 1
    if guess >answer:
        print("大了")
    elif guess <answer:
        print("小了")
    else:
        print(f"恭喜,用了{tries}次猜中!")
        break
else:
    print(f"次数用尽,答案是{answer}")

# ===== 任务 7：综合练习 · FizzBuzz（面试常考） ====================
# 遍历 1-100：
#   能被 3 整除输出 Fizz
#   能被 5 整除输出 Buzz
#   同时能被 3 和 5 整除输出 FizzBuzz
#   否则输出数字本身
# 注意判断顺序：先判断 15 的情况，否则会漏
for n in range(1, 101):
    if n % 15 == 0:        # 同时被 3 和 5 整除（15 是 3 和 5 的最小公倍数）
        print("FizzBuzz")
    elif n % 3 == 0:       # 只被 3 整除
        print("Fizz")
    elif n % 5 == 0:       # 只被 5 整除
        print("Buzz")
    else:
        print(n)           # 都不能整除，输出数字本身


# ===== 自检清单 ====================================================
# [ ] 掌握 if-elif-else、for、while 的语法
# [ ] 理解 break/continue/for-else 的区别
# [ ] 会用 enumerate 取下标、zip 配对遍历
# [ ] 能独立写出猜数字和 FizzBuzz
