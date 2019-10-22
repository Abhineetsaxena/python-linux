import subprocess

subprocess.getstatusoutput("yum install -y httpd")
subprocess.getstatusoutput("systemctl restart httpd")
subprocess.getstatusoutput("systemctl enable httpd")
subprocess.getstatusoutput("iptables -F")
subprocess.getstatusoutput("setenforce 0")
