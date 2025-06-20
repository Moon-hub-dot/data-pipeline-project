#!/bin/bash

echo "🔁 Starting Data Cleaning Pipeline..."

# Step 1: Run Python Script
python scripts/data_cleaner.py

echo "✅ Data Cleaned Successfully."

# Step 2: Simulate AWS Upload
echo "☁️ Uploading summary.csv to AWS S3 bucket..."
echo "[SIMULATED] aws s3 cp summary.csv s3://shivani-data-pipeline-2025/"

echo "🎉 Simulated Cloud Upload Completed."

# Step 3: Log Done
echo "📝 All tasks completed at $(date)"
echo "Pipeline run on $(date)" >> logs/pipeline_log.txt
# Simulate Lambda Trigger
echo "🧠 Triggering Lambda..."
python scripts/lambda_trigger.py

echo "🎉 Pipeline Execution Completed."
