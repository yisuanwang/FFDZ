
# (1231, '18岁什么化妆品都不用，28岁什么化妆品都没用。', '27'),
# 把nows.fun的数据库数据转换成php array格式
def write_(str):
    file_name = 't.txt'
    with open(file_name, 'a',encoding='utf-8') as file_obj:
        file_obj.write(str)

for i in range(0,1230):
    str=input("a:")
    str=str[:len(str)-1].split(',')
    write_('\"'+str[1].replace('\'','')+"\",\n")
    # print(str[1].replace('\'',''))
    pass

