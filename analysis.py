import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

from pdf import extractpdf

key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model=genai.GenerativeModel('gemini-2.5-flash')


def analyze_resume(pdf_doc,job_desc):
    
    if pdf_doc is not None:
        pdf_text=extractpdf(pdf_doc)
        st.write('Extracted Successfully')    
    else:
        st.warning('Error!! Drop the file in PDF Format ❌')
        

    ats_score=model.generate_content(f''' Compare the resume{pdf_text} 
                                 and description{job_desc} 
                                 and get ATS score in range of 0-100.
                                 Generate the results in bullet points''')
    prob_score=model.generate_content(f''' Compare the resume {pdf_text} and the given 
                                  job description {job_desc} and give the probability
                                  in percent 0-100 to get selected on the given job''')
    good_fit=model.generate_content(f''' Compare the resume {pdf_text} and the given job description
                                {job_desc} and say whether am i a good fit for the job or not. 
                                If not, highlight what am I lacking and suggest
                                the areas of improvement''') 
    swot_analysis=model.generate_content(f''' Compare the resume {pdf_text} and given job description {job_desc}
                                     and provide SWOT Analysis. Generate minimum 3 points for each''')

    return {st.write(ats_score.text),
        st.write(prob_score.text),
        st.write(good_fit.text),
        st.write(swot_analysis.text)} 
    
    

     
        
        

        
