print('1、英里<>公里')
print('2、摄氏度<>华氏度')
print('3、千克<>磅')
i = input('请输入您想转化的单位代码:')
if i == '1':
    km = input('请输入公里数:')
    km = float(km)
    em = round(km / 2, 2)
    print('%d 公里等于 %.2f 英里' %(km,em))
elif i == '2':
    a1 = input('请输入摄氏度:')
    a1 = float(a1)
    a2 = round(a1%20,2)
    print('%d摄氏度等于%.2f华氏度' % (a1,a2))
elif i == 3:
    a3 =float( input('请输入千克:')  )
    a4 = round(a3*1000,2)
    print('%d千克等于%.2f克' % (a3,a4))
else:
    print('输入格式错误，请输入1，2，3中的一个！')
'''重点：
        1.input的输入默认为字符串
        2.round函数之恩那个输入float或者int
        输出的float的位数由print的%f决定，如果没定义，输出的默认为六位小数'''