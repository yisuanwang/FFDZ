# https://music.163.com/song?id=1481164987&userid=1756052009
# https://music.163.com/song?id=1449990499&userid=1756052009
# https://music.163.com/song?id=1463503505&userid=1756052009
# https://music.163.com/song?id=1294910785&userid=1756052009
# https://music.163.com/song?id=1450630238&userid=1756052009
# https://music.163.com/song?id=1435449062&userid=1756052009
# https://music.163.com/song?id=1370047789&userid=1756052009
# https://music.163.com/song?id=553755659&userid=1756052009
# https://music.163.com/song?id=465921195&userid=1756052009
# https://music.163.com/song?id=28018075&userid=1756052009
# https://music.163.com/song?id=445665094&userid=1756052009
# https://music.163.com/song?id=1425626819&userid=1756052009
# https://music.163.com/song?id=29004400&userid=1756052009
# https://music.163.com/song?id=407450223&userid=1756052009
# https://music.163.com/song?id=1436709403&userid=1756052009
# https://music.163.com/song?id=1426112587&userid=1756052009
# https://music.163.com/song?id=1398663411&userid=1756052009
# https://music.163.com/song?id=1382596189&userid=1756052009
# https://music.163.com/song?id=1349292048&userid=1756052009
# https://music.163.com/song?id=1328146041&userid=1756052009
# https://music.163.com/song?id=27890306&userid=1756052009
# https://music.163.com/song?id=1357825630&userid=1756052009
# https://music.163.com/song?id=1383876635&userid=1756052009
# https://music.163.com/song?id=25706282&userid=1756052009
# https://music.163.com/song?id=1350202699&userid=1756052009
# https://music.163.com/song?id=516076896&userid=1756052009
# https://music.163.com/song?id=514761281&userid=1756052009
# https://music.163.com/song?id=554989668&userid=1756052009
# https://music.163.com/song?id=1374056687&userid=1756052009
# https://music.163.com/song?id=523251118&userid=1756052009

from urllib.parse import parse_qsl,urlparse
import urllib.request


# 上面是歌曲的复制链接，这里将链接转换为main.py中的music_list，再把它复制带main里面

strt=''
for i in range(30):
    str=input('输入：')
    strt+='\"{}\",'.format(parse_qsl(urlparse(str).query)[0][1])

print(strt)