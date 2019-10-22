import os
import subprocess
import crypt

os.system("tput setaf 1")
print("\t\tWelcome to my tools")
os.system("tput setaf 0")
print("\t\t---------------")


print("""
Press 1: to live stream
Press 2: to check cal
Press 3: to create user
Press 4: to create file
Press 5: to exit from this tools
""")

print("enter your choice : ", end='')
ch = input()
print(ch)

if int(ch) == 1:
	print("Enter IP address of host")
	RemoteIp=input()
	subprocess.getstatusoutput("scp /root/pythoncode/live.py "+RemoteIp+":/root/Desktop/" )
	subprocess.getstatusoutput("ssh -X "+RemoteIp+" python36 /root/Desktop/live.py")
elif int(ch) == 2:
	os.system("cal")
elif int(ch) == 3:
		print("Enter user name")
		uname=input()
		print("Enter password")
		upass=input()
		ucrypt=crypt.crypt(upass,"123")
		os.system("useradd -m -p"+" "+uname)

elif int(ch) == 4:
	print("Enter the file name")
	filename = input()
	os.system("cat" + filename)
elif int(ch) == 5:
	sys.exit(0)
else:
	print("wrong input")

