import streamlit as st
from PIL import Image
from os import getcwd
st.header("Convert")


#name = form.text_area('Please Enter the Text')
image_file = st.file_uploader("Choose a image file")
#form = st.form(key='my-form')
Output_file=st.text_input('Enter Output File Name')
#st.write("Upload a CSV/Text file or Type/Copy text below.")
#st.write("File will be downloaded to the working directory")
OP=Output_file + '.pdf'
#submit = st.button('Submit')
#st.write("Hel")
try:
    if image_file is not None:
#w=r'C:\Users\320848\Documents\doc2.docx'
#p=r'C:\Users\320848\Documents\doc21.pdf'
#print(p)
        #st.write('D')
        im_1=Image.open(image_file)
        im_1 = im_1.convert('RGB')
        #st.write('A')
        im_1.save(OP)
        c=getcwd()    
        c=c + '/' + OP
        #st.write(c)
        with open(c,"rb") as file:
                    #st.write(c)
                    st.download_button(label='Download',data=file,file_name=OP,mime="pdf") 
except:
    st.write("E")