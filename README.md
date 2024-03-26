# Bulk Create Folders From a Spreadsheet Data
This script will create a main folder and inside of this main folder a folder with the name from the rows of a spreadsheet.

Format will be: "First column - Second column", so it can be a "Date - Title" or "Name - Family name" or "Serial number - Product name".
So it can be used for any type of folder Bulk creation you need.

## Bulk Create Folders from Spreadsheet

This Python script creates folders based on data from an Excel spreadsheet.

### Features

* Reads dates and titles from an Excel spreadsheet.
* Creates folders with the format "date - title" inside a designated parent folder.

### Requirements

* Python 3.x
* openpyxl library (`pip install openpyxl`)

### Instructions

1. **Clone or Download the Repository:**
   Clone this repository to your local machine or download the `Bulk_Create_folders.py` script.

2. **Update File Paths:**
   Open the script (`Bulk_Create_folders.py`) in a text editor.
    * Replace the value assigned to the `SPREADSHEET_PATH` variable with the actual path to your Excel spreadsheet on your computer.
    * Replace the value assigned to the `TARGET_FOLDER` variable with the desired path to the folder where you want to create the subfolders.

3. **Run the Script:**
   Open a terminal or command prompt and navigate to the directory containing the script.
   Run the script using the following command:

   ```bash
   python Bulk_Create_folders.py
Example Usage
SPREADSHEET_PATH:

'C:/Users/owner/Documents/data.xlsx'  # Replace with your actual path
TARGET_FOLDER:

'C:/Users/owner/Pictures/Project A'  # Replace with your desired path
This will create folders based on the date and title information found in your Excel spreadsheet within the "Project A" folder.
