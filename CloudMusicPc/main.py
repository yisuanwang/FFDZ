# @Time    : 2020/1/24
# @Author  : yisuanwang
#抓取歌曲下面的评论，music_list是挑选过后的歌单
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
from multiprocessing import Pool

music_list=["1433338551","1456706488"]#,"1477539203","1481164987","1449990499","1463503505","1294910785","1450630238","1435449062","1370047789","553755659","465921195","28018075","445665094","1425626819","29004400","407450223","1436709403","1426112587","1398663411","1382596189","1349292048","1328146041","27890306","1357825630","1383876635","25706282","1350202699","516076896","514761281","554989668","1374056687","523251118"]
musicid = "1433338551"
id=1230

def get_response(offset,limit):
    #参数
    para = {
        'offset':offset,#页数
        'limit':limit#总数限制
    }
    # 歌曲id
    global musicid
    #歌曲api地址
    musicurl = "http://music.163.com/api/v1/resource/comments/R_SO_4_"+musicid+"?"+urlencode(para)
    #头结构
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'vjuids=-13ac1c39b.1620457fd8f.0.074295280a4d9; vjlast=1520491298.1520491298.30; _ntes_nnid=3b6a8927fa622b80507863f45a3ace05,1520491298273; _ntes_nuid=3b6a8927fa622b80507863f45a3ace05; vinfo_n_f_l_n3=054cb7c136982ebc.1.0.1520491298299.0.1520491319539; __utma=94650624.1983697143.1521098920.1521794858.1522041716.3; __utmz=94650624.1521794858.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=FYtmJTTpVwmbihVrUad6u76CKxuzXZnfYyPZfK9bi%5CarU936rIdoIiVU50pfQ6JwjGgBvSyZO0%2FR%2BcoboKdPuMztgHCJwzyIgx1ON4v%2BJ2mOvARluNGpRo6lmhA%5CfcfCd3EwdS88sPgxpiiXN%5C6HZZEMQdNRSaHJlcN%5CXY657Faklqdh%3A1522053962445; _iuqxldmzr_=32',
        'Host':'music.163.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    #代理IP
    proxies= {
        'http:':'http://121.232.146.184',
        'https:':'https://144.255.48.197'
    }
    try:
        response = requests.post(musicurl,headers=headers,proxies=proxies)
        if response.status_code == 200:
            return response.content
    except RequestException:
        print("访问出错")

# 评论写入文件
def write_(str):
    file_name = 't.txt'
    with open(file_name, 'a',encoding='gbk') as file_obj:
        file_obj.write(str.encode("gbk", 'ignore').decode("gbk", "ignore"))
#解析返回页
def parse_return(html):
    global id
    data = json.loads(html)#将返回的值格式化为json
    if data.get('hotComments'):
        hotcomm = data['hotComments']
        print('--------------------------------------------------------------这是热门评论-------------------------------------------------------------------------------')
        # 热门评论
        for hotitem in hotcomm:
            hotdata = hotitem['content']
            len_=len(hotdata)
            # strrr='('+str(id)+', \''+hotdata+'\',\''+str(len_)+'\'),'
            strrr = '\"'+ hotdata + '\",'
            strrr=strrr.replace('\n','\\n').replace('\r','||r')
            strrr.encode('GBK', 'ignore').decode('GBk')
            write_(strrr+'\n')
            # print(strrr)
            id+=1
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
    else:
        print('--------------------------------------------------')
    if data.get('comments'):
        comm = data['comments']
        for item in comm:
            hotdata = item['content']
            len_ = len(hotdata)
            # 这里用来获取指定长度的普通评论
            if len_>159 or len_<20:
                continue
                pass
            strrr = '\"' + hotdata + '\",'
            strrr = strrr.replace('\n', '\\n').replace('\r', '||r')
            strrr.encode('GBK', 'ignore').decode('GBk')
            write_(strrr + '\n')
            # print(data)
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
def main(offset):
    for i in music_list:
        global musicid
        musicid=i
        gethtml = get_response(offset,200)
        parse_return(gethtml)
        pass

if __name__ == '__main__':
    groups = [x*20 for x in range(0,20)]
    pool = Pool()
    pool.map(main,groups)
    for x in range(0,20):
        main(x*20)