# 🧪 Asana Automation Script (Python + Selenium)

Automates the creation of dashboards, tasks, and reports on the [Asana](https://asana.com) website using Python and Selenium WebDriver. Includes automated test cases with detailed reporting via `pytest` and `Allure`.

---

## ⚙️ Setup

 **Install Dependencies:**
Install the dependemcies selenium, pytest, and allure. Then run the script and generate reports for that.
## Project Structure:

/project-folder
├── chromedriver
├── test_asanascript.py

🚀 Run the Automation

cd chrome_driver_path
pytest --alluredir=allure-results
allure serve allure-results

This opens Chrome, executes test cases from test_asanascript.py, and generates a test report in the browser.

🧰 Tools & Technologies
- Python
- Selenium WebDriver
- ChromeDriver
- pytest

## Allure Reporting

📄 Output
Automated UI interaction with Asana

Detailed test reports (with pass/fail stats and timestamps)

## 👩‍💻 Author
I wrote this script as part of a testing automation assignment.
