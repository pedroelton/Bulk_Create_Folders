import os
import openpyxl

# Define spreadsheet path
SPREADSHEET_PATH = r'C:\YOUR\SPREADSHEET\PATH'  # Replace with your actual file path

# Define target folder path 
TARGET_FOLDER = r'C:\YOUR\FOLDER\PATH'  # Replace with your desired folder path


def create_folder(date, title):
  """Creates a MAIN folder"""
  folder_name = f"{date} - {title}"
  full_path = os.path.join(TARGET_FOLDER, 'YOUR FOLDER NAME GOES HERE', folder_name)
  os.makedirs(full_path, exist_ok=True)
  print(f"Folder created: {full_path}")


#This script creates a folder with a "date - title" example "3.14 - This is the title"  
def main():
  # Open the Excel file
  wb = openpyxl.load_workbook(filename=SPREADSHEET_PATH)
  sheet = wb.active  # Assuming the first sheet is your data sheet

  # Skip header row (assuming first row is header)
  for row in sheet.iter_rows(min_row=2):
    date = row[0].value  # Assuming date is in the first column
    title = row[1].value  # Assuming title is in the second column
    create_folder(date, title)

if __name__ == '__main__':
  main()
