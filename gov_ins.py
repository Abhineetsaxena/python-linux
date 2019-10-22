import cv2
import subprocess

cap=cv2.VideoCapture(0)
while True:
	ret, photo=cap.read()
	#grayphoto=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
	cv2.imshow("hey",photo)
	if cv2.waitKey(1)==13:
		#break
		cv2.imwrite("/root/Desktop/inspection.png",photo)
		subprocess.getstatusoutput("hadoop fs -put /root/Desktop/inspection.png /")
	if cv2.waitKey(1)==66:
		break
	
cv2.destroyAllWindows()
cap.release()






