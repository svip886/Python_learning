# 打印三角形

row=int(input('请输入行数:'))
# 右三角形
for n in range(1,row+1):
    for x in range(n): 
        print('*',end='')
    print()
# 左三角形
for n in range(1,row+1):
    for x in range(row,0,-1):
        if x>n:
            print(' ',end='')
        else:
            print('*',end='')
    print()
# 两边三角形
for n in range(1,row+1):
    for x in range(row,n,-1):
            print(' ',end='')
    for y in range(1,2*n):
            print('*',end='')
    print()