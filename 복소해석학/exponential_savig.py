#f(z) = e^(iz)를 html로 만들 수 있는 코드

import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

# z 값을 위한 범위 설정 (실수)
z_values = np.linspace(-10, 10, 400)

# f(z) = e^(iz) 계산
f_z = np.exp(1j * z_values)

# 실수부와 허수부 분리
x = z_values
y = np.real(f_z)
z = np.imag(f_z)

# 3D 그래프 생성
trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', name='f(z) = e^(iz)')
layout = go.Layout(
    title='3D Plot of f(z) = e^(iz)',
    scene=dict(
        xaxis_title='z (Real part)',
        yaxis_title='Re(f(z))',
        zaxis_title='Im(f(z))'
    )
)
fig = go.Figure(data=[trace], layout=layout)

# 그래프 저장 (interactive HTML 파일로 저장)
pyo.plot(fig, filename='3d_plot.html')
