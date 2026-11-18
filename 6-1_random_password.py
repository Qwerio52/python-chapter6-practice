# 6.1 随机密码生成
import random
import string

def generate_pwd():
    # 大小写字母 + 数字
    char_pool = string.ascii_letters + string.digits
    pwd = ''.join(random.choice(char_pool) for _ in range(8))
    return pwd

if __name__ == "__main__":
    print("生成10个8位随机密码：")
    for i in range(10):
        print(f"{i+1:2d}. {generate_pwd()}")