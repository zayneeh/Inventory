# Home inventory 

A data pipeline for processing home inventory PDF documents,
extracting structured data, and preparing it for analytics.

## Overview

This project implements:

- Processing of home inventory data from PDF files
- Parsing and structuring textual content
- Extraction of key information about inventory items and owners
- Returning a structured JSON response for analytics

## Project Structure

```text
PERICULUM-DS-INTERNSHIP---TECHNICAL-ASSESSMENT/
├── data/
│   ├── home_inventory.pdf
│   └── result.json
├── scripts/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── Align.py
│   ├── Classes.py
│   ├── Extract_data.py
│   └── Load_in_json.py
├── tests/
├── .gitignore
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Installation

```bash
# Clone the repository
git clone https://github.com/zayneeh/Periculum-DS-Internship---Technical-Assessment.git


cd Periculum-DS-Internship---Technical-Assessment
```

# Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

# Install dependencies

```bash
pip install -r requirements.txt

 #if using Poetry

Poetry install
```

# Run Pipeline

```bash
python main.py
```
