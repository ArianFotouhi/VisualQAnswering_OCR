from ocr import ocr_image
import transformers
import torch

import warnings 
warnings.filterwarnings('ignore') 



def LLM_Launcher(question, instruction, image_path):
    # MODEL_NAME = "TheBloke/Llama-2-13b-Chat-GPTQ"

    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"


    retrived_info=ocr_image(image_path)



    template = f"Answer the question based on this information:{retrived_info}"


    
    messages = [
        {"role": "user", "content": template},
        {"role": "assistant", "content": instruction},
        {"role": "assistant", "content": question},

    ]



    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
    )    
    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=512,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.05,
        top_p=0.9,
    )
    print('------------------------------------------------Answer------------------------------------------------')
    print(outputs[0]["generated_text"][-1])

