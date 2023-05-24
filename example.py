# 创建 NotionExporter 实例
import os

from notion2vuepress import NotionExporter

exporter = NotionExporter(
    # token_v2
    _token='v02%3Auser_token_or_cookies%3AQ66-cNX8yXEK-jzADJY-Ho_NxYr82y2kXfniQU6zC1pXNfP11XPuIooLT-EsjDPlgTyvHuSxj575Om0OhSIx0oRd5YYep9UPqDhhTqPxbLQqrGqw7HzKG0aNeSnG8K-2gLGP',
    # 图片Cookie
    img_token='1%3AvljdZQ4YXmhwbh1RQcqbgsj_PtuU0FGAplMDnOC_1vY%3Af9502cfb689b275d22efa623be36895db52c50c567d9b760%3A50ddbcb1-ae33-4542-aaae-7308f5c3bdb8',
)

# https://www.notion.so/youyizhang/d9c4e3199aad4c60a816ace1df4e6477?pvs=4
page_url = 'd9c4e3199aad4c60a816ace1df4e6477'
file_path = os.getcwd()
# page_url: 文件id
# file_path: 文件下载位置
exporter.export_to_markdown(page_url, file_path)
