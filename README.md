# Metrc Package Combiner

This repository contains a Google Apps Script to combine multiple Metrc Excel package export files into a single Google Sheets spreadsheet.

## Overview

The script processes Excel files from a Google Drive folder, where each file represents package data from Metrc (seed-to-sale tracking system) for different licenses and package statuses. It combines all data into a unified spreadsheet while preserving license numbers and package status information from the filenames.

## Requirements

### Google Apps Script Setup
1. **Enable Drive API**: In your Apps Script project, go to:
   - `Resources` > `Advanced Google Services` > Enable `Drive API`
   - Also enable it in the Google Cloud Console for your project

### File Naming Convention
Files must follow this naming pattern:
```
Metrc-Massachusetts-[License No.]-Packages-[Package Status].xlsx
```

**Example**: `Metrc-Massachusetts-MC281599-Packages-Active.xlsx`

### Supported Values
- **License Numbers**: MC281599, MP281433 (or any alphanumeric license)
- **Package Statuses**: Active, Inactive, In-Transit, Transferred

## How It Works

1. **Reads Excel files** from the specified Google Drive folder
2. **Converts each Excel file** to Google Sheets format using the Drive API
3. **Maps columns** according to package status schemas (each status has different columns)
4. **Combines all data** into a single spreadsheet with standardized column names
5. **Creates a summary sheet** showing row counts per license/status combination
6. **Cleans up** temporary converted files

## Column Mapping

The script handles different schemas for each package status:

### Active Packages
- Contains: Location, Lab Test Status
- Missing: Patient, Finished, Discontinued, etc.

### Inactive Packages  
- Contains: Patient, Administrative Recall
- Missing: Location, Finished, Discontinued, etc.

### In-Transit Packages
- Contains: Patient, Administrative Recall, Finished, Discontinued
- Missing: Location, Gross Weight, etc.

### Transferred Packages
- Contains: Destination License, Manifest Number, Transfer Status, Production Batch info
- Uses different column names (e.g., "Package" instead of "Tag")

## Output

The script creates a new Google Sheets spreadsheet with:

1. **Main Sheet**: Combined data with all rows from all files
   - Columns: 33 standardized columns including License_No, Package_Status, Processing_Date, etc.
   
2. **Summary Sheet**: Overview of processed data
   - Columns: License_No, Package_Status, Row_Count

## Installation & Usage

1. Open [Google Apps Script](https://script.google.com)
2. Create a new project
3. Enable the Drive API (see Requirements above)
4. Copy the contents of `combineMetrcPackages.txt` into the script editor
5. Update the `FOLDER_ID` constant with your Google Drive folder ID
6. Run the `combineMetrcPackages()` function
7. Authorize the script when prompted
8. Check the execution log for progress and the output spreadsheet link

## Error Handling

The script includes robust error handling:
- Skips files that don't match the naming convention
- Handles files with no data
- Logs errors for individual files without stopping the entire process
- Cleans up temporary files even if errors occur

## Original Issue

The original script was failing with errors like:
```
Exception: Service Spreadsheets failed while accessing document with id...
```

This was caused by trying to open Excel files directly as Google Sheets without proper conversion. The fix uses the Drive API's `insert()` method with `convert: true` to properly convert Excel files to Google Sheets format before processing.

## Folder Structure

```
Google Drive Folder (ID: 1uzk2fa0-DzgHXlSPQNuw86YaVSxPBhaN)
├── Metrc-Massachusetts-MC281599-Packages-Active.xlsx
├── Metrc-Massachusetts-MC281599-Packages-Inactive.xlsx
├── Metrc-Massachusetts-MC281599-Packages-InTransit.xlsx
├── Metrc-Massachusetts-MC281599-Packages-Transferred.xlsx
├── Metrc-Massachusetts-MP281433-Packages-Active.xlsx
├── Metrc-Massachusetts-MP281433-Packages-Inactive.xlsx
├── Metrc-Massachusetts-MP281433-Packages-InTransit.xlsx
└── Metrc-Massachusetts-MP281433-Packages-Transferred.xlsx
```