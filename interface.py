import streamlit as st

from analysis import analyze_resume

st.set_page_config(page_title='CV Analyzer')

st.title('Resume Analysis Using AI')

st.header('''This will help in Analysis of Resume''')

st.sidebar.subheader('Drop your resume here')
pdf_doc=st.sidebar.file_uploader('Click here to browse',type=['pdf'])

st.sidebar.markdown("Designed by Midhun Santhosh")


job_desc=st.text_area('Copy and paste the JD here',max_chars=10000)

submit=st.button("Generate Score")

if submit:
    with st.spinner("Getting Results"):
        analyze_resume(pdf_doc,job_desc)
        
        
        
        


