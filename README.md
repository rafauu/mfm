# mfm

mfm is a smart mirror project running on Raspberry Pi.

## Installation
```
sudo apt-get install -y libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
sudo pip3 install Flask
sudo pip3 install opencv-python
wget "xml with face recognition"
```

## Running
```
git clone https://github.com/rafauu/mfm.git
cd mfm
export FLASK_APP=hello.py && flask run &
python3 face_recognition.py
```

## Useful commands
```
ls /dev/ | grep video
lsusb
```

## Solving problems
```
VIDEOIO ERROR: V4L2: Pixel format of incoming image is unsupported by OpenCV
Unable to stop the stream: Device or resource busy
```
`cv2.VideoCapture` is running in loop without releasing

```
Captured video is blank
```
Lack of `cv2.waitKey` method or wrong value

```
cv2.error: OpenCV(3.4.3) /home/pi/opencv-python/opencv/modules/objdetect/src/cascadedetect.cpp:1698: error: (-215:Assertion failed) !empty() in function 'detectMultiScale'
```
Xml with face recognition set is provided incorrectly

```
cv2.error: OpenCV(3.4.3) /home/pi/opencv-python/opencv/modules/core/src/persistence_c.cpp:388: error: (-49:Unknown error code -49) Input file is empty in function 'cvOpenFileStorage'
```
Content of xml file is invalid
