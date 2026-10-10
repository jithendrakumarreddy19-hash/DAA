
# Closest Pair of Points - Brute Force

import math

points = [(1, 2), (4, 6), (5, 3), (2, 3)]

min_dist = float('inf')
closest_pair = None

for i in range(len(points)):
    for j in range(i + 1, len(points)):

        x1, y1 = points[i]
        x2, y2 = points[j]

        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        if dist < min_dist:
            min_dist = dist
            closest_pair = (points[i], points[j])

print("Closest Pair:", closest_pair)
print("Minimum Distance:", round(min_dist, 2))
