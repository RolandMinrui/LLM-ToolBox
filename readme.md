# TEMG4950N: Meta LLaMA 3 Strategy for Viu International
This repo is designed for HKUST TEMG4950N courses.
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
pip install bitsandbytes
```
## Resources
### General
* [LLM-ToolBox](https://github.com/RolandMinrui/LLM-ToolBox): tailor-made github repo for TEMG4950N
* [HF Transformers](https://huggingface.co/docs/transformers/index): state-of-the-art LLMs library.
* [HF TRL](https://github.com/huggingface/trl): easy-to-use library for fine-tuning LLMs.
* [Meta Llama](https://llama.meta.com/docs/get-started/): official guidelines to Meta Llama series.
### Datasets
* [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json): contain 52K instruction-following data.
* [OpenAssistant Guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco): contain 10K high quality conversation & chat data.
### Prompting
* [Prompt Engineering Guide](https://www.promptingguide.ai/): a comprehensive guide to prompt engineering of language models.
### Fine-tuning
### Inference
* [vLLM](https://docs.vllm.ai/en/latest/): a fast and easy-to-use library for LLMs inference.
### Deployment
* [Ollama](https://ollama.com/)