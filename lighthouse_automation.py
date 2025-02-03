import json
import os
import subprocess
from datetime import datetime
import pandas as pd
from utils import save_report, create_summary

def run_lighthouse(url, output_dir):
    """Run Lighthouse for a specific URL"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"lighthouse_{timestamp}"
    
    command = f"lighthouse {url} --output=json,html --output-path={output_dir}/{report_name} --chrome-flags='--headless'"
    
    try:
        subprocess.run(command, shell=True, check=True)
        return f"{report_name}.report.json"
    except subprocess.CalledProcessError as e:
        print(f"Error running Lighthouse for {url}: {e}")
        return None

def main():
    # Create output directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "reports")
    os.makedirs(output_dir, exist_ok=True)

    # Load configuration
    with open("config.json", "r") as f:
        config = json.load(f)

    results = []
    for url in config["urls"]:
        print(f"Testing {url}...")
        report_file = run_lighthouse(url, output_dir)
        
        if report_file:
            report_path = os.path.join(output_dir, report_file)
            result = save_report(report_path, url)
            results.append(result)

    # Create summary
    if results:
        summary_file = create_summary(results, output_dir)
        print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    main()
