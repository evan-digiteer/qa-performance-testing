import json
import pandas as pd
from datetime import datetime

def save_report(report_path, url):
    """Process and save Lighthouse report"""
    with open(report_path, 'r') as f:
        report_data = json.load(f)

    metrics = report_data['audits']
    
    result = {
        'url': url,
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

def create_summary(results, output_dir):
    """Create a summary CSV file from multiple reports"""
    df = pd.DataFrame(results)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = f"{output_dir}/summary_{timestamp}.csv"
    
    df.to_csv(summary_file, index=False)
    return summary_file
