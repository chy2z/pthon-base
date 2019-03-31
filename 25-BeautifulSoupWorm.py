# -*- coding:utf-8 -*-
"""
演示 爬虫 BeautifulSoup
# pip install BeautifulSoup4
"""
import re
from bs4 import BeautifulSoup

def printf(info,target=None):
    if target:
        print('%s---->%s' % (target, info))
    else:
        print('%s---->%s' % ('', info))

def formatHtml():
    # 格式化html代码
    printf(soup.prettify(), "格式化代码")

def selectByTagName(tagName):
    # 获取head信息
    header = soup.select(tagName)
    printf(type(header), "head类型")
    printf(header, "输出head")
    printf(header[0], "head[0]")
    printf(type(header[0]), "head[0]类型")
    printf(header[0].text, "head内容")

def selectA():
    alinks = soup.select('a')

    # 获取元素
    for x in alinks:
        printf(x.text,"标签A内容")
        printf(x['href'],"标签A链接")
        printf(x['myid'], "标签A自定义属性")

    # 获取元素的属性
    for x in alinks:
        for attr in x.attrs:
            printf(attr, "标签A属性")
            printf(x[attr], "标签A属性")

def selectByElementId():
    title = soup.select('#title')
    printf(type(title),"元素title类型")
    printf(title[0].text,"元素title文本")

def selectByElementClass():
    alinks = soup.select('.link')
    print([x.text for x in alinks])

def selectElementText():
    body = soup.select('body')[0]
    printf(body.text,"获取元素所有子元素文本")

def findByTagName():
    # 查找到的第一个满足条件的Tag
    element = soup.find('a')
    printf(element.text, "元素内容")
    printf(element.name, "元素名称")

    # 获取元素的属性
    for attr in element.attrs:
            printf(attr, "元素属性名称")
            printf(element[attr], "元素属性值")

def findByAttr():
    # 查找到的第一个满足条件的Tag
    element = soup.find(attrs={'class':'link','myid':'a2'})
    printf(element.text, "元素内容")
    printf(element.name, "元素名称")

    # 获取元素的属性
    for attr in element.attrs:
        printf(attr, "元素属性名称")
        printf(element[attr], "元素属性值")

def findByRe():
    # 查找到的第一个满足条件的Tag
    element = soup.find('a',attrs={'class': 'link','my-attr':re.compile(r'\d+\w+')})
    printf(element.text, "元素内容")
    printf(element.name, "元素名称")

    # 获取元素的属性
    for attr in element.attrs:
        printf(attr, "元素属性名称")
        printf(element[attr], "元素属性值")

def findChild():
    element= soup.find('p').find('a')
    printf(element,"超找子元素")

"""
find 和 find_all 用法一样
find 返回的是第一个tag
find_all 返回是tag列表
"""
def find_All_TagName():
    # 查找到的所有满足条件的Tag
    elements = soup.find_all('a')

    for element in elements:
        printf(element.text, "元素内容")
        printf(element.name, "元素名称")

    # 获取元素的属性
    for element in elements:
       for attr in element.attrs:
            printf(attr, "元素属性名称")
            printf(element[attr], "元素属性值")

if __name__ == '__main__':
  html = '''
  <html>
    <body>
          <h1 id="title">Hello World</h1>
          <p id="p1">
          <a href="www.baidu.com" myid='a1' my-attr="abc" class="link">百度</a>
          <a href="www.sina.com" myid='a2' my-attr="123abc" class="link">新浪</a>          
          </p>
    </body>
  </html>
  '''
  # 这里指定解析器为html.parser（python默认的解析器）
  soup = BeautifulSoup(html,'html.parser')
  #formatHtml()
  #selectByTagName("h1")
  #selectA()
  #selectByElementId()
  #selectByElementClass()
  #selectElementText()
  #findByTagName()
  #findChild()
  #findByAttr()
  #findByRe()
  find_All_TagName()