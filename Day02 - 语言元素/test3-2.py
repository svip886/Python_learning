year=int(input('输入年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    print('该年为闰年')
else:
    print('不是闰年')