m, n = map(int, input("请输入两个整数，以空格分隔: ").split(' '))
arr = []
for i in range(m):
    arr_n = list(map(int,input(f"请输入第{i+1}行:").split(' ')))
    arr.append(arr_n)

def yidong(path,i,j):
    if(path==0):
        i = i + arr[i][j]
    if(path==1):
        i = i - arr[i][j]
    if(path==2):
        j = j + arr[i][j]
    if(path==3):
        j = j - arr[i][j]
    return i,j

# 用于记录已经访问过的位置以及到达该位置的最短步数
visited = {}
# 将起始位置 (0, 0) 的步数设为0，并加入已访问记录，前驱位置设为None
visited[(0, 0)] = (0, None)
# 队列中的元素为 (i, j, steps)，分别表示当前位置的行、列和到达该位置的步数
queue = [(0, 0, 0)]


def shortest_path_iterative():
    while queue:
        i, j, steps = queue.pop(0)
        print(f"起始位置:{i+1},{j+1}")

        if (i, j) == (m - 1, n - 1):
            # 找到目标位置，构建最短路线
            path = []
            current_pos = (i, j)
            while current_pos!= (0, 0):
                path.append(current_pos)
                current_pos = visited[current_pos][1]
            path.append((0, 0))
            path.reverse()
            return steps, path

        for path in range(4):
            new_i, new_j = yidong(path, i, j)

            if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                visited[(new_i, new_j)] = (steps + 1, (i, j))
                queue.append((new_i, new_j, steps + 1))
                print(f"可以到达位置:{new_i+1},{new_j+1},花费{steps + 1}步")
                print(visited)


    return -1, []


shortest_steps, shortest_path = shortest_path_iterative()
if shortest_steps == -1:
    print("无法到达目标位置！")
else:
    print(f"最短步数：{shortest_steps}")
    print("最短路线：", shortest_path)

