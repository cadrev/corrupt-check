# Image Segregator
This is a sample script for determining the image quality sent by DOST-ASTI's UrbanFlood Sensor Networks.
DOST-ASTI's project on urban flood monitoring involves a tandem of water-level sensors and serial cameras to 
monitor street level flooding. Data from these sensors are sent via a GPRS every 5 minutes. 

![image](https://github.com/cadrev/corruptcheck/blob/master/screenshot/sample.png)

The challenge in archiving the camera images is that sometimes the images are corrupted upon receiving. 
To seggregate between the good and bad images, a simple machine learning model is made to clean the data set worth of 30000 images. 
