import os
import getpass
import subprocess
import signal
subprocess.getstatusoutput("tput setaf 3")
print("\t\tWelcome to my Tools menu")
print("\t\t________________________")
subprocess.getstatusoutput("tput setaf 0")
def onSignal(x,y):
	print("\nsignal given\n")
	exit()
signal.signal(2,onSignal)

password="linux"

enteredPass=getpass.getpass("Enter password : ")

if enteredPass==password:
	operateOn=input("1-local\n2-remote\n3-setup Hadoop\n")
	if int(operateOn)==1:
		print("""
			press 1 to check date
			Press 2 to create folder
			
				""")
		print("Enter your choice :")
		choice=input()
		if int(choice)==1:
			print(subprocess.getstatusoutput("date")[1])
		elif int(choice)==2:
			print("Enter folder name")
			fname=input()
			subprocess.getstatusoutput("mkdir "+fname)
		#elif int(choice)==3:

	elif int(operateOn)==2:
		remoteIP=input("Enter Remote IP : ")
		while subprocess.getstatusoutput("ping -c 2 "+remoteIP)[0]!=0:
				print("\nThis IP is Unreachable!\nPress t to try again or any other key to exit: ",end='')
				if input()!='t':
					exit()
				else:
					remoteIP=input("Enter Remote IP : ")
					
				
		print("""
		press 1 to check date
		Press 2 to create folder
		
			""")
		print("Enter your choice :")
		choice=input()
		if int(choice)==1:
			print(subprocess.getstatusoutput("ssh "+remoteIP+" date")[1])
		elif int(choice)==2:
			print("Enter folder name")
			fname=input()
			subprocess.getstatusoutput("ssh "+remoteIP+" mkdir "+fname)
		#elif int(choice)==3:

	elif int(operateOn)==3:

		print(subprocess.getstatusoutput("echo id | ssh-keygen")[1])
		masterIP=input("Enter IP of master : ")
		while subprocess.getstatusoutput("ping -c 2 "+masterIP)[0]!=0:
			print("\nThis IP is Unreachable!\nPress t to try again or any other key to exit: ",end='')
			if input()!='t':
				exit()
			else:
		
				masterIP=input("Enter IP of master: ")

		print(subprocess.getstatusoutput("echo y | ssh-copy-id {}".format(masterIP))[1])

		f1=open("f2.txt","w")
		f1.write('<?xml version="1.0"?>'+'\n'+'<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>'+'\n'+'<!-- Put site-specific property overrides in this file. -->'+'\n\n'+'<configuration>'+'\n'+'<property>'+'\n'+
			'<name>dfs.name.dir</name>'+'\n'+'<value>/master</value>'+'\n'+'</property>'+'\n'+'</configuration>')
		f1.close()

		subprocess.getstatusoutput("echo redhat | scp f2.txt "+masterIP+":/etc/hadoop/hdfs-site.xml")

		f3=open("fh.txt","w")
		f3.write("""
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

{} master
			""".format(masterIP))

		f3.close()








				
					
		f1=open("f2.txt","w")
		f1.write('<?xml version="1.0"?>'+'\n'+'<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>'+'\n'+'<!-- Put site-specific property overrides in this file. -->'+'\n\n'+'<configuration>'+'\n'+'<property>'+'\n'+
			'<name>dfs.data.dir</name>'+'\n'+'<value>/data</value>'+'\n'+'</property>'+'\n'+'</configuration>')
		f1.close()



		f2=open("fcore.txt","w")
		f2.write('<?xml version="1.0"?>'+'\n'+'<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>'+'\n'+'<!-- Put site-specific property overrides in this file. -->'+'\n\n'+'<configuration>'+'\n'+'<property>'+'\n'+
			'<name>fs.default.name</name>'+'\n'+'<value>hdfs://'+masterIP+':9001'+'</value>'+'\n'+'</property>'+'\n'+'</configuration>')
		f2.close()



		numslave=input("\nEnter number of slaves : ")
		j=int(numslave)	
		ipsla=[]
	
		i=1
		while j!=0:
			ips=input("\nEnter ip of slave"+str(i)+" :")
			
			while subprocess.getstatusoutput("ping -c 2 "+ips)[0]!=0:
				print("\nThis IP is Unreachable!\nPress t to try again or any other key to exit: ",end='')
				if input()!='t':
					exit()
				else:
					ipsla=input("\nEnter ip of slave"+str(i)+" :")
			if subprocess.getstatusoutput("ping -c 2 "+ips)[0]==0:
				ipsla.append(ips)
				print(subprocess.getstatusoutput("echo y | ssh-copy-id {}".format(ips))[1])
				i=i+1
				
				subprocess.getstatusoutput("ssh "+ips+" hostnamectl set-hostname slave{}".format(ips))

				f3=open("fh.txt","a")
				f3.write('\n'+ips+' slave'+str(i))
				f3.close()


			j=j-1  

	#	i=0
	#	while numslave!=0:
			#ipsla=input("\nEnter ip of slave"+str(i)+" :")
			
			#while subprocess.getstatusoutput("ping -c 2 "+ipsla)[0]!=0:
		subprocess.getstatusoutput("ssh "+masterIP+" hostnamectl set-hostname master")
		subprocess.getstatusoutput("scp fh.txt "+masterIP+":/etc/hosts")			
		subprocess.getstatusoutput("scp fcore.txt "+masterIP+":/etc/hadoop/core-site.xml")		

		ipcli=input("Enter ip of client : ")
		while subprocess.getstatusoutput("ping -c 2 "+ips)[0]!=0:
			print("\nThis IP is Unreachable!\nPress t to try again or any other key to exit: ",end='')
			if input()!='t':
				exit()
			else:
				ipcli=input("\nEnter ip of client"+str(i)+" :")
		print(subprocess.getstatusoutput("echo y | ssh-copy-id {}".format(ipcli))[1])
		f3=open("fh.txt","a")
		f3.write('\n'+ipcli+' client')
		f3.close()



		for s in ipsla:
			#	print("\nThis IP is Unreachable!\nPress t to try again or any other key to exit: ",end='')
			#	if input()!='t':
			#		exit()
			#	else:
			#		ipsla=input("\nEnter ip of slave"+str(i)+" :")
			#if subprocess.getstatusoutput("ping -c 2 "+ipsla[i])[0]==0:

			
			subprocess.getstatusoutput("scp fh.txt "+s+":/etc/hosts")
			subprocess.getstatusoutput("scp f2.txt "+s+":/etc/hadoop/hdfs-site.xml")
			subprocess.getstatusoutput("scp fcore.txt "+s+":/etc/hadoop/core-site.xml")

			subprocess.getstatusoutput("ssh "+s+" iptables -F")
			subprocess.getstatusoutput("ssh "+s+" hadoop-daemon.sh start datanode")
			


			
			
	#		numslave=numslave-1  

			

		print("""
		press 1 to install jdk and hadoop
		Press 2 to
	
			""")
		print("Enter your choice :")
		choice=input()

			 
		subprocess.getstatusoutput("ssh "+masterIP+" iptables -F")
		subprocess.getstatusoutput("ssh "+masterIP+" hadoop namenode -format")
		subprocess.getstatusoutput("ssh "+masterIP+" hadoop-daemon.sh start namenode")
		subprocess.getstatusoutput("ssh "+masterIP+" jps")
		subprocess.getstatusoutput("ssh "+masterIP+" hadoop dfsadmin -report")

		for s in ipsla:
			subprocess.getstatusoutput("ssh "+s+" jps")

		
		subprocess.getstatusoutput("ssh "+ipcli+" iptables -F")
		subprocess.getstatusoutput("scp fcore.txt "+ipcli+":/etc/hadoop/core-site.xml")	
		subprocess.getstatusoutput("ssh "+ipcli+" hostnamectl set-hostname client")



	else:
		print("Invalid choice!")
		exit()		

else:
	print("Incorrect password!")
	exit()
