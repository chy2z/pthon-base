"""
# 实现一个简单的爬虫
"""
import urllib
import urllib.request
import re
import os


# 根据url获取网页html内容
def getHtmlContent(url):
    '''
      user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
      headers = {'User-Agent': user_agent}
    '''
    page = urllib.request.urlopen(url)
    return page.read().decode('utf-8')


# 从html中解析出所有jpg图片的url
# 图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # h='<img src="https://pic3.zhimg.com/80/9dc11ec6df61a0ede08bf63a38b31402_hd.jpg" >'
    # h='<div><a class="UserLink-link" data-za-detail-view-element_name="User" target="_blank" href="//www.zhihu.com/people/pythonpeixun" data-reactid="194"><img class="Avatar AuthorInfo-avatar" width="38" height="38" src="https://pic3.zhimg.com/ece4a48c051c804668ffb59409d2ad49_xs.jpg" srcset="https://pic3.zhimg.com/ece4a48c051c804668ffb59409d2ad49_l.jpg 2x" alt="黄哥" data-reactid="195"/></a></div>'

    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)".+?>')

    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg,html)

    print(" 图片数量: " +str(len(jpgs)))

    return jpgs

# 将html内容输出到文件
def outPutFile(html):
    path="./worm/html/"
    # 新建文件夹
    if not os.path.exists(path):
        os.mkdir(path)
    f = open(path+"a.txt", "w+", encoding='utf-8')
    f.write(html)
    f.close()

# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    urllib.request.urlretrieve(imgUrl, fileName)


# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls, path='./worm/imgs/'):
    # 新建文件夹
    if not os.path.exists(path):
        os.mkdir(path)

    # 用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print('正在下载：%s %s' % (count,url))
        count = count + 1


# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    outPutFile(html)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)


def main():
    url = 'http://blog.csdn.net/lenovo403/article/details/50721609'
    download(url)


if __name__ == '__main__':
    main()