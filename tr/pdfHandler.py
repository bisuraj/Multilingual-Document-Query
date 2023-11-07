import pdfplumber
import tempfile
import streamlit as st

from deep_translator import GoogleTranslator
from googletrans import Translator


def translateToEnglish(docPages):

    translator = Translator(service_urls=[
        'translate.google.com',    # Default for general translations
        'translate.google.co.in',  # English (India)
        'translate.google.de',     # German
        'translate.google.fr',     # French
        'translate.google.es',     # Spanish
        'translate.google.it',     # Italian
        'translate.google.co.jp',  # Japanese
        'translate.google.com.br',  # Portuguese (Brazil)
        'translate.google.com.np',  # Nepali (Nepal)
        'translate.google.co.in',  # Hindi (India)
        'translate.google.co.tn',  # Tamil (India)
    ])

    
    # You can change 'en' to your target language
    pageTr = []
    
    for page in docPages:
        
        translation = translator.translate(page, dest='en')

        pageTr.append(translation.text)
        
    return " ".join(pageTr)


def extractText(pdfFile):

    if pdfFile is None:
        raise AttributeError(f"No pdf file uploaded")

    with tempfile.NamedTemporaryFile() as tempFile:
        tempFile.write(pdfFile.read())

        with pdfplumber.open(tempFile) as pdf:
            pageText = []
            
            for page in pdf.pages:
                pageText.append(page.extract_text())
                
                # break
                # print(text)

        print(translateToEnglish(pageText))
        # with open("../temp/text.txt", "w", encoding='utf-16') as f:
        #     f.write(translateToEnglish(text))


with open(r"E:\Projects\NLP_\Final\Papers\Tamil_culture.pdf", "rb") as f:
    extractText(f)
