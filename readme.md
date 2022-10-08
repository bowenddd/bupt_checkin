# 北邮“半自动”健康打卡脚本

## Info
北邮半自动健康打卡脚本，使用python+selenium实现

## Environment

- macos 11.3
- python 3.8.12
- selenium 3.141.0

## QuickStart

1. 将checkin.py文件克隆到本地
2. 安装selenium包
3. 启动safari driver
命令行输入以下命令
    ```
    safaridriver --enable
    ```
4. 填入checkin.py文件中第9行和第10行中的学号和密码(与登陆信息门户一致)

5. 命令行输入以下命令启动打卡
    ```
    python checkin.py
    ```