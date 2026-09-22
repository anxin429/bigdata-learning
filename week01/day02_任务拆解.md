# Day 02 · 任务拆解（逐项打勾版）

> 目标：列表 / 元组 / 字典 / 集合 四种容器玩熟
> 总时长约 120 分钟，按顺序做，每完成一项打勾 ✅
> 运行：`python day02.py`（或 VSCode 右上角 ▶）

---

## 任务 1 · 列表基本操作（约 20 分钟）

- [ ] 1.1 末尾追加 10 → `nums.append(10)`
- [ ] 1.2 索引 0 处插入 0 → `nums.insert(0, 0)`
- [ ] 1.3 删第一个 2 → `nums.remove(2)`（只删第一个）
- [ ] 1.4 `pop()` 弹出最后一个元素并打印 → `last = nums.pop(); print(last)`
- [ ] 1.5 排序（**不改原列表**）→ `sorted(nums)` 升序、`sorted(nums, reverse=True)` 降序
- [ ] 1.6 切片：前 3 个 `nums[:3]`、偶数位（索引 0/2/4）`nums[::2]`、反转 `nums[::-1]`

**完成标准**：能口述 `append` / `insert` / `remove` / `pop` 各自干啥；知道 `sort()` 改原列表、`sorted()` 不改。

**坑**：`remove(2)` 只删第一个 2，不会全删；想全删用列表推导式（任务 2）。

---

## 任务 2 · 列表推导式（约 15 分钟）

- [ ] 2.1 生成 `[0,1,4,9,...,81]` → `[i*i for i in range(10)]`
- [ ] 2.2 从 nums 筛出 >3 的数 → `[x for x in nums if x > 3]`
- [ ] 2.3 `["a","b","c"]` 变大写 → `[w.upper() for w in ["a","b","c"]]`

**完成标准**：能默写模板 `[表达式 for 变量 in 可迭代对象 if 条件]`，并说出它是"循环+处理的压缩写法"。

---

## 任务 3 · 元组与解包（约 10 分钟）

- [ ] 3.1 定义 `point = (3, 5)`，解包 → `x, y = point`
- [ ] 3.2 写函数返回（最大, 最小），调用时解包接收：
  ```python
  def minmax(lst):
      return max(lst), min(lst)
  hi, lo = minmax([5, 2, 9, 1])
  ```
- [ ] 3.3 一行交换 `a, b` → `a, b = b, a`

**完成标准**：理解"解包"= 把右边多个值按顺序赋给左边多个变量；记住一行交换 idiom。

---

## 任务 4 · 字典（重点，约 20 分钟）

- [ ] 4.1 建 `{"name":"张三","age":20,"score":88}`，各做一次：
  - 增：`d["gender"] = "M"`
  - 删：`del d["score"]`
  - 改：`d["age"] = 21`
  - 查：`print(d["name"])`
- [ ] 4.2 遍历：key `for k in d`、value `for v in d.values()`、键值对 `for k, v in d.items()`
- [ ] 4.3 `get()` 取不存在的 key 给默认值 → `d.get("xxx", "没找到")`；对比 `d["xxx"]` 会 `KeyError`
- [ ] 4.4 合并两字典 → `{**a, **b}`

**完成标准**：能说出 `d.get(k, 默认)` 和 `d[k]` 的区别（取不到时一个给默认值不报错，一个报错）。

---

## 任务 5 · 字典统计词频（重点中的重点，约 15 分钟）

- [ ] 5.1 纯 dict 统计（不用 Counter）：
  ```python
  words = ["apple","banana","apple","orange","banana","apple"]
  d = {}
  for w in words:
      d[w] = d.get(w, 0) + 1
  print(d)
  ```
- [ ] 5.2 进阶：用 `collections.Counter` 一行 → `print(Counter(words))`，对比两种写法

**完成标准**：理解 `d.get(w, 0) + 1` —— 取不到返回 0 再加 1。这是**计数统计的万能模板**，也是后面 Pandas `groupby` 的底层思路。

---

## 任务 6 · 集合去重（约 10 分钟）

- [ ] 6.1 `[1,2,2,3,3,3,4]` 去重 → `list(set([1,2,2,3,3,3,4]))`
- [ ] 6.2 交集 `&`、并集 `|`、差集 `-`：
  ```python
  a, b = {1,2,3}, {2,3,4}
  print(a & b, a | b, a - b)   # {2,3} {1,2,3,4} {1}
  ```

**完成标准**：记住集合三特性——无序、去重、支持交并差；去重首选 `set()`。

---

## 任务 7 · 综合 · 成绩单（约 25 分钟）

- [ ] 7.1 打印及格（>=60）学生姓名 → `[s["name"] for s in students if s["score"] >= 60]`
- [ ] 7.2 平均分（保留 1 位）→ `sum(s["score"] for s in students) / len(students)`，用 `f"{avg:.1f}"`
- [ ] 7.3 最高分学生 → `max(students, key=lambda s: s["score"])`
- [ ] 7.4 按分数从高到低排序 → `sorted(students, key=lambda s: s["score"], reverse=True)`

**完成标准**：能解释 `key=lambda s: s["score"]` —— 告诉 `max`/`sorted`"按 score 这个字段比大小"，而不是按整个字典。

---

## 收尾（做完所有任务）

- [ ] 打开 `参考答案.md` 对照写法
- [ ] 在 `day02.py` 里写 3 行今日笔记（容器各自适用场景）
- [ ] 提交亮绿点：
  ```bash
  git add .
  git commit -m "day02: 容器 list/tuple/dict/set 与词频统计"
  git push
  ```

## 每日 SQL（从今天立习惯，15 分钟）
- 牛客网「SQL 必知必会」刷 2 题（SELECT / WHERE / ORDER BY）
- 今天没做的话，明天补上，之后每天保持

## 自检清单（全打勾 = Day 2 过关）
- [ ] 能说 list / tuple / dict / set 各自特点和适用场景
- [ ] 会写列表推导式
- [ ] 知道 `dict.get()` 和 `[]` 的区别
- [ ] 能用 dict 做计数统计
- [ ] 理解 `key=lambda` 在 `max` / `sorted` 里的作用
