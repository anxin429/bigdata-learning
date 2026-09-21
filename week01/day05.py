# Day 5 · 文件读写 / 异常处理
# 用时约 120 分钟
# 运行：python day05.py
# 注意：所有 open() 都要指定 encoding="utf-8"，Windows 下不指定会乱码

# ===== 任务 1：读写文本文件 ========================================
# 1.1 用 with open(...) as f 写一个文件 test.txt，写入 3 行内容
# 1.2 再读回来，逐行打印
# 1.3 分别尝试 f.read() / f.readline() / f.readlines()，说出三者区别
# 提示：with 会自动关闭文件，不要用裸 open 忘 close


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


# ===== 任务 3：JSON 读写 ===========================================
import json

data = {"name": "张三", "age": 20, "courses": ["Python", "Java"], "graduated": False}
# 3.1 把 data 转成 JSON 字符串（ensure_ascii=False 才能正常显示中文）
# 3.2 写入 data.json，再读回来
# 3.3 对比 json.dumps / dump 和 loads / load 的区别（s = string）


# ===== 任务 4：异常处理 ============================================
# 4.1 捕获除零错误：10 / 0
# 4.2 捕获多个异常：int("abc") 和 [1,2][5]
# 4.3 用 try-except-else-finally 写一遍，观察各部分什么时候执行
# 4.4 用 raise 主动抛出一个 ValueError
# 提示：finally 无论是否异常都会执行，常用来释放资源


# ===== 任务 5：文件路径 ============================================
import os
# 5.1 打印当前工作目录 os.getcwd()
# 5.2 用 os.path.join 拼接路径（不要手写 "dir\\file"）
# 5.3 判断文件是否存在，不存在则创建
# 5.4 列出当前目录下所有 .py 文件
# 加分：用 pathlib.Path 重写一遍（现代写法，推荐）


# ===== 任务 6：综合练习 · 成绩管理系统 ============================
# 写一个完整的小程序：
#   1. 从 students.csv 读取成绩
#   2. 计算平均分、最高分、最低分
#   3. 把统计结果写入 report.txt
#   4. 把每个学生的等级（优秀/良好/及格/不及格）追加到 CSV 最后一列
#   5. 全程用 try-except 处理：文件不存在、数据格式错误
# 要求：逻辑拆成函数，不要写成一坨


# ===== 自检清单 ====================================================
# [ ] 习惯用 with open() 而不是裸 open
# [ ] Windows 下记得 encoding="utf-8" 和 newline=""
# [ ] 会 csv 和 json 的读写
# [ ] 理解 try-except-else-finally 各自的执行时机
