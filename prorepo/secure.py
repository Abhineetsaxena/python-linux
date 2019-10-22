import cv2
print("""
Enter your mode:
Press 1. Welcome Home
Press 2. Bye Home
""")
print("Enter Your Choice")
choice=input()
if int(choice) ==2 :
	cap= cv2.VideoCapture(0)
 	body = cv2.CascadeClassifier('haarcascade_fullbody.xml')
	while True:
    
    
  		ret, photo = cap.read()
    		coord=face.detectMultiScale(photo)
    		bodyNo=len(coord)
    
   		 if bodyNo>0 :
        		n=0
       		        while n<bodyNo:
            		x1=coord[n][0]
        
       	     		y1=coord[n][1]
            		x2=coord[n][2]+x1
            		y2=coord[n][3]+y1
            		rect_photo=cv2.rectangle(photo, (x1,y1), (x2,y2),(255,255,255),3)
            		n=n+1
    		cv2.imshow('bodies',rect_photo)
    		print(bodyNo+" Bodies Detected ");
    		if cv2.waitKey(1)==13:
            		#break
			cv2.imwrite("/root/Desktop/thief.png",photo)
			subprocess.getstatusoutput("hadoop fs -put /root/Desktop/theif.png /")
		if cv2.waitKey(1)==66:
			break
            
	cv2.destroyAllWindows()
	cap.release()
else:
	print("Welcome Home")
    
        
