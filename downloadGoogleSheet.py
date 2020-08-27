from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from csv_functions import create_csv,write_to_csv
import datetime
import os
from time import gmtime, strftime




########################################################################################################
    # Authentication begins
########################################################################################################

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/spreadsheets']

def main():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    service_sheets = build('sheets', 'v4', credentials=creds)

########################################################################################################
    # Authentication ends
########################################################################################################

    # Call the Sheets API
    sheet = service_sheets.spreadsheets()


    # The ID and range of an OPPR data import spreadsheet.
    RANGE_NAME = '{ENTER TAB NAME}!{ENTER RANGE}'
    spreaadsheet_id = '{ENTER SPREADSHEET ID}'
    new_csv = '{ENTER_NAME_OF_CSV}.csv'


    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=RANGE_NAME).execute()
    values = result.get('values', [])


    if not values:
        print('No data found.')
    else:

        # function to create CSV for appropriate folder
        create_csv(projects_csv)


        for row in values:

            new_entry = [row]


            # Write to CSV created
            write_to_csv(new_csv,new_entry)


if __name__ == '__main__':
    main()
