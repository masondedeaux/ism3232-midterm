# ISM3232 Midterm: Harvest Table Catering

- **Name:** Mason Dedeaux
- **Version:** BETA
- **Date:** October 25, 2026

## What This Program Does

This program creates an event report for Harvest Table Catering. It calculates event costs and discounts, checks staffing needs, and shows a summary of all bookings.

## Business Rules

- Food cost is the guest price multiplied by the number of guests.
- Events under 25 guests get no discount. Events with 25 or more guests get 5% off.
- Nonprofit events with 100 or more guests get 12% off instead.

- A $75 service fee is added when the discounted food cost is $500 or less.
- Events with a final total above $2,500 need a manager's sign-off.
- A second chef is needed for more than 80 guests or a final total of at least $3,000.

## How to Run  

Run these commands from the project folder in WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

```bash
ruff format .
ruff check .
pytest -v
```

The 23 tests cover all eight business functions, rule boundaries, empty lists, ties, and report formatting.

## Files in This Repository

- `business_rules.py`: Contains the eight business functions and rule constants.
- `main.py`: Stores the events and displays the report.
- `tests/__init__.py`: Marks the tests folder as a Python package.
- `tests/test_business_rules.py`: Contains the 23 tests.

- `requirements.txt`: Lists the installed packages and versions.
- `.gitignore`: Keeps the virtual environment and cache files out of Git.
- `README.md`: Explains the program and how to run it.
- `commands.md`: Records the terminal commands and their output.

## AI Use Statement

I did not use AI on this exam.