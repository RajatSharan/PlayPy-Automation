# PlayPy-Automation
Overview
PlayPy-Automation is a powerful test automation framework built using Playwright and Python. It enables fast, reliable, and scalable end-to-end (E2E) testing for modern web applications.

With Playwright’s robust capabilities and Python’s simplicity, this framework provides a seamless way to automate browser interactions across Chromium, Firefox, and WebKit.

Features
✅ Cross-browser & Cross-platform Testing – Run tests on Chrome, Firefox, and Safari effortlessly
✅ Headless & Headed Mode – Execute tests in headless mode for speed or headed mode for debugging
✅ Fast & Reliable Automation – Handles dynamic web elements, auto-waits, and resilient locators
✅ API Testing Support – Perform API calls and validate responses alongside UI tests
✅ Parallel Execution – Run multiple tests in parallel for faster results
✅ Screenshots & Video Recording – Capture test failures for debugging
✅ CI/CD Integration – Seamless integration with GitHub Actions, Jenkins, and other CI/CD pipelines

Tech Stack
Language: Python 🐍
Framework: Playwright 🎭
Test Runner: Pytest 🧪
Reporting: Allure Report 📊
Setup & Installation
1. Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/PlayPy-Automation.git
cd PlayPy-Automation
2. Create a Virtual Environment (Optional but Recommended)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
3. Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4. Install Playwright Browsers
sh
Copy
Edit
playwright install
Running Tests
Run All Tests
sh
Copy
Edit
pytest tests/
Run Tests in Headless Mode
sh
Copy
Edit
pytest --headless
Run Tests in Parallel
sh
Copy
Edit
pytest -n 4  # Runs 4 tests in parallel
CI/CD Integration
PlayPy-Automation is optimized for CI/CD workflows. Simply add the following GitHub Actions workflow to enable automated testing in your pipeline:

yaml
Copy
Edit
name: PlayPy Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Install Playwright Browsers
        run: playwright install

      - name: Run Tests
        run: pytest tests/
Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or bug fixes.


