import wget
import pathlib
import pdfplumber
import PyPDF2
import numpy as np
import os
import pandas as pd
import openai

# Code adapted from https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88

def getPaper(paper_url, filename=paperFilePath):
    """
    Downloads a paper from it's arxiv page and returns
    the local path to that file.
    """
    downloadedPaper = wget.download(paper_url, filename)
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath

# Convert pdf to text and display content
def displayPaperContent(paperContent, page_start=0, page_end=5):
    for page in paperContent.pages[page_start:page_end]:
        print(page.extract_text())

#provide name of local file where downloaded pdf will be stored 
paperFilePath = "elk.pdf"
#Download and store pdf locally, replace the url with any pdf 
getPaper('https://arxiv.org/pdf/2106.15448.pdf')
#read pdf from local filepath
paperContent = PyPDF2.PdfFileReader(paperFilePath)
#Optional - show first 5 pages
displayPaperContent(paperContent)


openai.api_type = "azure"
openai.api_base = "https://aiforgoodlab-scu-openai.openai.azure.com/"
openai.api_version = "2022-03-01-preview"
openai.api_key = '[#add your key here#]'



def pr(x):
    print(x, end='\n')

def davinci(paperContent,temperature=0.30,max_tokens=60,p=0.9,full=False):
    '''
    The loop reads each page ofthe pdf in turn. 
    THe page is converted to text and the question and end tag are added
    Then this is sent to the RCW-2 davinci engine
    Each page's result is stored in a dictionary d

    Note: this method doesn't work so well.
    Probably better to isolate the methods section using regex and some deterministic rules, 
    then send that to davinci
    '''

    question = "Which datasets were used in the following paper?\n\n"
    end_tag = "\n The datasets:"
    print(temperature, max_tokens, p)
    d={}
    pg=0
    for page in paperContent.pages:
        pg+=1
        print('page number %s' %pg)
        text=question + page.extract_text() + end_tag
        response = openai.Completion.create(
            engine="RCW-2",
            prompt=text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=p,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['\n']
        )
        if full:
            d[pg]=response
        else:
            result=response.choices[0].text
            print(result)
            d[pg] = result
    return d

a=davinci(paperContent=paperContent)



print(prompt,end='\n')

response = davinci(prompt, max_tokens=220,temperature=.9,p=0.9)
response.choices[0].text



