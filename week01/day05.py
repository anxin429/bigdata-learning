# Day 5 · 文件读写 / 异常处理
# 用时约 120 分钟
# 运行：python day05.py
# 注意：所有 open() 都要指定 encoding="utf-8"，Windows 下不指定会乱码

# ===== 任务 1：读写文本文件 ========================================
# 1.1 用 with open(...) as f 写一个文件 test.txt，写入 3 行内容
# 1.2 再读回来，逐行打印
# 1.3 分别尝试 f.read() / f.readline() / f.readlines()，说出三者区别
# 提示：with 会自动关闭文件，不要用裸 open 忘 close
# with open("test.txt","w",encoding="utf-8") as f:
#     f.write("第一行\n")
#     f.write("第二行\n")
#     f.write("第三行\n")
# with open("test.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line,end="")
# with open("test.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print("read->", repr(content))
# with open("test.txt","r",encoding="utf-8")as f:
#     print("readline ->",repr(f.readline()))
#     print("readline ->",repr(f.readline()))
# with open("test.txt","r",encoding=("utf-8")) as f:
#     lines = f.readlines()
#     print("readlines->",lines)
# ===== 任务 2：CSV 读写（后面天天用） =============================
import csv

rows = [
    ["name", "score"],
    ["张三", 88],
    ["李四", 95],
    ["王五", 72],
]
# 2.1 用 csv.writer 把 rows 写入 students.csv
#    注意：open 时要加 newline=""，否则 Windows 下会多空行
# 2.2 用 csv.reader 读回来并打印
# 2.3 改用 csv.DictWriter / DictReader 写一遍（按列名操作更清晰）
# import csv
# rows = [["name","score"],
#         ["张三", 88],
#         ["李四",95],
#         ["王五",72],
# ]
# with open("students.csv","w",newline="",encoding="utf-8") as f:
#     w = csv.writer(f)
#     w.writerows(rows)
# with open("students.csv","r",encoding="utf-8")as f:
#     r = csv.reader(f)
#     for row in r:
#         print(row)
# with open("students2.csv","w",newline="",encoding="utf-8") as f:
#     w = csv.DictWriter(f,fieldnames=["name","score"])
#     w.writeheader()
#     w.writerow({"name":"张三","score":88})
#     w.writerow({"name":"李四","score":95})
#     w.writerow({"name":"王五","score":72}) 
# with open("students2.csv","r",encoding="utf-8") as f:
#     r = csv.DictReader(f)
#     for row in r:
#         print(row["name"],row["score"])

# ===== 任务 3：JSON 读写 ===========================================
import json

