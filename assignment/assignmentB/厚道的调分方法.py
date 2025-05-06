points = list(map(float, input().split()))
points.sort()
min_point = points[int(len(points)*0.4)]
def new_point(b):
    return min_point*b/1000000000 + 1.1**(min_point*b/1000000000)

left, right = 0, 1000000000
while left < right:
    mid = (left+right)//2
    if new_point(mid) < 85:
        left = mid+1
    else:
        right = mid
print(right)
