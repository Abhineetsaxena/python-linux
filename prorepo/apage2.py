#!/usr/bin/python36

import subprocess

print("content-type: text/html")
print()

print("Abhineet's web page...<br>")
x=subprocess.getoutput("date")
print(x)

print("""
<h1><a href='http://192.168.43.132/172.17.0.2:4200' target='f'>redhat</a></h1>
<iframe width='100%' height='300px' name='f'></iframe>
""")
#subprocess.getoutput("sudo systemctl restart docker")
output=subprocess.getoutput("sudo docker ps -a")
rows=output.split("\n")

print("""
<marquee>Zoooooooooo........</marquee>
<table border='5' cellpadding='10'>
<tr>
<th>Name</th>
<th>Image</th>
<th>Status</th>
<th>Stop</th>
<th>Start</th>
<th>Console</th>
<th>Terminate</th>
</tr>
""")

for i in rows[1:]:
	print("<tr>")
	print("<td>"+i.split()[-1]+"</td>")
	print("<td>"+i.split()[1]+"</td>")
	if "Up" in i.split()[6]:
		print("<td>Running</td>")
		print("<td><a href='http://192.168.43.132/cgi-bin/doc_stop.py?q={}'>stop</a></td>".format(i.split()[0]))	

		print("<td>start</td>")
	elif "Exited" in i.split()[6]:
		print("<td>Stopped</td>")

		print("<td>stop</td>")
		print("<td><a href='http://192.168.43.132/cgi-bin/doc_start.py?q={}'>start</a></td>".format(i.split()[0]))

	else:
				
		print("<td>unknown</td>")
		print("<td>start</td>")			
		print("<td>stop</td>")

	print("<td>console</td>")
	print("<td><a href='http://192.168.43.132/cgi-bin/doc_terminate.py?q={}'>terminate</a></td>".format(i.split()[0]))	

	print("<td><a href='http://192.168.43.132/cgi-bin/doc_console.py?q={}' target='f'>console</a></td>".format(i.split()[0]))	
	
	print("</tr>")
print("""
</table>
""")
