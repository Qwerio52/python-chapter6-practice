# 6.4 文字字符频率分析
def char_analysis(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    # 按频次降序排序
    res = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    print("字符 | 频次")
    print("-"*15)
    for k,v in res:
        print(f"{repr(k):4} | {v}")

if __name__ == "__main__":
    text = input("请输入一段文本：")
    char_analysis(text)