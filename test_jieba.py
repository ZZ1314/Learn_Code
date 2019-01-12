import jieba

# 文件地址
path_hamlet = "jieba_txt/hamlet.txt"
path_tk = 'jieba_txt/threekingdoms.txt'

# # 获取文件函数
# def getText():
#     txt = open(path_hamlet, "r").read()
#     # 小写文本
#     txt = txt.lower()
#     # 排除符号
#     for ch in '''!'@#$%^&*()_+-=,./<>?;:"[]{}''':
#         txt = txt.replace(ch, " ")
#     return txt
#
#
# hamlet_txt = getText()
# # 分词处理
# words = hamlet_txt.split()
# # 空字典
# counts = {}
# for word in words:
#     # word 为 key count为value
#     counts[word] = counts.get(word, 0) + 1
# # 字典列表化 .items获取key,values
# item = list(counts.items())
# item.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
#     word, count = item[i]
#     print("{0:<10}:{1:>5}".format(word, count))


txt = open(path_tk, "r", encoding="UTF-8").read()
excludes = {'将军', "二人", "不可", "不能", "却说", "如此", "商议", "如何", "主公", "军士", "左右", "军马"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
        # word 为 key count为value
    counts[rword] = counts.get(rword, 0) + 1

for word in excludes:
    del counts[word]
# 字典列表化 .items获取key,values
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}:{1:>5}".format(word, count))
