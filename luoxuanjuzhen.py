m, n = map(int, input("请输入两个整数，以空格分隔: ").split(' '))
arr = []
for i in range(m):
    arr_n = list(map(int,input(f"请输入第{i+1}行:").split(' ')))
    arr.append(arr_n)

re_arr = []
left, right, top, bottom = 0, n - 1, 0, m - 1
while left <= right and top <= bottom:
    # 从左到右打印上边
    for j in range(left, right + 1):
        re_arr.append(arr[top][j])
    top += 1
    if top > bottom:
        break
    # 从上到下打印右边
    for i in range(top, bottom + 1):
        re_arr.append(arr[i][right])
    right -= 1
    if left > right:
        break
    # 从右到左打印下边
    for j in range(right, left - 1, -1):
        re_arr.append(arr[bottom][j])
    bottom -= 1
    if top > bottom:
        break
    # 从下到上打印左边
    for i in range(bottom, top - 1, -1):
        re_arr.append(arr[i][left])
    left += 1
print("顺时针输出矩阵的元素:", re_arr)
