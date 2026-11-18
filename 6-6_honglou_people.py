# 6.6 红楼梦人物统计 jieba词频
import jieba

# 停用词、无关词过滤
excludes = {"什么","一个","我们","那里","你们","如今","说道","知道","起来","姑娘","这里","出来","众人","自己","一面","只见","两个","没有","怎么","不是"}

if __name__ == "__main__":
    # 替换为你的txt路径，编码gb18030
    with open("红楼梦.txt","r",encoding="gb18030") as f:
        txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for w in words:
        if len(w) ==1:
            continue
        # 人物别名合并
        if w == "宝玉":
            w = "贾宝玉"
        elif w == "黛玉":
            w = "林黛玉"
        elif w == "宝钗":
            w = "薛宝钗"
        counts[w] = counts.get(w,0)+1
    # 删除停用词
    for w in excludes:
        if w in counts:
            del counts[w]
    items = sorted(counts.items(), key=lambda x:x[1], reverse=True)
    print("红楼梦出场最多前20人物：")
    for i in range(20):
        name,num = items[i]
        print(f"{i+1:2d}. {name:4s} {num}次")