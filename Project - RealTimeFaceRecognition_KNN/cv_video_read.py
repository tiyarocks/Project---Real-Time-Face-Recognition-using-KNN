#Read a video stream from camera(Frame by frame)
import cv2
cap=cv2.VideoCapture(0) #0 means id of default webcam
while True:
	ret,frame=cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#if due to any reason the frame is not captured try it again
	if ret==False:
		continue
	cv2.imshow("Video Frame",frame)
	cv2.imshow("Gray Frame",gray_frame)

	#wait for user input q then u wll stop the loop
	key_pressed=cv2.waitKey(1)&0xFF
	if key_pressed==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
