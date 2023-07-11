import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

template = """Question: {question} Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0, api_key=OPENAI_API_KEY), verbose=True)

    return llm_chain

if __name__ == "__main__":
    cl.run()
