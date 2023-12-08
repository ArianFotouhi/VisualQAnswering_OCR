from llm import LLM_Launcher

image_path = ''
question = "What is the date of event" 
instruction = "Answer short"
image_path = 'image.png'

LLM_Launcher(question= question,
             instruction= instruction,
             image_path=image_path)