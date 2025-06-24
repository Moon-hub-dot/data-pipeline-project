![GitHub Workflow Status](https://github.com/Moon-hub-dot/data-pipeline-project/actions/workflows/run_pipeline.yml/badge.svg)

# 🛠️ Data Pipeline Project – Automated Data Cleaning & Deployment

Welcome to the **Data Monitoring Pipeline Project** built by **Shivani G** – a fresher passionate about data analysis, DevOps, and cloud automation. This project simulates a real-world data engineering workflow using Python, Shell scripting, GitHub Actions, and AWS.

---

## 📌 Project Highlights

- ✅ **Automated Data Cleaning** using Python (pandas)
- ✅ **Log Generation** with time-stamped summaries
- ✅ **Shell Script** to simulate pipeline automation
- ✅ **GitHub Actions CI/CD** for auto-execution on every code push
- ✅ [Optional] AWS S3 & Lambda trigger setup for cloud automation

---

## 📂 Folder Structure

data_pipeline_project/
│
├── raw_data/ # Raw input CSV files
├── cleaned_data/ # Output: Cleaned CSVs
├── logs/ # Logs and summary reports
├── scripts/
│ ├── data_cleaner.py # Core cleaning + logging script
│ └── lambda_trigger.py # Simulated AWS Lambda trigger
├── run_pipeline.sh # Shell script to execute pipeline
├── .github/
│ └── workflows/
│ └── run_pipeline.yaml # GitHub Actions automation
└── README.md # You're reading it!
---

## 🔁 Workflow Overview

### 🔹 Step 1: Data Cleaning with Python
- Reads raw sales data CSV using `pandas`
- Cleans missing values, trims whitespaces
- Generates summary:
  - Total Sales
  - Total Profit
  - Top 5 Cities
- Saves cleaned data + summary log file

### 🔹 Step 2: Automation with Shell Script
- Executes Python script
- Simulates upload to AWS S3
- Echoes completion status

### 🔹 Step 3: GitHub Actions CI/CD
- Automatically runs the pipeline on every `git push`
- Future-ready for CRON jobs or scheduled triggers

---

## ☁️ (Optional) Cloud Component: AWS

- **AWS S3**: Simulated upload of cleaned data files
- **AWS Lambda**: Simulated auto-trigger when new file arrives in bucket

(Note: For real AWS usage, you'd need free-tier or paid access.)

---

## 📊 Sample Summary Log
✅ Summary:
Total Orders: 999
Total Sales: ₹3,52,450.00
Total Profit: ₹54,800.40
Top 5 Cities: {'New York': 120, 'San Francisco': 98, 'Los Angeles': 94, ...}
---

## 🚀 How to Run Locally

1. Clone repo  
   `git clone https://github.com/Moon-hub-dot/data-pipeline-project.git`

2. Navigate into folder  
   `cd data_pipeline_project`

3. Install dependencies  
   `pip install pandas`

4. Run the pipeline  
   - On Windows: `bash run_pipeline.sh` (Git Bash recommended)

---

## 🧠 Skills Demonstrated

- **Python** (Data wrangling with pandas)
- **DevOps** (Shell scripting, CI/CD)
- **Cloud Concepts** (AWS S3, Lambda – simulated)
- **Git & GitHub** (Version control, Actions)

---

## 📄 Resume Add-on

**“Built a complete data pipeline that automates data cleaning using Python, logs summaries, and simulates cloud upload to AWS S3. Integrated GitHub Actions for CI/CD and explored AWS Lambda-based automation triggers.”**

---

## 🙋‍♀️ About Me

👩🏻‍💻 **Shivani G**  
🎓 BCA Graduate | Aspiring Data Analyst  
📧 shivaniganesh388@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/shivani-g-2bb2a9288)  
🌟 Always learning. Always growing.

---

## 🫱🏼‍🫲🏼 Contributions

Pull requests, suggestions, and forks are welcome!  
⭐ Star this repo if you found it helpful.


