# Day 6 · 模块 / 包 / 虚拟环境 / 标准库
# 用时约 120 分钟
# 运行：python day06.py

# ===== 任务 1：自定义模块 ==========================================
# 1.1 新建文件 myutils.py，写两个函数：add(a,b) 和 now_str()
# 1.2 在 day06.py 里 import 并使用
# 1.3 体会 if __name__ == "__main__": 的作用
#     （在 myutils.py 底部加测试代码，分别在直接运行和被 import 时观察）
# 提示：被 import 时 __name__ 是模块名，直接运行时是 "__main__"


# ===== 任务 2：包的组织 ============================================
# 建一个目录 mypkg/，里面放 __init__.py、math_utils.py、str_utils.py
# 然后从外部 from mypkg import math_utils 使用
# 提示：__init__.py 可以是空文件，它的存在让目录变成"包"


# ===== 任务 3：虚拟环境（必做，后面装包全靠它） ===================
# 在命令行执行（不要在 py 文件里）：
#   python -m venv .venv
#   .venv\Scripts\activate          (Windows)
#   pip install requests
#   pip list
#   pip freeze > requirements.txt
# 观察：激活后命令行前面会出现 (.venv)
# 为什么需要虚拟环境？——不同项目依赖版本冲突


# ===== 任务 4：常用标准库 ==========================================
import os
import sys
import time
import random
import datetime
import re

# 4.1 os：获取当前目录、拼接路径、判断文件存在、列目录
# 4.2 sys：打印 sys.argv（命令行参数）、sys.version
# 4.3 time：time.time() 计时一段代码、time.sleep(1)
# 4.4 datetime：获取当前时间、格式化成 "2026-09-26 14:30:00"、
#               字符串转 datetime、计算 7 天后是几号
# 4.5 random：随机整数、随机选择、打乱列表
# 4.6 re：用正则从 "订单号：A20260926001，金额：￥128.50" 里
#         提取出订单号和金额
# 提示：strftime 格式化 / strptime 解析 / re.findall / re.search


# ===== 任务 5：collections 与 itertools（数据分析常用） ===========
from collections import Counter, defaultdict, namedtuple, deque
# 5.1 Counter：统计词频并取 Top3（most_common）
# 5.2 defaultdict：按首字母把单词分组（对比普通 dict 的繁琐）
# 5.3 namedtuple：定义一个 Point(x, y)，用 .x .y 访问
# 5.4 deque：实现一个固定长度为 3 的队列


# ===== 任务 6：综合练习 · 批量重命名脚本 ==========================
# 写一个脚本，把指定目录下所有 .txt 文件重命名成
#   "2026-09-26_001.txt" 这种格式（日期_序号）
# 要求：
#   1. 目录路径从命令行参数传入（sys.argv）
#   2. 目标目录不存在时给出友好提示并退出
#   3. 打印每一步的旧名 → 新名
#   4. 先用 print 演练（dry-run），确认无误后再真正改名
# 加分：用 argparse 改写，支持 --dir 和 --dry-run 参数


# ===== 自检清单 ====================================================
# [ ] 理解 if __name__ == "__main__"
# [ ] 能创建并激活 venv，会用 pip 装包
# [ ] 会用 datetime 做时间格式化和计算
# [ ] 会用 re 提取关键信息
# [ ] 知道 Counter 和 defaultdict 的用法
