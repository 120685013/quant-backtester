from metrics import calc_information_ratio


# 1. 正常情况
excess_returns = [
    0.01, 0.02, -0.01, 0.015, 0.005,
    0.012, -0.005, 0.018, 0.007, 0.011,
    -0.003, 0.014, 0.006, 0.009, 0.013,
    -0.002, 0.016, 0.008, 0.004, 0.010
]

print("normal:", calc_information_ratio(excess_returns))


# 2. 样本不足
short_returns = [0.01] * 10

print("too few samples:", calc_information_ratio(short_returns))


# 3. std = 0
stable_returns = [0.01] * 20

print("zero std:", calc_information_ratio(stable_returns))