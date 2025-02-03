import json
import pandas as pd
from datetime import datetime
import time

def save_report(report_path, url, device_type):
    """Process and save Lighthouse report"""
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                report_data = json.load(f)

            metrics = report_data['audits']
            
            result = {
                'url': url,
                'device_type': device_type,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'performance_score': report_data['categories']['performance']['score'] * 100,
                'first_contentful_paint': metrics['first-contentful-paint']['numericValue'],
                'speed_index': metrics['speed-index']['numericValue'],
                'largest_contentful_paint': metrics['largest-contentful-paint']['numericValue'],
                'interactive': metrics['interactive']['numericValue'],
                'total_blocking_time': metrics['total-blocking-time']['numericValue'],
                'cumulative_layout_shift': metrics['cumulative-layout-shift']['numericValue']
            }
            return result
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            if attempt == max_attempts - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)

def create_summary(results, output_dir):
    """Create a summary CSV file from multiple reports"""
    df = pd.DataFrame(results)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = f"{output_dir}/summary_{timestamp}.csv"
    
    df.to_csv(summary_file, index=False)
    return summary_file
