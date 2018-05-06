import hashlib
import os
import sys

#/////////////////////////////#
# Message :
#			Tolong Jangan Recode
#			Kalo Mau Recode Izin
#			Dulu Sama Author
# Kontak Author -》 facebook.com/ardi.muhammad.35574406
# Gmail Author  -》 mrsuardi4@gmail.com
#/////////////////////////////#

Limpar = "clear"

def Makassar():
		os.system(Limpar)
		print("""\033[1;36m
   ------------------------------------
  |-| \033[1;31mTools  》 HashCode              \033[1;36m|-|
  |-| \033[1;31mAuthor 》 Mr.Ardi               \033[1;36m|-|
  |-| \033[1;31mGithub 》 github.com/ardisql/   \033[1;36m|-|
   ------------------------------------
""")

def Mks(frase, call):
		Ardi1 = input(frase)
		if Ardi1 == "y":
				call()
		if Ardi1 == "m":
				Escolha()
		else:
				Mks(frase,call)
				
def Escolha():
		Makassar()
		print("""\033[1;36m
     A) Hash   》 MD5
     B) Hash   》 Sha1
     C) Hash   》 Sha224
     D) Hash   》 Sha256
     E) Hash   》 Sha384
     F) Hash   》 Sha512
     X) Keluar 》 Exit
""")
		Ardi1 = input("[Menu] - 》》")
		if Ardi1 == "A" or Ardi1 == "a":
				Md5()
		if Ardi1 == "B" or Ardi1 == "b":
				Sha1()
		if Ardi1 == "C" or Ardi1 == "c":
				Sha224()
		if Ardi1 == "D" or Ardi1 == "d":
				Sha256()
		if Ardi1 == "E" or Ardi1 == "e":
				Sha384()
		if Ardi1 == "F" or Ardi1 == "f":
				Sha512()
		if Ardi1 == "X" or Ardi == "x":
				os.system("killall -9 com.termux")
		else:
				Escolha()
				
def Md5():
		Makassar()
		Sundala00 = input("[ Md5 ] - 》》 ")
		md5 = hashlib.md5(Sundala00.encode())
		print (md5.hexdigest())
		Mks("Ulangi Hash Md5 / Back Menu (y/m) ",Md5)
		
def Sha1():
		Makassar()
		Sundala01 = input("[ Sha1 ] - 》》")
		sha1 = hashlib.sha1(Sundala01.encode())
		print(sha1.hexdigest())
		Mks("Ulangi Hash Sha1 / Back Menu (y/m) ",Sha1)
		
def Sha224():
		Makassar()
		Sundala02 = input("[Sha224] - 》》")
		sha224 = hashlib.sha224(Sundala02.encode())
		print(sha224.hexdigest())
		Mks("Ulangi Hash Sha224 / Back Menu (y/m) ",Sha224)
		
def Sha256():
		Makassar()
		Sundala03 = input("[Sha256] - 》》")
		sha256 = hashlib.sha256(Sundala03.encode())
		print(sha256.hexdigest())
		Mks("Ulangi Hash Sha256 / Back Menu (y/m) ",Sha256)
		
def Sha384():
		Makassar()
		Sundala04 = input("[Sha384] - 》》")
		sha384 = hashlib.sha384(Sundala04.encode())
		print(sha384.hexdigest())
		Mks("Ulangi Hash284 / Back Menu (y/m) ",Sha384)
		
def Sha512():
		Makassar()
		Sundala05= input("[Sha512] - 》》")
		sha512 = hashlib.sha512(Sundala05.encode())
		print(sha512.hexdigest())
		Mks("Ulangi Hash512 / Back Menu (y/m) ",Sha512)
		
		
Escolha()