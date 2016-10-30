import asyncore
import socket


class AsyncGet(asyncore.dispatcher):
    def __init__(self, host):
        asyncore.dispatcher.__init__(self)
        self.host = host
        # 创建Socket对象
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 80))  # 连接服务器
        self.request = b'GET /  HTTP/1.0\r\n\r\n'  # 请求index.html页面
        self.outf = None
        print('请求的地址来自：', host)

    def handle_connect(self):
        print('连接：', self.host)

    def handle_read(self):
        if not self.outf:
            print('正在创建连接：：', self.host)
        self.outf = open('%s.txt' % self.host, 'wb')  # 将服务器信息写入记事本中
        data = self.recv(8192)  # 获取服务器发送过来的信息
        if data:
            self.outf.write(data)  # 写入记事本中

    def writeable(self):
        return len(self.request) > 0

    def handle_write(self):
        num_sent = self.send(self.request)  # 发送客户端请求

    def handle_close(self):
        asyncore.dispatcher.close(self)
        print('Socket对象关闭于：', self.host)
        if self.outf:
            self.outf.close()


if __name__ == '__main__':
    AsyncGet('www.nankai.edu.cn')
    asyncore.loop()


