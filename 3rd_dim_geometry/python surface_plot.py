import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x와 y 값을 설정
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X * Y

# 3D 플롯 설정
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 곡면 그리기
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# 플롯 꾸미기
ax.set_title('$z = xy$ 곡면')
ax.set_xlabel('X 축')
ax.set_ylabel('Y 축')
ax.set_zlabel('Z 축')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# 그래프 출력
plt.show()
