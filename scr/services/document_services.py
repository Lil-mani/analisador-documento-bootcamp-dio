from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from ultils.Config import Config

def analyze_document(card_url):

    credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
    document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)


    card_inf = document_Client.begin_analyze_document(
        "prebuilt-creditCard",
        AnalyzeDocumentRequest(url_source=card_url)
    )

    result = card_inf.result()

    for document in result.documents:
        fields = document.get('fields', {})

        return{
            "card_name": fields.get('CardHolderName', {}).get('content'),
            "card_number": fields.get('CardNumber', {}).get('content'),
            "expiry_date": fields.get('ExpirationDate', {}).get('content'),
            "bank_name": fields.get('IssuingBank', {}).get('content'),
        }

   

