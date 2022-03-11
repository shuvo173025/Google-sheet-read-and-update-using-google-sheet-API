from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import openpyxl

def getting_data_from_responses_file():
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    # The ID of a sample spreadsheet.
    #SAMPLE_SPREADSHEET_ID = '1HybOoZlHxYaGdhELlBQyiuHxFagVyD3e8yQXVUXbCQE'
    SAMPLE_SPREADSHEET_ID = '1mo2PwKH_IC0thDX0AAmnQotfJerjmv6GvlXau14yDLE'


    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Form Responses 1!A1:G1076").execute()
    global values
    values = result.get('values', [])

getting_data_from_responses_file()
#print(values)

def getting_data_from_old_xlsx_dataset():
    temp_dict_2 = {}
    df = pd.read_excel('NLP_Data_Set.xlsx')

    ndf = df[['Timestamp','Text In Local Language','Text In moderate Language','Sentiment']]

    x = 'Disgust'
    for i,y in enumerate(ndf['Sentiment']):
        if x == y:
            timestamp = ndf['Timestamp'][i]
            text_in_local_language = ndf['Text In Local Language'][i]
            test_in_moderate_language = ndf['Text In moderate Language'][i]
            temp_dict = {'Timestamp':timestamp,'Text In Local Language':text_in_local_language,'Text In moderate Language':test_in_moderate_language}
            temp_dict_1 = {i:temp_dict}
            temp_dict_2.update(temp_dict_1)

    global z
    z = pd.DataFrame(temp_dict_2).transpose()
    #print(z['Text In moderate Language'])
getting_data_from_old_xlsx_dataset()



def fix_sentiment(c,aoa):
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of a sample spreadsheet.
    # SAMPLE_SPREADSHEET_ID = '1HybOoZlHxYaGdhELlBQyiuHxFagVyD3e8yQXVUXbCQE'
    SAMPLE_SPREADSHEET_ID = '1mo2PwKH_IC0thDX0AAmnQotfJerjmv6GvlXau14yDLE'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=c, valueInputOption = "USER_ENTERED", body = {"values":aoa}).execute()


def get_changable_sentiment():
    test = []
    old_data_set_index_list = z.index
    old_data_set_text_list = z['Text In moderate Language']
    #a = (old_data_set_text_list[old_data_set_index_list[0]])

    ndf = pd.DataFrame(values)
    #b = (ndf[2][10])

    for i,x in enumerate(old_data_set_index_list):
        #### old data set ar text
        a = (old_data_set_text_list[old_data_set_index_list[i]])
        #### responses data ar text
        b = ndf[2][(old_data_set_index_list[i]+1)]
        if a == b:
            c = "Form Responses 1!E" + str((old_data_set_index_list[i]+2))
            #aoa = [['Fear']]
            #aoa = [['Disgust']]
            #aoa = [['Surprise']]
            #fix_sentiment(c,aoa)

get_changable_sentiment()

