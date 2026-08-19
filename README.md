 Smart Expense & Budget Analyzer

A Python-based data analysis application that helps users understand their spending patterns by processing **CSV transaction files and text-based PDF statements**. The application summarizes expenses, analyzes spending by category, identifies large transactions, and presents the results through an interactive Streamlit dashboard.

##  Project Overview

Managing transaction data can make it difficult to understand where money is being spent. This project was created to transform raw transaction records into meaningful and easy-to-understand insights.

The application allows users to upload transaction data and automatically performs basic data cleaning, analysis, and visualization.

##  Features

*  Upload **PDF** transaction statements
*  Upload **CSV** transaction files
*  Clean and process transaction data
*  Calculate total spending
*  Calculate average transaction value
*  Identify the largest transactions
*  Analyze spending by category
*  Visualize spending patterns
*  Interactive Streamlit dashboard
*  Basic error handling for invalid or unsupported data

## How It Works

```text id="4d8b3b"
             Transaction Data
                    │
             ┌──────┴──────┐
             ↓             ↓
            CSV           PDF
             │             │
             │        Text Extraction
             │             │
             └──────┬──────┘
                    ↓
              Data Processing
                    ↓
              Data Cleaning
                    ↓
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       Summary   Categories   Largest
       Analysis   Analysis   Transactions
          │         │         │
          └─────────┼─────────┘
                    ↓
             Streamlit Dashboard
```

## Technologies Used

* **Python** — Core programming language
* **Pandas** — Data processing and analysis
* **Streamlit** — Interactive web application
* **PyPDF** — PDF text extraction
* **Matplotlib** — Data visualization

## Project Structure

```text id="q75xga"
smart-budget-analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the main application logic, including:

* File uploading
* PDF extraction
* CSV processing
* Data cleaning
* Expense calculations
* Category analysis
* Interactive dashboard

### `requirements.txt`

Contains all Python dependencies required to run the project.

##  Installation

### 1. Clone the repository

```bash id="y8egkf"
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project

```bash id="j2p3tv"
cd smart-budget-analyzer
```

### 3. Install dependencies

```bash id="5fjr6m"
pip install -r requirements.txt
```

### 4. Run the application

```bash id="r4r0lj"
streamlit run app.py
```

The application will open in your browser.

##  Requirements

```text id="a8y7nq"
streamlit
pandas
matplotlib
pypdf
```

Install them with:

```bash id="72v4wm"
pip install streamlit pandas matplotlib pypdf
```

##  Input Formats

### CSV

The recommended CSV format is:

```text id="u3k4wm"
Date,Description,Category,Amount
2026-08-01,Books,Education,1200
2026-08-02,Lunch,Food,250
2026-08-03,Bus,Transport,80
2026-08-04,Notebook,Education,150
```

### PDF

The application can extract text from **machine-readable PDFs**.

Scanned PDFs that contain only images may require OCR before the transaction information can be processed reliably.

##  Example Analysis

After uploading transaction data, the dashboard can display:

```text id="zv8p5n"
Total Spending       ₹18,450
Average Transaction  ₹615
Largest Transaction  ₹5,000
```

It can also group expenses by categories such as:

```text id="w0k8bs"
Education
Food
Transport
Entertainment
Shopping
```

##  Technical Concepts

This project provided practical experience with:

* Data cleaning
* Data transformation
* Exploratory data analysis
* Statistical summaries
* Data visualization
* PDF text extraction
* File handling
* Interactive application development

##  Future Improvements

*  Automatic transaction categorization
*  Monthly spending comparison
*  Budget-limit alerts
*  Spending prediction using machine learning
*  Anomaly detection for unusual transactions
*  Interactive charts and filters
*  Exportable financial reports
*  OCR support for scanned statements
*  Database storage for historical transactions
*  Personalized budgeting recommendations

## Learning Outcomes

Building this project helped me understand how raw data can be transformed into useful information through **data processing, analysis, and visualization**. It also gave me practical experience building a complete Python application with an interactive user interface.

## Project Purpose

This project was developed as part of my exploration of **Python, data science, and practical software development**, with the goal of applying programming concepts to a real-world problem: making transaction data easier to analyze and understand.

##  License

This project is intended for **educational and portfolio purposes**.
