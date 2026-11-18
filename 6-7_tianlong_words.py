# 6.7 天龙八部高频词（词语≥2字符）
import jieba

excludes = {"说道","知道","只见","如何","自己","出来","众人","一个","什么","今日"}

if __name__ == "__main__":
    with open("天龙八部.txt","r",encoding="gb18030") as f:
        txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for w in words:
        if len(w) >=2:
            counts[w] = counts.get(w,0)+1
    for w in excludes:
        if w in counts:
            del counts[w]
    items = sorted(counts.items(), key=lambda x:x[1], reverse=True)
    print("天龙八部最高频10个词语：")
    for i in range(10):
        word,num = items[i]
        print(f"{i+1}. {word}  {num}")