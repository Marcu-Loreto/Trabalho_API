import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

def get_translate_chain():
    model = ChatOpenAI(
        model='gpt-4o',
    )
    translate_prompt = ChatPromptTemplate.from_template(
        'Traduza o texto a seguir para o idioma {language}: {text}'
    )
    translate_chain = translate_prompt | model | StrOutputParser()
    return translate_chain