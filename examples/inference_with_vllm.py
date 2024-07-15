import os
import argparse
import datetime
import json
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name_or_path", 
                        type=str, 
                        default="meta-llama/Llama-2-7b-hf", 
                        help="model name or path for inference")
    parser.add_argument("--dataset_path", 
                        type=str, 
                        default="../data/examples.json", 
                        help=".json path of dataset")
    parser.add_argument("--output_dir", 
                        type=str, 
                        default="../output_dir/output.jsonl", 
                        help=".json path for output")
    parser.add_argument("--max_tokens", 
                        type=int, 
                        default=128, 
                        help="max number of newly generated tokens")
    args = parser.parse_args()

    return args

def main():
    args = arg_parser()   

    print("--- Start Preparing Prompts and Data ---")
    print(f"The dataset is {args.dataset_path}")
    with open(args.dataset_path, "r") as f:
        data = json.load(f)['instances']
    prompts = [i['input'] for i in data]

    print("--- Start Loading Model and Tokenizer ---")
    print(f"The model is {args.model_name_or_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path, trust_remote_code=True)

    model = LLM(model=args.model_name_or_path)
    sampling_params = SamplingParams(temperature=0, 
                                     max_tokens=args.max_tokens,
                                     stop_token_ids=[tokenizer.eos_token_id])

    print("--- Start Inference ---")
    outputs = model.generate(prompts, sampling_params)

    print("--- Start Writing Outputs ---")
    if os.path.exists(args.output_dir):
        os.remove(args.output_dir)
    text = []
    for output in outputs:
        text.append({
            "input": output.prompt,
            "output": output.outputs[0].text
        })
    with open(args.output_dir, "w") as f: 
        json.dump(text, f, indent=4)
    
    print("--- Finish ---")

if __name__ == "__main__":
    main()
