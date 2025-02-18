# Lighthouse Performance Testing Automation

Automated performance testing tool using Google Lighthouse for multiple URLs across different environments and device types.

## Prerequisites

- Node.js (for Lighthouse)
- Python 3.x
- Chrome browser

## Setup

1. Install Lighthouse globally:
```bash
npm install -g lighthouse
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Main Configuration (config.json)
- Located in `config.json`
- Controls device configurations and active environment
- Example:
```json
{
    "configurations": {
        "desktop": {
            "preset": "desktop",
            "form-factor": "desktop"
        },
        "mobile": {
            "preset": "mobile",
            "form-factor": "mobile"
        }
    },
    "activeEnv": "staging"
}
```

### Environment Configuration
- Located in `env/` directory
- Separate files for different environments (staging.json, production.json)
- Contains URLs to test for each environment

## Usage

1. Select environment by updating `activeEnv` in config.json
2. Run the script:
```bash
python lighthouse_automation.py
```

## Output

- Reports are saved in the `reports/` directory
- Organized by device type (desktop/mobile)
- Each report includes:
  - HTML report
  - JSON data
  - Summary of all tests

## Report Structure

```
reports/
├── desktop/
│   └── [webpage]_desktop_[timestamp].report.html
├── mobile/
│   └── [webpage]_mobile_[timestamp].report.html
└── summary_[timestamp].json
```
