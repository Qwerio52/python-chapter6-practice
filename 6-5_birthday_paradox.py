# 6.5 生日悖论模拟
import random

def birthday_simulate(people=23, trial=10000):
    hit = 0
    for _ in range(trial):
        birthdays = set()
        same = False
        for _ in range(people):
            b = random.randint(1,365)
            if b in birthdays:
                same = True
                break
            birthdays.add(b)
        if same:
            hit +=1
    prob = hit / trial
    return prob

if __name__ == "__main__":
    for times in [100, 1000, 5000, 10000]:
        p = birthday_simulate(23, trial=times)
        print(f"样本量 {times:5d} 次，23人同生日概率：{p:.4f}")