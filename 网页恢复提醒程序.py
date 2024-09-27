try:
    import bs4,time,requests
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    import sys
    print('欢迎使用网站检查Python小程序')
    time.sleep(0.7)
    text1=input('请输入你需要Ping的网址(请以https://开头)')
    time.sleep(0.7)
    times=int(input('请输入ping的次数'))+1
    time.sleep(0.7)
    breaking=int(input('请输入间隔时间（单位为秒）'))
    time.sleep(0.7)
    to_addr = input('请输入你想要发送到的邮箱,以便通知您')
    #url='https://swzx.ctbu.edu.cn/bpm/rule?wf_num=R_S003_B036&wf_processid=d215908c0f6a1043dd09c310acbfd041dbe7&backUrl=https://swzx.ctbu.edu.cn/swzxm/#/'
    #以上为测试网址
    url=text1
    res=requests.get(url)
    i=int(1)
    from_addr = input('请输入您的邮箱\n目前仅支持QQ邮箱与163邮箱')
    password = input('请输入您的授权码\n可以在邮箱的Smtp服务中找到')
    if 'qq'in from_addr:
        smtp_server = 'smtp.qq.com'# 发信服务器
    if '163' in from_addr:
        smtp_server = 'smtp.163.com'# 发信服务器


    while i < times :#开始ping网页
        print(res)
        time.sleep(breaking)
        i=i+1
        if '20' in str(res):
        #这里想要判断返回的状态码 然后给用户发邮件通知 如果是20x那么网站可以访问
            server = smtplib.SMTP_SSL(smtp_server)
            server.connect(smtp_server,465)
            subject = '网页恢复通知'
            book=('您检查的网页已经回复，请立即查看\n'+url+'\n\n\n\n\n\n\——————————————————————————————————————————————您的Python网站可用监测器')
            msg = MIMEText(book,'plain','utf-8')# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
            msg['Subject'] = Header(subject, 'utf-8')
            server.login(from_addr, password)# 登录发信邮箱
            server.sendmail(from_addr, to_addr, msg.as_string())# 发送邮件
        try:
            print('邮件发送成功')
            server.quit()# 关闭服务器
        except:
            print('Error(⊙﹏⊙)\n邮件发送失败请重试')
        if i==times:#讲解返回码
            print('在程序完成后 你需要知道')
            time.sleep(1)
            print('[2xx]代表成功可以访问')
            time.sleep(1)
            print('[3xx]代表网站被重新定向')
            time.sleep(1)
            print('[4xx]代表客户端错误')
            time.sleep(1)
            print('[5xx]代表服务器出了点问题')
            time.sleep(1)
        if '20' not in str(res):
            choice=input('请问是否退出\n退出请输入0\n继续重复Ping网页请输入1\n' )
        if choice=='0':#是否反复ping网页
            print('程序已停止 请关闭窗口')
            time.sleep(0.8)
            print('感谢使用')
            break
        if choice=='1':
                i=1
except :
    print('程序结束 欢迎再次使用')
    time.sleep(1)
    print('如果你也喜欢编程 可以发邮件於我交流')
    time.sleep(1)
    print('程序结束 将于3秒后自动结束进程')
    time.sleep(2)
    print('再见')
    time.sleep(1)
    sys.exit()