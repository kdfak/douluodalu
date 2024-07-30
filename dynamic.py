import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://dl.131437.xyz/book/douluodalu1/1.html'

while url:
    # 伪装自己
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    # 发送请求
    resp = requests.get(url, headers=headers)
    # 设置编码
    resp.encoding = 'utf-8'

    # 解析页面
    e = etree.HTML(resp.text)

    # 使用 BeautifulSoup 进行更好地处理
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 提取文本
    info = soup.select_one('.entry-text .m-post').get_text(separator='\n', strip=True)

    # 提取标题
    title = soup.select_one('div h1').get_text(strip=True)

    print(title, "\n")

    # 保存到文件
    with open("D:\\pythonwork\\pythonProject\\斗罗大陆.txt", 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')

    # 更新 URL
    href_list = e.xpath('//tr/td[2]/a/@href')
    if href_list:
        url = f'https://dl.131437.xyz{href_list[0]}'
    else:
        print("No href found in the XPath query.")
        url = None  # Or handle the error as needed
