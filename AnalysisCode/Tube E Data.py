import numpy as np

a = 1660
n = 1
n2 = 2
theta_zero = 237.4
x = np.array([ 224, 223.6, 223.3, 222.3, 222, 221.2, 220.4, 220.1, 220, 217, 216.8, 214, 212.7
    
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
save_path = '/Users/hall5jj/Desktop/PHY277/EXP3/Tube E Data.txt'

with open(save_path, 'w') as f:
    f.write(f"{'Index':<10}{'Theta Diff (deg)':<20}{'Lambda':<20}\n")
    f.write(f"{'-'*50}\n")
    for idx, (t, l) in enumerate(zip(theta_diff, lamb), start=1):
        f.write(f"{idx:<10}{t:<20.6f}{l:<20.6f}\n")

n2theta_diff = []
for xi in x:
    if xi == 0:
        n2theta_diff.append(np.nan)
    else:
        n2diff = (theta_zero - xi)
        n2theta_diff.append(diff)

print("n2 Theta Values: ", n2theta_diff)

n2lamb = a * np.sin(np.deg2rad(n2theta_diff)) / n2

print("n2 Lambda: ", n2lamb)

# Set the full file path
save_path2 = '/Users/hall5jj/Desktop/PHY277/EXP3/Tube E n2 Data.txt'

with open(save_path2, 'w') as f:
    f.write(f"{'Index':<10}{'n2 Theta Diff (deg)':<20}{'n2 Lambda':<20}\n")
    f.write(f"{'-'*50}\n")
    for idx, (t, l) in enumerate(zip(n2theta_diff, n2lamb), start=1):
        f.write(f"{idx:<10}{t:<20.6f}{l:<20.6f}\n")

