# GSpread is a Python API for Google Sheets
import gspread

# This is for authorization with the Google Sheets API
from oauth2client.service_account import ServiceAccountCredentials

# PPrint is used for a readable JSON output in the terminal
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

# Opens Google sheet named "Tutorial" in Google Sheets
sheet = client.open("Tutorial").sheet1

# Grabs all data from the Google Sheet, and assigns it to the variable "data"
data = sheet.get_all_records()

# Grabs data from a specific row
row = sheet.row_values(3)

# Grabs data from a specific column
column = sheet.col_values(3)

# Grabs data from a specific Cell
cell = sheet.cell(1, 2).value

# Insert Row into Google Sheets "Tutorial"
insert_row = ["hello", 5, "red", "blue"]
sheet.insert_row(row, 4)

# Delete a specific row in Google Sheets "Tutorial"
sheet.delete_row(4)

# Update a specific cell in Google Sheets "Tutorial"
sheet.update_cell(2, 2, "This Guy")

# Grabs the amount of Rows in the Google Sheets "Tutorial" File
num_rows = sheet.row_count

pprint(num_rows)

