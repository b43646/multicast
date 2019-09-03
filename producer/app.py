#coding:utf-8,
import socket 
import time

ANY = '0.0.0.0'
SENDERPORT=31501 
MCAST_ADDR = '224.168.2.9'
MCAST_PORT = 36000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) 
sock.bind((ANY,SENDERPORT)) #绑定发送端口到SENDERPORT，即此例的发送端口为1501
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255) #设置使用多播发送
while 1: 
    time.sleep(10)
    sock.sendto('Hello World', (MCAST_ADDR,MCAST_PORT) ); #将'hello world'发送到多播地址的指定端口，属于这个多播组的成员都可以收到这个信息
