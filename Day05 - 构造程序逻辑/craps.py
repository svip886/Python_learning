"""
骰子游戏。
游戏规则：玩家投2个骰子
    第一次摇到7、11点，玩家胜
    第一次摇到2、3、12点，庄家胜
    其他点数继续摇，摇到7点，庄家胜，摇到第一次的点数，玩家胜
    直至分出胜负。
"""
from random import randint
money=1000 # 初始金额
while money>0:
    print('当前资产为%d元' % (money))
    while True:
        x=int(input('请下注：'))
        if x>0 and x<=money:
            print('游戏开始！')
            break
        else:
            print('下注金额不在可用金额范围内，请重新输入！')
    input('按回车键开始摇骰子')
    first=randint(1,6)+randint(1,6)
    print('你摇出了%d点' % (first))
    if first==7 or first==11:
        print('你赢了！')
        money+=x
    elif first==2 or first==3 or first==12:
        print('你输了！')
        money-=x
    else:
        while True:
            input('按回车键开始摇骰子')
            again=randint(1,6)+randint(1,6)
            print('你摇出了%d点' % (again))
            if again==first:
                print('你赢了！')
                money+=x
                break
            elif again==7:
                print('你输了！')
                money-=x
                break
            else:
                print('再来一次') 
print('你没钱了，输的只剩一条内裤~')
