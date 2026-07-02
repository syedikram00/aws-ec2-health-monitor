# AWS EC2 Health Monitor

A Python-based DevOps automation tool that connects to AWS EC2 using the AWS SDK (`boto3`), retrieves instance information, performs a basic health check, and exports the results to a CSV report.

## Features

- Connects to AWS EC2 using `boto3`
- Retrieves all EC2 instances
- Displays:
  - Instance Name
  - Instance ID
  - Instance State
  - Instance Type
  - Public IP Address
- Generates a CSV report automatically
- Handles missing values gracefully
- Clean and modular project structure

---

## Tech Stack

- Python 3.13
- AWS EC2
- AWS CLI
- boto3
- CSV Module
- Git
- GitHub

---

## Project Structure

```
aws-ec2-health-monitor/
│
├── .github/
│   └── workflows/
│       └── ec2.yml
│
├── logs/
│
├── reports/
│   └── ec2_report.csv
│
├── scripts/
│   └── ec2_health.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/aws-ec2-health-monitor.git
cd aws-ec2-health-monitor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials:

```bash
aws configure
```

Enter your:

- AWS Access Key
- AWS Secret Access Key
- Default Region
- Output Format (`json`)

---

## Usage

Run the script:

```bash
python scripts/ec2_health.py
```

---

## Sample Output

```
========================================
AWS EC2 HEALTH REPORT
========================================

Name          : Web Server
Instance ID   : i-003e9b77259510ecd
State         : Running
Instance Type : t3.micro
Public IP     : 54.xxx.xxx.xxx

========================================
Report saved successfully.
```

---

## Output Report

A CSV report is automatically generated in:

```
reports/ec2_report.csv
```

---

## Skills Demonstrated

- AWS SDK (boto3)
- AWS EC2 Automation
- Cloud Infrastructure Monitoring
- Python Scripting
- CSV Report Generation
- AWS CLI
- Git & GitHub
- DevOps Automation

---

## Future Improvements

- CloudWatch Metrics Integration
- CPU and Memory Monitoring
- Email Notifications
- Slack Alerts
- Multi-Region Support
- GitHub Actions Automation
- Logging Support

---

## Author

**Syed Ikram Shah**


