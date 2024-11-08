import streamlit as st 
from services.blob_service import upload_blob
from services.document_services import analyze_document

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url,caption="Imagem enviada",use_column_width=True)
    st.write("Resultados da validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green'>Cartão válido!</h1>",unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info["card_name"]}")
        st.write(f"Banco Emissor: {credit_card_info["bank_name"]}")
        st.write(f"Data e validade: {credit_card_info["expiry_date"]}")
    else:
        st.markdown(f"<h1 style='color: red'>Cartão Invalido!</h1>",unsafe_allow_html=True)
        st.write("Este não é um cartão de credito válido. Por favor tente outro cartão!")

def configure_interface():
    st.title("Upload de arquivo DIO BOOTCAMP - desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo",type=["png","jpg","jpeg"])

    if uploaded_file:
        fileName = uploaded_file.name 

        blob_url = upload_blob(uploaded_file,fileName)

        if blob_url is not None:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analyze_document(blob_url)

            show_image_and_validation(blob_url, credit_card_info)

        else:
            st.write(f"Ocorreu um erro ao enviar o arquivo {fileName} para o Azure Blob Storage")


if __name__ == "__main__":
    configure_interface()