# **🚀 Automated Testing Framework**

This repository contains an automated testing framework for **UI and API testing** using **Playwright, Pytest, and Requests**.

---

## **📌 Framework Overview**
This framework is designed for **end-to-end (E2E) UI automation** and **API functional testing**. It supports:

✅ **UI Testing:** Using **Playwright** with **Page Object Model (POM)** for maintainability.  
✅ **API Testing:** Using **Requests** with modular API utilities and test data handling.  
✅ **GitHub Actions CI/CD:** Automated test execution and report generation.  

---

## **🔧 Environment Setup**
Follow these steps to set up and run tests locally:

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.10+** and **Node.js** (for Playwright) installed.

#### **Clone the repository:**
```sh
git clone https://github.com/your-repo/talk-further-automation.git
cd talk-further-automation
```

# **🚀 Environment Setup & Test Execution Guide**

## **🔧 Virtual Environment Setup (Optional but Recommended)**

### **1️⃣ Create a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

# Install required Python packages:
```sh
pip install -r requirements.txt
```
# Install Playwright and browsers:
```sh
playwright install --with-deps
```

# **🚀 Test Execution **

## 1️⃣ Run UI Tests

### To execute Playwright UI tests, use:

```sh
pytest tests/test_e2e.py --maxfail=1 --disable-warnings -v --html=reports/ui_report.html --self-contained-html
```

## 2️⃣ Run API Tests
### To execute API tests, use:

```sh
pytest tests/test_api.py --maxfail=1 --disable-warnings -v --html=reports/api_report.html --self-contained-html
```

## 3️⃣ Run All Tests

### To run both UI and API tests:

```sh
pytest --maxfail=1 --disable-warnings -v --html=reports/full_report.html --self-contained-html
```

## 🖥️ GitHub Actions CI/CD
### This framework includes a GitHub Actions workflow for automated test execution.

## ✅ When does the workflow trigger?
On every push or pull request to main or master
Runs Playwright and API tests on Ubuntu (Linux)
Generates and uploads HTML reports & Playwright video recordings

## 📂 Folder Structure

📦 talk-further-automation
 ┣ 📂 config
 ┃ ┗ 📜 config.py                  # API and UI base URLs
 ┣ 📂 pages
 ┃ ┗ 📜 home_page.py               # Page Object Model for UI tests
 ┣ 📂 support
 ┃ ┣ 📜 common_functions.py        # UI helper functions
 ┃ ┣ 📜 random_utils.py            # Random data generator (Faker)
 ┣ 📂 api_utils
 ┃ ┣ 📜 base_api.py                # API base class (Requests)
 ┃ ┣ 📜 authors_api.py             # API utility for Authors endpoint
 ┣ 📂 tests
 ┃ ┣ 📜 test_e2e.py                # Playwright UI tests
 ┃ ┣ 📜 test_api.py                # API functional tests
 ┣ 📜 .github/workflows/ci.yml     # GitHub Actions workflow for CI/CD
 ┣ 📜 requirements.txt             # Python dependencies
 ┣ 📜 pytest.ini                   # Pytest configuration
 ┣ 📜 .gitignore                   # Files to exclude from Git tracking
 ┣ 📜 README.md                    # Documentation (this file)

## 📜 Reporting

After test execution, reports are generated in the reports/ folder.

#Local Execution: Open the HTML report:
open reports/report.html  # Mac/Linux
start reports/report.html # Windows

## 💡 Additional Features
Video Recording of Playwright tests (saved in videos/ folder)
Automatic Browser Setup with playwright install
Retry Logic for flaky tests
Logs & Assertions for better debugging



