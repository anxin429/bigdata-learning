# Day 1 · 变量 / 数据类型 / 字符串
# 用时约 90 分钟 | 先自己写，卡住看提示，全部做完再看 参考答案.md
# 运行：python day01.py

# ===== 任务 1：变量与类型 ==========================================
# 定义 4 个变量：name(str) / age(int) / height(float) / is_student(bool)
# 打印它们的值，并用 type() 打印各自的类型
# 提示：Python 动态类型，不需要声明

name = "陈文洁"
age = 20
height = 80.0
is_student = True
print(name,type(name))
print(age ,type(age))
print(height,type(height))
print(is_student,type(is_student))
# ===== 任务 2：类型转换 ============================================
# 用 input() 读两个数字，输出它们的和
# 注意：input() 返回 str，不转类型会变成字符串拼接
# 提示：int(x) / float(x)
s1 = input("请输入第一个数字！")
s2 = input("请输入第二个数字！")
a = int(s1)
b = int(s2)
print(a+b)
# ===== 任务 3：字符串常用操作 ======================================
s = "  Hello, Big Data World  "
# 3.1 去掉首尾空格
# 3.2 转小写 / 转大写
# 3.3 把 "Big Data" 替换成 "Python"
# 3.4 用逗号切分成列表，再用 "-".join() 拼回字符串
# 3.5 切片：取前 5 个字符、取最后 5 个字符、倒序输出
# 提示：strip() lower() upper() replace() split() join() [start:end:step]
s = " Hello,Big Data World "
t = s.strip()
print("去空格后：",repr(t))
print("大写:",t.upper())
print("小写：",t.lower)
print("替换后:",t.replace("Big Data","Python"))
parts = t.split(",")
print("拆分:",parts)
print("拼回:","-".join(parts))
print("前5个:",t[:5])
print("最后5个：",t[-5:])
print("倒序：",t[::-1])
# ===== 任务 4：f-string 格式化 =====================================
# name="张三" city="北京" salary=12345.678
# 输出："张三 来自 北京，月薪 12345.68 元"
# 要求 salary 保留 2 位小数、总宽度 12、右对齐
# 提示：f"{salary:>12.2f}"
name = "张三"
city = "北京"
salary = 12345.78
print(f"{name}来自{city},月薪{salary:>12.2f}元")

# ===== 任务 5：综合练习 · 名片生成器 ==============================
# 让用户输入一行 "姓名,年龄,城市"，例如 "张三,20,北京"
# 解析后输出：
#   ================
#   姓名：张三
#   年龄：20 岁
#   城市：北京
#   ================
# 提示：split(",")；年龄记得转 int
line = input("请输入 姓名，年龄，城市:")
parts = line.split(",")
p_name = parts[0]
p_age = int(parts[1])
p_city = parts[2]
bar = "=" * 16
print(bar)
print(f"姓名:{p_name}")
print(f"年龄:{p_age}岁")
print(f"城市:{p_city}")
print(bar)
# ===== 自检清单 ====================================================
# [ ] 能说出 int / float / str / bool / None 五种基本类型
# [ ] 知道 input() 返回的是字符串
# [ ] 会写 f-string，知道 :.2f 和 :>12 的含义
# [ ] 理解切片 [start:end:step] 里 step=-1 是倒序
