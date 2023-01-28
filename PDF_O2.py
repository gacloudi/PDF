import glob
import streamlit as st
from os import getcwd
from PyPDF2 import PdfMerger
files = st.file_uploader("Choose a image file",accept_multiple_files=True)
Output_file=st.text_input('Enter Output File Name')
#st.write("Upload a CSV/Text file or Type/Copy text below.")
#st.write("File will be downloaded to the working directory")
OP=Output_file + '.pdf'
#files = glob.glob(r'C:\Users\320848\OneDrive - Cognizant\Desktop\DS\*') # Creating a glob object
#files = glob.glob(r'C:\Users\DINGOO KARTHICK\Pictures\PDF\*.pdf') # Creating a glob object
merger = PdfMerger()
try:
    if files is not None:
        for pdf in files:
            merger.append(pdf)
        merger.write(OP)
        merger.close()
        c=getcwd()    
        c=c + '/' + OP
                #st.write(c)
        with open(c,"rb") as file:
                #st.write(c)
                st.download_button(label='Download',data=file,file_name=OP,mime="pdf")
except:
    st.write("E")