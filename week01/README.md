# Week 01 · Python 基础补齐（09.21 – 09.27）

> 目标：**不看资料能独立写出 100 行以上的完整脚本**
> 每天 2–4 小时。已确认环境：Python 3.13.14 ✓ / Git ✓ / JDK 8 ✓ / IDEA 2024.3 ✓

---

## 今天（D1）立刻要做的四件事

### ① 编辑器（20 分钟）
二选一，别纠结：
- **装 VSCode**（推荐，Python 阶段轻量、Jupyter 方便）→ https://code.visualstudio.com/ ，装完装 `Python` 和 `Jupyter` 扩展
- 或在现有 IDEA 里装 `Python` 插件（Settings → Plugins → 搜 Python）

### ② 建 GitHub 仓库（15 分钟）
1. GitHub 新建仓库 `bigdata-learning`，**不要**勾选 README
2. 本地已经 `git init` 好了，执行：
```bash
git remote add origin https://github.com/<你的用户名>/bigdata-learning.git
git add .
git commit -m "week01: 开始 Python 基础"
git push -u origin main
```
> 如果提示 branch 名不是 main，先 `git branch -M main`

### ③ 跑通第一个脚本（5 分钟）
```bash
cd week01
python day01.py
```
能正常运行就说明环境没问题。

### ④ 开始 Day 1 的练习（90 分钟）
打开 `day01.py`，按里面的 TODO 写。**先自己写，卡住看提示，全部做完再看 `参考答案.md`。**

---

## 本周七天安排

| 天 | 主题 | 练习文件 | 完成标准（自检） |
|---|---|---|---|
| D1 | 变量、数据类型、字符串 | `day01.py` | 能熟练用 f-string 格式化输出 |
| D2 | 列表、元组、字典、集合 | `day02.py` | 能用 dict 统计词频 |
| D3 | 条件、循环、控制流 | `day03.py` | 能写出九九乘法表 |
| D4 | 函数、参数、作用域、lambda | `day04.py` | 能解释 `*args` 和 `**kwargs` |
| D5 | 文件读写、异常处理 | `day05.py` | 能读写 CSV 和 JSON |
| D6 | 模块、包、虚拟环境、标准库 | `day06.py` | 能建 venv 并装第三方包 |
| D7 | 综合项目：词频统计 | `day07.py` | 独立完成，不看答案 |

**你有基础的话**：D1–D3 可以压成两天，省出的时间给 D5–D7。但**练习必须做**，不能跳过。

---

## 每日固定动作（雷打不动）

| 时段 | 内容 |
|---|---|
| 开始 20 min | 复习昨天代码 + 笔记 |
| 中间 | 按练习文件写代码 |
| 最后 30 min | **SQL 1–2 题**（牛客网 SQL 必知必会） |
| 收尾 10 min | 写笔记 + `git commit` |

> SQL 从 D1 就要开始，本周目标是刷完基础查询，下周开始窗口函数。

---

## 周末验收（09.27 晚上）

- [ ] 7 个练习文件全部自己写完（不是抄答案）
- [ ] `day07.py` 词频统计能独立跑通，输出 Top20
- [ ] GitHub 上有 6–7 天连续提交（绿点连成片）
- [ ] SQL 基础查询刷完
- [ ] 有一份自己的笔记（哪怕只有几行）

---

## 卡住时怎么办

1. 报错先看**最后一行**的错误类型（`TypeError` / `NameError` / `IndentationError`）
2. 敲不定 API 就 `python` 进交互模式试，比查文档快
3. 单个问题卡超过 20 分钟 → 跳过，标记下来，第二天再回头
4. **不要**一上来就问 AI 要完整答案，先自己试 3 次
