# Ball-on-Head-Tracking-Using-OpenCV
In the ABU ROBOCON 2022 Theme, the robot must be able to accomplish a preset objective, such as breaking the lagori disc and displace which is on the opponent Robot.

Computer Vision is a field of study that helps to develop techniques to recognize images and displays. It has different featureslike image recognition, object detection and image creation, etc. Object detection is used in face detection, vehicle detection, web images, and safety systems.

Using these techniques and algorithms, based on Color Detection which is also based on image processing require lots of mathematical and computerv frameworks understanding by using dependencies such as OpenCV we can detect BOH in image by the area object in a highlighted rectangular box .This additionally incorporates the exactness of every strategy for distinguishing object.

As a result, our objective is to identify the ball on the opponent's robot. Because I was new to OpenCV at the time, detecting the white ball was more difficult for me. I used a deep learning technique to detect if it was successfully archived, but we had to implement it on an embedded system, and when we did, we lost accuracy, so I decided to track the blue plate, which is the ball's base. So I applied the hSV technique to identify the blue disc and obtained a detection range of 7.2 m.

I also applied some mathematics and found the angle and distance of the disc from the camera. Hence, the distance and angle are achieved according to that data. I have to control the motor speed and give the horizontal and vertical angle, so I have to send this data to the Arduino from the Raspberry Pi. So, as this algorithm is deployed on the Raspberry Pi, I successfully established communication between the Raspberry Pi and Arduino. According to that data, I give the rpm to the motor and a perfect vertical and horizontal angle to the mechanism. 

Refer below link for Video

https://drive.google.com/drive/folders/1Ximfg1-KuPpoy5ckm-h-RLROpXXloFu1?usp=sharing
