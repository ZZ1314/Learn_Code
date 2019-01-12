import wordcloud
import jieba

# height高度 width宽度
# minfontsize最小字号 maxfontsize最大字号
# font_step 字间距
# font_path 字体文件
# max_words 最大单词数量
# stop_words 排除单词
# backgroundcolor 背景颜色
# mask 词云形状
path = 'jieba_txt/threekingdoms.txt'
font = 'Hiragino Sans GB.ttc'
f = open(path, "r", encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path=font,
                        width=1000, height=700, background_color='white'
                        )
w.generate(txt)
w.to_file("wc.png")
