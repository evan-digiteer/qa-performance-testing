# Lighthouse Automation Project

This project automates Google Lighthouse testing for multiple URLs and generates reports.

## Prerequisites

- Python 3.8+
- Node.js and npm (for Lighthouse)
- Google Chrome

## Installation

1. Install Lighthouse globally:
```bash
npm install -g lighthouse
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.json` to specify:
- URLs to test
- Lighthouse configuration flags

## Usage

Run the automation script:
```bash
python lighthouse_automation.py
```

The script will:
1. Create a `reports` directory
2. Run Lighthouse tests for each URL
3. Generate HTML and JSON reports
4. Create a CSV summary of all results

## Output

- Individual HTML reports for each URL
- JSON reports with detailed metrics
- Summary CSV file with key metrics across all URLs
