from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
from shutil import get_terminal_size


def cls():
    print("\n" * get_terminal_size().lines, end='')

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


def finding_thoughtful_data():
    ndf = pd.DataFrame(values)

    thoughtful_sentiment = ndf[4]

    x = 'Thoughtful'
    for i,y in enumerate(thoughtful_sentiment):
        if x == y:
            c = "Form Responses 1!E" + str(i+1)
            print(ndf[2][i],'\n')
            print('Sad - 1\tAngry - 2\tHappy - 3\tDisgust - 4\tSurprise - 5\tFear - 6\tNull - 7\tPhrase - 8\n')
            z = (input('Enter The Number Here - - -  '))

            if z == '1':
                aoa = [['Sad']]

            if z == '2':
                aoa = [['Angry']]

            if z == '3':
                aoa = [['Happy']]

            if z == '4':
                aoa = [['Disgust']]

            if z == '5':
                aoa = [['Surprise']]

            if z == '6':
                aoa = [['Fear']]

            if z == '7':
                aoa = [['Null']]

            if z == '8':
                aoa = [['Phrase']]
            cls()
            fix_sentiment(c, aoa)

finding_thoughtful_data()
