# Day 4 · 函数 / 参数 / 作用域 / lambda
# 用时约 120 分钟
# 运行：python day04.py

# ===== 任务 1：函数基本写法 ========================================
# 写一个函数 greet(name)，打印 "你好，{name}！"
# 再写一个函数 add(a, b) 返回 a + b（注意是 return 不是 print）
def greet(name):
    print(f"你好,{name}!")
def add(a,b):
    return(a+b)
print("小明")
print(add(3,5))
# ===== 任务 2：四种参数（重点） ====================================
# 写一个函数 demo(a, b=10, *args, **kwargs)，调用时分别传入：
#   demo(1)
#   demo(1, 2)
#   demo(1, 2, 3, 4)
#   demo(1, 2, 3, name="张三", age=20)
# 在函数里打印 a, b, args, kwargs，观察它们分别是什么类型
# 提示：args 是 tuple，kwargs 是 dict
def demo(a,b=10,*args,**kwargs):
    print("a =", a, type(a))
    print("b =", b, type(b))
    print("args =", args, type(args))
    print("kwargs =", kwargs, type(kwargs))
    print("-"*20)
demo(1)
demo(1,2)
demo(1,2,3,4)
demo(1,2,3,name = "张三",age = 20)
# ===== 任务 3：默认参数的坑（必踩一次） ===========================
# 错误示范：def append_item(x, lst=[]): lst.append(x); return lst
# 连续调用 append_item(1)、append_item(2)，观察结果是不是 [1, 2]
# 为什么？正确写法是什么？
# 提示：默认参数在函数定义时只创建一次，可变对象会被共享
# 正确写法：lst=None，函数内 if lst is None: lst = []
#def append_item(x, lst = []):
#    lst.append(x)
#    return lst
#print(append_item(1))
#print(append_item(2))
def append_item(x, lst = None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
print(append_item(1))
print(append_item(2))
# ===== 任务 4：作用域 ==============================================
x = 10
# 4.1 写一个函数读 x，能读到吗？
# 4.2 在函数里写 x = 20，外面的 x 变了吗？为什么？
# 4.3 用 global 在函数里真正修改外面的 x
# 4.4 体会：不要滥用 global，尽量用返回值
x = 10
def read_x():
    print("4.1函数内读到的 x =",x)
read_x()
print("4.1外面的x =", x)
def write_x():
    x = 20
    print("4.2函数内x =",x)
write_x()
print("4.2 外面的x =",x)
def change_x():
    global x
    x = 20
    print(f"4.3函数内x={x}")
change_x()
print(f"4.3外面的x ={x}")


# ===== 任务 5：lambda 与高阶函数 ===================================
students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 95},
    {"name": "王五", "score": 72},
]
# 5.1 用 sorted + lambda 按 score 降序排
# 5.2 用 map + lambda 把所有分数 +5
# 5.3 用 filter + lambda 筛出及格的人
# 5.4 对比：同样的需求用列表推导式怎么写？（推导式更 Pythonic）
students = [
    {"name":"张三","score":88},
    {"name":"李四","score":95},
    {"name":"王五","score":72},
]
by_score = sorted(students, key=lambda s: s["score"],reverse=True)
print(by_score)
new_scores = list(map(lambda s:s["score"]+5,students))
print(new_scores)
passed = list(filter(lambda s: s["score"]>= 60,students))
print(passed)
new2 = [s["score"]+5 for s in students]
print(new2)
passed2 = [s for s in students if s["score"]>=60]
print(passed2)
# ===== 任务 6：递归 ================================================
# 6.1 用递归写阶乘 n!
# 6.2 用递归写斐波那契第 n 项（体会它有多慢，n=35 试试）
# 6.3 用循环改写斐波那契，对比速度
# 提示：递归必须有终止条件
def factorial(n):
    if n == 1:
        return 1
    return n* factorial(n-1)
print(factorial(5))
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))
# ===== 任务 7：综合练习 · 计算器模块 ==============================
# 写一个模块化的计算器：
#   add / sub / mul / div 四个函数
#   div 要处理除数为 0 的情况（返回 None 或抛异常）
#   再写一个 dispatch(op, a, b)，用字典映射操作符到函数
#   例如 dispatch("+", 3, 5) -> 8
# 提示：ops = {"+": add, "-": sub, ...}
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return None
    return a / b
def dispatch(op, a ,b):
    ops = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":div,
    }
    return ops[op](a,b)
print(dispatch("+",3,5))
print(dispatch("-",10,4))
print(dispatch("*",3,5))
print(dispatch("/",10,2))
print(dispatch("/",10,0))
# ===== 自检清单 ====================================================
# [ ] 能解释 *args 和 **kwargs
# [ ] 知道默认参数不要用可变对象
# [ ] 理解局部变量和全局变量
# [ ] 会用 sorted(..., key=lambda ...) 排序复杂结构
# [ ] 知道递归要有终止条件
