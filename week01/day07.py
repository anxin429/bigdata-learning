# Day 7 · 综合项目：文本文件词频统计
# 目标：独立完成，不看参考答案
# 用时约 150 分钟
# 运行：python day07.py <文本文件路径>

"""
需求
----
读一个英文文本文件，统计词频，输出出现次数最多的 20 个词，
并把完整结果写入 wordcount_result.csv。

要求
----
1. 读文件（utf-8，要处理文件不存在的情况）
2. 清洗：全部转小写、去掉标点符号和数字
3. 分词：按空白切分
4. 过滤停用词（the / a / is / and 等，自己列一个 20 个词左右的列表）
5. 统计：用 dict 或 Counter
6. 输出：
   - 终端打印 Top20，格式对齐
   - 结果写入 wordcount_result.csv（两列：word, count）
7. 额外打印：总词数、去重后词数、平均词长

加分项（选做）
--------------
- 支持从命令行传文件路径（sys.argv 或 argparse）
- 词形还原的简单处理：复数 s 去掉（books -> book）
- 统计双词组合（bigram）的 Top10
- 用 matplotlib 画 Top10 的柱状图（提前装好 pip install matplotlib）

测试素材
--------
没有英文文本的话，用下面这段生成一个（或者找一篇英文新闻、小说 txt）：
"""

SAMPLE_TEXT = """
Big data is a field that treats ways to analyze, systematically extract
information from, or otherwise deal with data sets that are too large or
complex to be dealt with by traditional data processing application software.
Data with many cases offer greater statistical power, while data with higher
complexity may lead to a higher false discovery rate. Big data analysis
challenges include capturing data, data storage, data analysis, search,
sharing, transfer, visualization, querying, updating and information privacy.
"""

# 提示：可以先用 SAMPLE_TEXT 跑通逻辑，再换成真实文件


def read_file(path):
    """读取文本文件，返回字符串。文件不存在时返回 None 并打印提示"""
    # TODO
    pass


def clean_text(text):
    """转小写、去掉标点和数字"""
    # TODO
    # 提示：re.sub(r"[^a-z\s]", "", text.lower())
    pass


def tokenize(text, stopwords):
    """切词并过滤停用词和空串"""
    # TODO
    pass


def count_words(words):
    """统计词频，返回 dict"""
    # TODO
    pass


def print_top(counter, n=20):
    """格式化打印 Top N"""
    # TODO
    # 提示：print(f"{i:>3}. {word:<15} {count:>5}")
    pass


def write_csv(counter, path="wordcount_result.csv"):
    """把结果写入 CSV"""
    # TODO
    pass


def main():
    # TODO: 串起整个流程
    pass


if __name__ == "__main__":
    main()


# ===== 周末验收 ====================================================
# [ ] 不看参考答案独立跑通
# [ ] 能处理中文路径和编码问题
# [ ] 结果 CSV 能用 Excel / pandas 正常打开
# [ ] 代码拆成了函数，不是一坨
# [ ] 已 git commit 并 push 到 GitHub
