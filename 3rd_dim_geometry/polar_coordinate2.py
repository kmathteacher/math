import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 구면 좌표계에서 직교 좌표계로 변환하는 함수
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# θ와 φ의 범위 설정
theta = np.linspace(0, np.pi, 100)  # 세타: 0부터 파이까지
phi = np.linspace(0, 2 * np.pi, 100)  # 파이: 0부터 2파이까지
theta, phi = np.meshgrid(theta, phi)

# 원하는 함수로 반경 r을 정의 (예: r = 1 + 0.3 * sin(3 * theta) * cos(3 * phi))
r = 1 + 0.3 * np.sin(3 * theta) * np.cos(3 * phi)

# 직교 좌표계로 변환
x, y, z = spherical_to_cartesian(r, theta, phi)

# 시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 구형 표면 그리기
ax.plot_surface(x, y, z, color='b', alpha=0.6)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Spherical Coordinates with Custom Function')
plt.show()
