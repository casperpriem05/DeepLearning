#!/bin/bash

python -m pip install --upgrade pip
pip install accelerate==0.28.0
pip install matplotlib==3.10.3
pip install pillow==9.3.0
pip install tensorflow==2.19.0
pip install diffusers==0.26.3 bitsandbytes==0.42.0
pip install transformers==4.38.2 diffusers==0.26.3 datasets==2.18.0 huggingface-hub==0.21.4
pip install xformers==0.0.25.post1 --index-url https://download.pytorch.org/whl/cu121
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121
pip install ultralytics==8.3.136
pip uninstall -y opencv-python
pip install opencv-python-headless==4.10.0.84
pip install --upgrade "numpy<2.0"
pip install --upgrade "optree>=0.13.0"
