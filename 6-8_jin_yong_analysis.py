# 6.8 金庸多作品词频对比分析
import jieba

excludes = {"说道","知道","只见","如何","自己","出来","众人","一个","什么","今日","这般","便是"}

def get_top_words(filepath, top_n=10):
    with open(filepath,"r",encoding="gb18030") as f:
        txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for w in words:
        if len(w)>=2:
            counts[w] = counts.get(w,0)+1
    for w in excludes:
        if w in counts:
            counts.pop(w, None)
    items = sorted(counts.items(), key=lambda x:x[1], reverse=True)
    return items[:top_n]

if __name__ == "__main__":
    books = {
        "天龙八部": "天龙八部.txt",
        "射雕英雄传": "射雕英雄传.txt",
        "神雕侠侣": "神雕侠侣.txt"
    }
    for name, path in books.items():
        print(f"\n==== {name} Top10高频词 ====")
        res = get_top_words(path,10)
        for idx,(w,c) in enumerate(res):
            print(f"{idx+1}. {w} : {c}")