"""
Composio AI Product Ops - Configuration
"""

import os

class Config:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(PROJECT_ROOT, "data")
    RESULTS_FINAL = os.path.join(DATA_DIR, "results_final.json")
    RESULTS_PASS1 = os.path.join(DATA_DIR, "results_pass1.json")
    METRICS_JSON = os.path.join(DATA_DIR, "metrics.json")
    VERIFICATION_QUEUE = os.path.join(DATA_DIR, "verification_queue.json")
    DATASET_CSV = os.path.join(DATA_DIR, "dataset.csv")
    
    # Verification thresholds
    CONFIDENCE_THRESHOLD = 0.85
    DEFAULT_TIMEOUT = 10
    USER_AGENT = "ComposioAIProductOpsAgent/2.4"
