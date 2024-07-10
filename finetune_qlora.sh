export CUDA_VISIBLE_DEVICES=0,1

DATA_PATH="<your data path>"
OUTPUT_PATH="<your output path>"
MODEL_PATH="<your model path>"
WANDB_RUN_NAME="<your wandb run name>"

cd finetune
deepspeed --master_port=13500 \
    finetune.py \
    --model_name_or_path $MODEL_PATH \
    --data_path $DATA_PATH \
    --output_dir $OUTPUT_PATH \
    --num_train_epochs 3 \
    --model_max_length 1024 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --save_steps 100 \
    --save_total_limit 1 \
    --learning_rate 1e-5 \
    --warmup_steps 10 \
    --logging_steps 20 \
    --lr_scheduler_type "cosine" \
    --gradient_checkpointing True \
    --report_to "wandb" \
    --run_name $WANDB_RUN_NAME \
    --deepspeed ../configs/ds_config_zero2.json \
    --bf16 True \
    --use_lora True \
    --bits 4 \
    --max_grad_norm 0.3 \
    --double_quant \
    --lora_r 64 \
    --lora_alpha 16 \
    --quant_type nf4 \