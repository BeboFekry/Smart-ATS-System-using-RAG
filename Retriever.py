import os
from sentence_transformers import SentenceTransformer
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

class embedding:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    def embed_documents(self, docs):
        embeddings = self.model.encode(docs)
        return embeddings.tolist()
    def embed_query(self, query):
        return self.model.encode(query).tolist()

class retriever():
    def __init__(self, verbose=0):
        
        embed_model = embedding()
        if verbose==1:
            print("Embedded model loaded succesfully!")
        #Loading VDB
        vector_database = Chroma(persist_directory="Data/VectorDB", embedding_function=embed_model)
        print(vector_database._collection.count())
        
        if verbose==1:
            print("Vactor database loaded succesfully!")

        self.retriever = vector_database.as_retriever(search_type="mmr", search_kwargs={'k':10})

        API = "AIzaSyCaPzDUJujNjXa8r2wQ5P0RCHlTMXJc5zE"

        self.llm = GoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=API,temprature=0)

        temp = """you are an AI helpfull assistant that helps recruiters to find best candidates.
        you will given 10 resumes, you need to recommend the best candidate from them according to the job description you will take.
        you need to formatting and write all the candidate's resumes you have completely, includes connection information, location, and all informations.
        then you need to suggest the best one according to the job description.
        you need to discuss why to choose a certain candidate.
        knowlege you know: {context}
        Question / Job Description: {question}"""

        self.prompt = PromptTemplate.from_template(temp)

        self.rag_chain = (
        {"context":self.retriever, "question":RunnablePassthrough()}
        | self.prompt
        | self.llm
        | StrOutputParser()
        )

        if verbose==1:
            print("RAG Chain loaded succesfully!")
        
    def find(self, job_description):
        try:
            answer = self.rag_chain.invoke(job_description)
            return answer
        except Exception as e:
            return f"Error occurred: {str(e)}"

