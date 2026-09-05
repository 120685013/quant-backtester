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

from metrics import calc_downside_deviation, calc_sortino_ratio


# downside deviation 正常情况
returns = [0.02, -0.01, 0.03, -0.02]
print("downside deviation:", calc_downside_deviation(returns))

# Sortino 正常情况
print("sortino:", calc_sortino_ratio(returns))

# 全部高于 target，downside deviation 理论上为 0
positive_returns = [0.01, 0.02, 0.03, 0.04]
print("sortino no downside:", calc_sortino_ratio(positive_returns))

# 空列表
print("sortino empty:", calc_sortino_ratio([]))