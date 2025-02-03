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

2. Install pandas first:
```bash
pip install --only-binary :all: pandas
```

3. Install remaining Python dependencies:
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

Reports are organized in the following structure:
```
reports/
├── desktop/
│   ├── example.com_desktop_20231025_120101.report.html
│   └── example.com_desktop_20231025_120101.report.json
├── mobile/
│   ├── example.com_mobile_20231025_120201.report.html
│   └── example.com_mobile_20231025_120201.report.json
└── summary_20231025_120301.csv
```

Each report includes:
- Mobile and desktop versions
- Performance metrics for each device type
- Consolidated CSV summary comparing both versions
