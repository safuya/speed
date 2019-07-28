from functools import lru_cache

import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def get_google_credentials(
        scope=['https://spreadsheets.google.com/feeds',
               'https://www.googleapis.com/auth/drive'],
        keyfile='client_secret.json'):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile, scope)
    return gspread.authorize(credentials)


def get_spreadsheet(name='speed'):
    gc = get_google_credentials()

    try:
        spreadsheet = gc.open(name)
    except gspread.SpreadsheetNotFound:
        spreadsheet = gc.create(name)

    gc.insert_permission(spreadsheet.id,
                         None,
                         perm_type='anyone',
                         role='reader')

    return spreadsheet


def get_worksheet(spreadsheet, name='speed'):
    try:
        return spreadsheet.worksheet(name)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.worksheet('Sheet1')
        worksheet.update_title(name)
        return worksheet


def read_and_sanitise_csv(filename='/var/speed/output.csv'):
    csv = pd.read_csv(filename)
    csv.Download = csv.Download / 1_000_000
    csv.Upload = csv.Upload / 1_000_000
    return csv[['Timestamp', 'Distance', 'Ping', 'Download', 'Upload']]


def main():
    spreadsheet = get_spreadsheet()
    worksheet = get_worksheet(spreadsheet)
    csv = read_and_sanitise_csv()
    set_with_dataframe(worksheet, csv)


if __name__ == '__main__':
    main()
