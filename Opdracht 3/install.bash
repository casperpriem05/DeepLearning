#!/bin/bash

pip install accelerate
pip install bitsandbytes
pip install datasets 
pip install diffusers
pip install matplotlib 
pip install pillow
pip install tensorflow 
pip install torch 
pip install transformers
pip install xformers
pip install ultralytics==8.3.136
pip uninstall -y opencv-python
pip install opencv-python-headless==4.10.0.84
pip install --upgrade "numpy<2.0"
pip install --upgrade "optree>=0.13.0"