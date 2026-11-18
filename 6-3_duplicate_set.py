# 6.3 重复元素判定（集合版本）
def has_duplicate_set(lst):
    # 集合自动去重，长度对比
    return len(set(lst)) != len(lst)

if __name__ == "__main__":
    test1 = [1,2,3,4,5]
    test2 = [1,2,3,2,5]
    print(f"{test1} 是否有重复：{has_duplicate_set(test1)}")
    print(f"{test2} 是否有重复：{has_duplicate_set(test2)}")