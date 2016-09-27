# Image Segregator
This is a sample script for determining the image quality sent by DOST-ASTI's UrbanFlood Sensor Networks.
DOST-ASTI's project on urban flood monitoring involves a tandem of water-level sensor and serial camera to 
monitor street level flooding. Data from these sensors are sent via GPRS every 5 minutes. 


<img src="https://github.com/cadrev/corruptcheck/blob/master/attachment/sample.png" width="300">


The challenge in archiving the camera images is that sometimes the images are corrupted upon receiving. 
To segregate between the good and bad images, a simple machine learning model is made to clean the data set worth of 30000 images. 
