from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
import transcriptor

transcript = transcriptor.get_transcript(
    "https://www.youtube.com/watch?v=vK4Mno4QYqk&t=1s")

OPENAI_API_KEY = "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"

template = f""" You are a helpful assistant programmed to generate questions based on any text provided. For every 
chunk of text you receive, you're tasked with designing 10 distinct questions. Each of these questions will be 
accompanied by 3 possible answers: one correct answer and two incorrect ones.

To ensure clarity and ease of processing, please structure your response in the following format, emulating a Python 
list of lists:

1. Create an outer list that contains 10 inner lists. 2. Each inner list represents a set of question and answers, 
and should contain exactly 4 strings in the following order: - The generated question. - The correct answer. - The 
first incorrect answer. - The second incorrect answer.

Please ensure your output mirrors this structure:
[
    ["Generated Question 1", "Correct Answer 1", "Incorrect Answer 1.1", "Incorrect Answer 1.2"],
    ["Generated Question 2", "Correct Answer 2", "Incorrect Answer 2.1", "Incorrect Answer 2.2"],
    ...
]
Make sure that your output is in english even if prompted in hindi or any other language
You must adhere to this format as it's optimized for further Python processing.
"""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
    )
chain = LLMChain(
    llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY),
    prompt=chat_prompt,
    )
print(chain.run(transcript))
