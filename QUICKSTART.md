# Quick Start Guide

## What Was Fixed

The Metrc Package Combiner script had a critical bug preventing it from converting Excel files to Google Sheets. This has been fixed.

## What You Need to Do

### 1. Enable the Drive API (CRITICAL - Required for the fix to work)

The fixed script uses Google's Drive API to properly convert Excel files to Google Sheets. You MUST enable it:

#### In Apps Script:
1. Open your Apps Script project
2. Click **Resources** (or Editor menu) → **Advanced Google Services**
3. Find **Drive API** in the list
4. Toggle it to **ON**
5. Click **OK**

#### In Google Cloud Console:
1. Click the link in the dialog that says "Google Cloud Platform API Dashboard"
2. Search for "Drive API"
3. Click **Enable**

### 2. Copy the Fixed Code

1. Open the `combineMetrcPackages.txt` file in this repository
2. Copy ALL the contents
3. Paste it into your Apps Script project (replacing the old code)

### 3. Run the Script

1. Save your script
2. Run the `combineMetrcPackages()` function
3. Authorize the script when prompted (it needs Drive permissions now)
4. Watch the execution log for progress

## What Changed

### Main Fix
- **Before**: Used `makeCopy()` which doesn't convert Excel to Sheets properly
- **After**: Uses `Drive.Files.insert()` with `convert: true` for proper conversion

### Other Improvements
- Fixed row count calculation (was off by 1)
- Better error handling and cleanup
- Added comprehensive documentation

## Expected Results

When you run the fixed script, you should see:

```
🚀 Starting Metrc Package Combiner...
📊 FOUND 8 Excel files!

📁 [1/8] Metrc-Massachusetts-MC281599-Packages-Active.xlsx
   License: MC281599 | Status: Active
   Rows: 150, Cols: 14
   Headers: Tag, Source Harvest(s), Source Package(s)...
   ✅ 149 rows

📁 [2/8] Metrc-Massachusetts-MC281599-Packages-Inactive.xlsx
   ...

🎉 SUCCESS! 1200 TOTAL ROWS
🔗 https://docs.google.com/spreadsheets/d/...
```

## Troubleshooting

### If you still see errors:

**Error: "Drive is not defined"**
- Solution: Enable Drive API (see step 1 above)

**Error: "Service Spreadsheets failed..."**  
- Solution: Make sure you copied ALL the new code, especially the Drive API parts

**Error: "Invalid filename"**
- Solution: Check that your files follow the naming convention:
  `Metrc-Massachusetts-[LICENSE]-Packages-[STATUS].xlsx`

## Need Help?

See the full documentation in:
- `README.md` - Complete usage guide
- `CHANGES.md` - Detailed technical changes
- `combineMetrcPackages.txt` - The script itself (with inline documentation)