data = {"name": "张三", "age": 20, "courses": ["Python", "Java"], "graduated": False}
# 3.1 把 data 转成 JSON 字符串（ensure_ascii=False 才能正常显示中文）
# 3.2 写入 data.json，再读回来
# 3.3 对比 json.dumps / dump 和 loads / load 的区别（s = string）
# import json
# data = {"name":"张三","age":20,"courses":["python","java"],"garaduated":False}
# s = json.dumps(data,ensure_ascii=False,indent=2)
# print(s)
# print(type(s))
# with open("data.json","w",encoding="utf-8") as f:
#     json.dump(data,f,ensure_ascii=False,indent=2)
# with open("data.json","r",encoding="utf-8") as f:
#     lodede = json.load(f)
#     print(lodede)
#     print(type(lodede))
# # ===== 任务 4：异常处理 ============================================
# 4.1 捕获除零错误：10 / 0
# 4.2 捕获多个异常：int("abc") 和 [1,2][5]
# 4.3 用 try-except-else-finally 写一遍，观察各部分什么时候执行
# 4.4 用 raise 主动抛出一个 ValueError
# 提示：finally 无论是否异常都会执行，常用来释放资源
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("出错:不能除以0")
# try:
#     int("abc")
# except (ValueError,IndentationError) as e:
#     print("出错:",e)
# try:
#     int("abc")
# except ValueError:
#     print("不是合法数字")
# try:
#     print([1,2][5])
# except IndexError:
#     print("下标越界")
# try:
#     x = int(input("请输入一个数字:"))
# except ValueError:
#     print("输入的不是数字！")
# else:
#     print("转换成功,x =",x)
# finally:
#     print("无论成功失败，我都会执行")
# def check_age(age):
#     if age < 0:
#         raise ValueError("年龄不能是负数")
#     print("年龄合法:",age)
# ===== 任务 5：文件路径 ============================================
import os
# 5.1 打印当前工作目录 os.getcwd()
# 5.2 用 os.path.join 拼接路径（不要手写 "dir\\file"）
# 5.3 判断文件是否存在，不存在则创建
# 5.4 列出当前目录下所有 .py 文件
# 加分：用 pathlib.Path 重写一遍（现代写法，推荐）
# import os
# print(os.getcwd())
# path = os.path.join("week01","day05.py")
# print(path)
# import os
# f = os.path.join("bigdata-learning","week01","new.txt")
# if not os.path.exists(f):
#     with open(f,"w",encoding="utf-8") as fh:
#         fh.write("新建的文件\n")
#     print("文件已创建")
# else:
#     print("文件已存在")
# import os 
# for name in os.listdir("."):
#     if name.endswith(".py"):
#         print(name)
# from pathlib import Path
# cwd = Path.cwd()
# print(cwd)
# p = Path("bigdata-learning")/"week01"/"day05.py"
# print(p)
# if not p.exists():
#     p.write_text("新建的文件\n",encoding="utf-8")
# for f in Path(".").glob("*.py"):
#     print(f)
# ===== 任务 6：综合练习 · 成绩管理系统 ============================
# 写一个完整的小程序：
#   1. 从 students.csv 读取成绩
#   2. 计算平均分、最高分、最低分
#   3. 把统计结果写入 report.txt
#   4. 把每个学生的等级（优秀/良好/及格/不及格）追加到 CSV 最后一列
#   5. 全程用 try-except 处理：文件不存在、数据格式错误
# 要求：逻辑拆成函数，不要写成一坨
import csv
def grade_of(score):
    if score >=90:return "优秀"
    elif score >=80: return "良好"
    elif score >=60: return "及格"
    else: return "不及格"
def read_students(path):
    students = []
    try :
        with open(path,"r",encoding="utf_8")as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    score = float(row["score"])
                except(ValueError,KeyError)as e:
                    print(f"跳过坏数据{row},原因{e}")
                    continue
                students.append({"name":row["name"],"score":score})
    except FileNotFoundError:
        print(f"文件不存在:{path}")
    return students
def compute_stats(students):
    scores = [s["score"]for s in students]
    if not scores:
        return{"avg":0,"max":0,"min":0}
    return{"avg":sum(scores)/len(scores),
           "max":max(scores),"min":min(scores)}
def write_report(stats,path):
    try:
        with open(path,"w",encoding="utf-8") as f:
            f.write(f"平均分:{stats['avg']:.2f}\n")
            f.write(f"最高分:{stats['max']}\n")
            f.write(f"最低分:{stats['min']}\n")
    except IOError as e:
        print(f"写报告失败:{e}")
def save_with_grade(students,path):
    try:
        with open(path,"w",newline="",encoding="utf-8")as f:
            w = csv.DictWriter(f,fieldnames=["name","score","grade"])
            w.writeheader()
            for s in students:
                s["grade"] =  grade_of(s["score"])
                w.writerow(s)
    except IOError as e:
        print(f"写csv失败:{e}")
def main():
    students = read_students("students.csv")
    if not students:
        print("没有可用数据,结束")
        return
    stats = compute_stats(students)
    write_report(stats,"report.txt")
    save_with_grade(students,"students_with_grade.csv")
    print("处理完成!report.txt和students_with_grade.csv已生成")
if __name__ == "__main__":
    main()
# ===== 自检清单 ====================================================
# [ ] 习惯用 with open() 而不是裸 open
# [ ] Windows 下记得 encoding="utf-8" 和 newline=""
# [ ] 会 csv 和 json 的读写
# [ ] 理解 try-except-else-finally 各自的执行时机
