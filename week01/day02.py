# Day 2 · 列表 / 元组 / 字典 / 集合
# 用时约 120 分钟
# 运行：python day02.py

# ===== 任务 1：列表基本操作 ========================================
nums = [5, 2, 9, 1, 7, 2]
# 1.1 末尾追加 10，在索引 0 插入 0
# 1.2 删除第一个 2（注意 remove 只删第一个）
# 1.3 用 pop() 弹出最后一个元素并打印它
# 1.4 排序：升序、降序（不要改原列表的写法）
# 1.5 切片：取前 3 个、取偶数位、反转
# 提示：append insert remove pop sort sorted reverse
nums = [5 , 2, 9, 1, 7, 2]
nums.append(10)
nums.insert(0,0)
nums.remove(2)
last = nums.pop()
print("弹出:",last)
print("当前:",nums)
print("升序:",sorted(nums))
print("降序:",sorted(nums,reverse=True))
print("前三:",nums[:3])
print("偶数位：",nums[::2])
print("反转:",nums[::-1])
# ===== 任务 2：列表推导式 ==========================================
# 2.1 生成 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 2.2 从 nums 里筛出所有大于 3 的数
# 2.3 把 ["a","b","c"] 变成 ["A","B","C"]
# 提示：[expr for x in iterable if cond]
squares = [i*i for i in range(10)]
print("平方:",squares)
big = [x for x in nums if x>3]
print("大于3:",big)
ups = [w.upper()for w in ["a","b","c"]]
print("大写:",ups)
# ===== 任务 3：元组与解包 ==========================================
# 3.1 定义 point = (3, 5)，用解包取出 x, y
# 3.2 写一个函数返回两个值（最大值和最小值），调用时解包接收
# 3.3 交换两个变量 a, b 的值（一行搞定）
# 提示：a, b = b, a
point = (3,5)
x,y = point
print("x:",x,"y:",y)
def max_min(nums):
    return max(nums),min(nums)
mx,mn = max_min([8,3,12,1,9])
print("最大:",mx,"最小:",mn)
a,b = 1,2
a,b = b,a
print("a:",a,"b:",b)


# ===== 任务 4：字典 ================================================
# 4.1 建一个学生字典 {"name":"张三","age":20,"score":88}，增删改查各做一次
# 4.2 遍历字典的 key、value、键值对
# 4.3 用 get() 取一个不存在的 key，给默认值（对比 [] 取不到会报错）
# 4.4 合并两个字典
# 提示：dict.items() / get(k, default) / {**a, **b}
stu = {"name":"张三","age":20,"score":88}
stu["city"] = "北京"
stu["score"] = 95
print("姓名：",stu["name"])
removed = stu.pop("age")
print("删掉的age:",removed)
print("现在：",stu)
for k in stu:
    print("key:",k)
for v in stu.values():
    print("values:",v)
for k, v in stu.items():
    print(f"{k} = {v}")
print("get不存在的:",stu.get("age","无此字段"))
a = {"x":1,"y":2}
b = {"y":3,"z":4}
merged = {**a,**b}
print("合并:",merged)
# ===== 任务 5：用字典统计词频（重点，后面天天用） ==================
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# 不用 collections，用纯 dict 统计每个词出现次数
# 提示：d[w] = d.get(w, 0) + 1
# 进阶：用 collections.Counter 一行搞定，对比两种写法
words = ["apple","banana","apple","orange","banana","apple"]
d = {}
for w in words:
    d[w] = d.get(w,0)+1
print("纯dict:",d)

# ===== 任务 6：集合去重 ============================================
# 6.1 给 [1,2,2,3,3,3,4] 去重
# 6.2 求两个列表的交集、并集、差集
# 提示：set() & | -
lst = [1,2,2,3,3,3,4]
print("去重:",set(lst))
a = {1,2,3}
b = {3,4,5}
print("交集:",a&b)
print("并集:",a|b)
print("差集 a-b:",a-b)
print("差集 b-a:",b-a)
# ===== 任务 7：综合练习 · 成绩单 ==================================
students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 95},
    {"name": "王五", "score": 72},
    {"name": "赵六", "score": 60},
]
# 7.1 打印所有及格（>=60）的学生姓名
# 7.2 求平均分（保留 1 位小数）
# 7.3 找出最高分的学生
# 7.4 按分数从高到低排序
# 提示：max(list, key=lambda s: s["score"]) / sorted(..., key=..., reverse=True)
students = [
    {"name":"张三","score":88},
    {"name":"李四","score":95},
    {"name":"王五","score":72},
    {"name":"赵六","score":60},
]
passed = [s["name"] for s in students if s["score"]>=60]
print("及格:",passed)
avg = sum(s["score"] for s in students)
print(f"平均分:{avg:.1f}")
top = max(students,key=lambda s: s["score"])
print("最高分:",top["name"],top["score"])
ranked = sorted(students,key=lambda s: s["score"],reverse=True)
print("排名:",[(s["name"],s["score"]) for s in ranked])
# ===== 自检清单 ====================================================
# [ ] 能说出 list / tuple / dict / set 各自的特点和适用场景
# [ ] 会写列表推导式
# [ ] 知道 dict.get() 和 [] 的区别
# [ ] 能用 dict 做计数统计（这是 Pandas groupby 的底层思路）
