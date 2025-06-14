from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


model = OllamaLLM(model="llama2")
 
template = """You are an expert in answering quesions about restaurants
Here are reviews of the restraunts: {reviews}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("------------")
    question = input("Ask your question (q to quit): ")
    if question == "q":
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews":[], "question":question})
    print(result)
 