# import requests
#
# url = 'https://mynizhyn.com/image/news_small/2023/02/13_100541_news2_411bd6062bc40de78fc9eaf63186f7c7-1.jpg'
#
# response = requests.get(url)
# print(response.content)
# print(response.text)
#
# with open('spring.jpg', mode='wb') as file:
#     file.write(response.content)
#
# url2 = 'https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.2/Git-2.42.0.2-32-bit.exe'
#
# with open('ins.exe', mode='wb') as file:
#     file.write(requests.get(url2).content)
#
# url3 = 'https://github.com/progit/progit2/releases/download/2.1.408/progit.pdf'
#
# with open('tutorial.pdf', mode='wb') as file:
#     file.write(requests.get(url3).content)

with open('spring.jpg', mode='rb') as file:
    print(file.read())
