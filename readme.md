## Quick Start
### Environment Setup
```
conda create -n toolbox python=3.9 -y
conda activate toolbox

# CUDA 11.7
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
pip install trl
```