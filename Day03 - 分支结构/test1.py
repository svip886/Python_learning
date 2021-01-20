# 英制单位英寸和公制单位厘米互换
# 1英寸=2.54厘米

l=float(input('请输入需要转换的长度：'))
unit=input('请输入单位：')
if unit=='in' or unit=='英寸':
    print('%.2f英寸 = %.2f厘米' % (l,l*2.54))
elif unit=='cm' or unit=='厘米':
    print('%.2f厘米 = %.2f英寸' % (l,l/2.54))
else:
    print('请输入正确的单位！')