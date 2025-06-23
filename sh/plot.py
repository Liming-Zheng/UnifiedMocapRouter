import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件（替换为你自己的文件名）
df = pd.read_csv('new_rubber_2.csv')  # ← 替换成你的文件名，比如 'output.csv'

# 时间转换为秒（从起始时间戳归零）
df['time_s'] = (df['timestamp[us]'] - df['timestamp[us]'].iloc[0]) / 1e6

# 转换为 NumPy array，防止 matplotlib 和 pandas 不兼容
time = df['time_s'].to_numpy()
x = df['x[m]'].to_numpy()
y = df['y[m]'].to_numpy()
z = df['z[m]'].to_numpy()
vx = df['vx[m/s]'].to_numpy()
vy = df['vy[m/s]'].to_numpy()
vz = df['vz[m/s]'].to_numpy()

# ===== 位置图 =====
plt.figure()
plt.plot(time, x, label='x [m]')
plt.plot(time, y, label='y [m]')
plt.plot(time, z, label='z [m]')
plt.xlabel('Time [s]')
plt.ylim([-10, 10])  # 设置y轴范围
# plt.xlim([0, time[-1]])  # 设置x轴范围
plt.ylabel('Position [m]')
plt.title('Position over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()

# ===== 速度图 =====
plt.figure()
plt.plot(time, vx, label='vx [m/s]')
plt.plot(time, vy, label='vy [m/s]')
plt.plot(time, vz, label='vz [m/s]')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.ylim([-10, 10])  # 设置y轴范围
plt.title('Velocity over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
