

sudo python3 -m pip uninstall tellopy
python3 setup.py bdist_wheel
sudo python3 -m pip install dist/tellopy-*.dev*.whl --upgrade
sudo apt-get install python3-pip -y
sudo python3 -m pip install tellopy
sudo python3 -m pip install pygame
sudo apt-get install mplayer -y
sudo apt-get install -y python-dev pkg-config -y
sudo apt-get install -y libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libavresample-dev libavfilter-dev -y
sudo python3 -m pip install av
sudo apt install python3-opencv


# sudo apt install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# # Dependencies for Python bindings
# # If you use a non-system copy of Python (eg. with pyenv or virtualenv), then you probably don't need to do this part
# sudo apt install python3.5-dev libpython3-dev python3-numpy
# # Optional, but installing these will ensure you have the latest versions compiled with OpenCV
# sudo apt install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
