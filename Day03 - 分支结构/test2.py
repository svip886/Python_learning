# 百分制成绩转换为等级制成绩
# A:score≥90|B:80≤score<90|C:70≤score<80|D：60≤score<70|E：score<60

score=float(input('输入分数：'))
if score>=0 and score<=100: # 判断输入是否符合百分制
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='E'
    print('该分数等级为:',grade)
else:
    print('分数输入错误，请重新输入！')