import numpy as np

a = 1660
n = 1
theta_zero = 237.4
x = np.array([
    223.5, 223.4, 223.1, 222.9, 222.7, 222.4, 222.1, 221.8, 221.6, 221.4,
    221.1, 220.7, 220.4, 220.1, 219.8, 219.4, 218.7, 218.4, 217.4, 217.2,
    217, 216.8, 216.7, 216.5, 216.4, 216, 215.9, 215.6, 215.4, 215.1,
    214.8, 214.6, 214.2, 213.9
])

theta_diff = []
for xi in x:
    if xi == 0:
        theta_diff.append(np.nan)
    else:
        diff = (theta_zero - xi)
        theta_diff.append(diff)

print("Theta Values: ", theta_diff)

lamb = a * np.sin(np.deg2rad(theta_diff)) / n

print("Lambda: ", lamb)

# Set the full file path
save_path = '/Users/hall5jj/Desktop/PHY277/EXP3/Tube C Data.txt'

with open(save_path, 'w') as f:
    f.write(f"{'Index':<10}{'Theta Diff (deg)':<20}{'Lambda':<20}\n")
    f.write(f"{'-'*50}\n")
    for idx, (t, l) in enumerate(zip(theta_diff, lamb), start=1):
        f.write(f"{idx:<10}{t:<20.6f}{l:<20.6f}\n")
