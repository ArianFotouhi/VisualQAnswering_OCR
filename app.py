from llm import LLM_Launcher

instruction = "Answer with minimal number of words. Example: What is the seat number? A15"


# question = "What is the passenger name?" 
# question = "What is the gate?" 
# question = "what is the flight date?"
question = "what is the seat number?" 
# question = "what is the flight number?"
# question = "what is the flight destination?"

image_path = 'image5.png'


LLM_Launcher(question= question,
             instruction= instruction,
             image_path=image_path)