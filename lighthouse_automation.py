import json
import os
import subprocess
from datetime import datetime
from utils import save_report, create_summary
import time

def run_lighthouse(url, output_dir, device_type):
    """Run Lighthouse for a specific URL and device type"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"report_{device_type}_{timestamp}"
    device_dir = os.path.join(output_dir, device_type)
    os.makedirs(device_dir, exist_ok=True)
    
    output_path = os.path.join(device_dir, report_name)
    
    # Base command parts
    command_parts = [
        'lighthouse',
        url,
        '--output=json,html',
        f'--output-path="{output_path}"',
        '--chrome-flags="--headless"'
    ]
    
    # Add device-specific settings
    if device_type == 'mobile':
        command_parts.extend([
            '--preset=perf',
            '--emulated-form-factor=mobile',
            '--throttling.cpuSlowdownMultiplier=4',
            '--throttling-method=simulate'
        ])
    else:  # desktop
        command_parts.extend([
            '--preset=desktop',
            '--emulated-form-factor=desktop',
            '--throttling.cpuSlowdownMultiplier=1',
            '--throttling-method=simulate'
        ])
    
    command = ' '.join(command_parts)
    
    try:
        print(f"Running Lighthouse for {url} ({device_type})...")
        subprocess.run(command, shell=True, check=True)
        time.sleep(2)  # Wait for files to be written
        
        json_file = f"{output_path}.report.json"
        if os.path.exists(json_file):
            return json_file
        return None
            
    except subprocess.CalledProcessError as e:
        print(f"Error running Lighthouse: {e}")
        return None

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "reports")
    os.makedirs(output_dir, exist_ok=True)

    urls = ["https://www.example.com"]
    device_types = ["desktop", "mobile"]
    
    results = []
    for url in urls:
        for device_type in device_types:
            json_path = run_lighthouse(url, output_dir, device_type)
            if json_path and os.path.exists(json_path):
                result = save_report(json_path, url, device_type)
                results.append(result)
                print(f"Report saved: {json_path}")

    if results:
        summary_file = create_summary(results, output_dir)
        print(f"\nSummary saved to {summary_file}")

if __name__ == "__main__":
    main()
