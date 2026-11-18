# 6.2 重复元素判定（遍历版本）
def has_duplicate(lst):
    temp = []
    for item in lst:
        if item in temp:
            return True
        temp.append(item)
    return False

if __name__ == "__main__":
    test1 = [1,2,3,4,5]
    test2 = [1,2,3,2,5]
    print(f"{test1} 是否有重复：{has_duplicate(test1)}")
    print(f"{test2} 是否有重复：{has_duplicate(test2)}")