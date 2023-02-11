# -*- coding: utf-8 -*-
import socket
import sys

# 正引き
def foward_lookup(domain):
	try:
		return socket.gethostbyname(domain)
	except:
		return False

# 逆引き
def reverse_lookup(ip):
	try:
		return socket.gethostbyaddr(ip)[0]
	except:
		return False

if __name__ == "__main__":
	f = open("./ip.txt")# ファイルの読み込み
	for host in f:
		host = host.replace("\n","")
                # 正引き
		ip = foward_lookup(host)
		print(ip)
                # 逆引き
				#
		#domain = reverse_lookup(host)
		#print domain
	f.close()