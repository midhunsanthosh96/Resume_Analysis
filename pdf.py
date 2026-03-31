from pypdf import PdfReader

def extractpdf(pdf_doc):
    try:
        pdf=PdfReader(pdf_doc)
        
        raw_text=''
        for index,pages in enumerate(pdf.pages):
            text=page.extract_text()
            if text:
                raw_text+=text
                
        return raw_text
    
    except Exception as e:
        return f"Error in reading the pdf"
    
    