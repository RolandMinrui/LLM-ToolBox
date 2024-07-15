## Quick Start
### Environment Setup
```
conda create -n toolbox python=3.9 -y
conda activate toolbox

# Install correct PyTorch version that satisfy your CUDA version
## CUDA 11.7
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
## CUDA 12.1
conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia



pip install trl
pip install peft
pip install vllm
pip install jsonlines
pip install wandb
```