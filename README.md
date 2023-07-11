# Chainlit Langchain Chatbots
This repository contains chatbots built with LangChain &amp; Chainlit. The chatbot can answer questions about math, generate Instagram caption ideas, and provide summaries of current events.


https://github.com/arham-kk/chainlit-langchain-chatbots/assets/108623726/04366260-5000-4f42-88e6-dc32f11398f4


This repository contains 3 examples of how to use chainlit and langchain to create interactive applications.

1. A simple chatbot that asks questions and provides answers.
2. A tool that generates 10 Instagram caption ideas for a given input.
3. A chat agent that can answer questions about math and current events

# Installation

1. Clone the repository:
```
git clone https://github.com/arham-kk/chainlit-langchain-chatbots.git
```
2. To run the examples, you will need to install the following dependencies:
```
pip install chainlit langchain openai
```
3. Once you have installed the dependencies, you can run the example

# Usage

Set your OpenAI and SERPAPI key inside the files:

```bash
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
```
