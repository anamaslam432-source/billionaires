# Billionaire Birthdays

A small Flask web app that shows which billionaires were born on a given day of the year. Pick a date and see their name, date of birth, country, and net worth.

## Project Structure

```
api/
├── app.py               # Flask application
├── billionaires.xlsx    # Data source (10 billionaires)
├── requirements.txt     # Python dependencies
├── README.md
├── static/
│   └── style.css        # Page styling
└── templates/
    └── index.html       # Single page template
```

## Features

- Shows billionaires whose birthday matches **today** by default
- Date picker to look up any other day
- Matches on month and day only (the year is ignored)
- Friendly messages for invalid dates and for days with no birthdays

## Routes

| Route        | Behavior                                              |
|--------------|-------------------------------------------------------|
| `/`          | Birthdays for today's date                            |
| `/<date>`    | Birthdays for the given date, e.g. `/2026-10-06`      |

An unparseable date shows an error message asking for a format like `2026-10-06`.

## Data File

`billionaires.xlsx` must sit in the same folder as `app.py`. The app reads columns A to D, in this order:

| A    | B             | C       | D                        |
|------|---------------|---------|--------------------------|
| Name | Date of Birth | Country | Net Worth (Billion USD)  |

To add or change entries, edit the spreadsheet and keep this column order. Header names are not used, but the order is.

## Requirements

- Python 3.9 or newer
- Packages in `requirements.txt`: Flask, pandas, openpyxl

## Setup and Run

```bash
# 1. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app (run it from inside the api/ folder)
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Notes

- Run `python app.py` from inside the `api/` folder, because the Excel file is loaded with a relative path.
- The page loads fonts (Fraunces and Work Sans) from Google Fonts, so an internet connection is needed for the intended look. It falls back to system fonts offline.
- `debug=True` is for local development only. For production, use a WSGI server such as gunicorn and turn debug off.
