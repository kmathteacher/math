import numpy as np
import matplotlib.pyplot as plt

# 복소수 평면 설정
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# 함수 f(z) = 1/sin(z)
def f(z):
    return 1 / np.sin(z)

# 수렴 영역을 나타내기 위해 함수값의 절대값을 계산
W = f(Z)

# 플롯 설정
plt.figure(figsize=(8, 8))
plt.imshow(np.abs(W), extent=[-10, 10, -10, 10], origin='lower', cmap='inferno', norm=plt.Normalize(vmin=0, vmax=5))
plt.colorbar(label='|1/sin(z)|')
plt.title('Convergence region of $f(z) = 1/\sin(z)$ in the complex plane')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
