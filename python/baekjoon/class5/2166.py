from math import inf
import sys

x_points = []
y_points = []

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))
    x_points.append(x)
    y_points.append(y)
x_points.append(x_points[0])
y_points.append(y_points[0])

det1, det2 = 0, 0
for i in range(n):
    det1 += x_points[i] * y_points[i+1]
    det2 += x_points[i+1] * y_points[i]

print(abs(det1-det2)/2)
    