from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture(scope="module")
def setup_browser():
    # Create a browser instance (e.g., Chrome)
    driver = webdriver.Chrome()
    
    # Set up any other browser configurations if needed
    driver.maximize_window()
    
    time.sleep(3)
    # Provide the browser instance to the tests
    yield driver
    
    # After the tests are done, close the browser
    driver.quit()

def test_login_to_asana(setup_browser):
    driver = setup_browser
    # Go to the Asana website
    driver.get("https://app.asana.com/-/login")

    # Find the email input field and send the email to it
    email_input = driver.find_element(By.XPATH , "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/input")
    email_input.send_keys("bhavishyaorra.2000@gmail.com")

    # Find and click the "Continue" button
    continue_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]")
    continue_button.click()

    # Wait for the password input field to become present
    wait = WebDriverWait(driver, 10)
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="p"]')))

    # Send the password to the password input field
    password_input.send_keys("@Bhavishya29")

    # Click the login button
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]")
    login_button.click()

    # Wait for the login process to complete
    time.sleep(3)
     


def test_create_project(setup_browser):
    driver = setup_browser
    # Locate the "Create a Task" button and click it
    create_task = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div")
    create_task.click()
    # Wait for the task title input field to become present
    wait = WebDriverWait(driver, 10)
    task_title_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[1]/div[2]/textarea")))

    # Assert that the task title input field is present and enabled
    assert task_title_input.is_enabled()

    # Enter the title for the task
    task_title_input.send_keys('SampleTask1')

    # Press the Enter key to create the task
    task_title_input.send_keys(Keys.RETURN)

    # Add a delay to allow the task to be created (you can adjust the time as needed)
    time.sleep(5)
    

def test_create_project(setup_browser):
    driver = setup_browser
    # Wait for up to 10 seconds for the "Create Project" button to become present
    wait = WebDriverWait(driver, 10)
    create_project_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="asana_main_page"]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[2]/div/a/div/div[1]/div[2]/div/div/div/h6')))

    # Assert that the "Create Project" button is present
    assert create_project_button is not None

    # Click on the "Create Project" button
    create_project_button.click()

    # Wait for up to 10 seconds for the page to load
    wait = WebDriverWait(driver, 10)

    # Then, select the type of project by locating and clicking the relevant element
    # For example, clicking on a button for a specific project type
    project_type_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]")

    # Assert that the project type button is present
    assert project_type_button is not None
    project_type_button.click()

    # Add a delay if necessary
    time.sleep(5)

    # Locate the project title input field
    project_title_input = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/input")

    # Assert that the project title input field is present
    assert project_title_input is not None
    project_title_input.send_keys('SampleProject1')

    # Add a delay to ensure the project title is set (you can adjust the time as needed)
    time.sleep(5)

    # After setting the project title, you may need to confirm it. You can add that code here.
    confirm_project_name_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[4]/div")

    # Assert that the "Confirm Project Name" button is present
    assert confirm_project_name_button is not None
    confirm_project_name_button.click()

    # Add a delay if necessary
    time.sleep(10)

    # Create tasks in the project
    Task1 = driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]")

    # Assert that the Task1 element is present
    assert Task1 is not None
    Task1.send_keys(Keys.RETURN)

    Task1_input = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/label/textarea")

    # Assert that the Task1_input element is present
    assert Task1_input is not None
    Task1_input.send_keys('SampleTask1')
    time.sleep(5)
    
    # To create a section in the project
    section = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]")

    # Assert that the section element is present
    assert section is not None
    section.click()
    time.sleep(5)
    

    # To view the overview of the project
    project_overview = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/nav/ul/div[1]/div/div[1]/div/div/li/div/a/span/span/span")

    # Assert that the project_overview element is present
    assert project_overview is not None
    project_overview.click()
    time.sleep(5)

    # To view the board of the project
    project_board = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/nav/ul/div[1]/div/div[3]/div/div/li/div/a/span/span/span")

    # Assert that the project_board element is present
    assert project_board is not None
    project_board.click()
    time.sleep(3)

    # To view the timeline of the project
    project_timeline = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/nav/ul/div[1]/div/div[4]/div/div/li/div/a/span/span/span")

    # Assert that the project_timeline element is present
    assert project_timeline is not None
    project_timeline.click()
    time.sleep(10)

    # To view the calendar
    project_calendar = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[1]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/nav/ul/div[1]/div/div[5]/div/div/li/div/a/span/span/span")

    # Assert that the project_calendar element is present
    assert project_calendar is not None
    project_calendar.click()
    time.sleep(5)


def test_check_inbox(setup_browser):
    driver = setup_browser
    # Find and click on the "Inbox" link
    locate_inbox = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/nav/div[3]/a")

    # Assert that the "Inbox" link element is present
    assert locate_inbox is not None
    locate_inbox.click()
    time.sleep(10)
    

def test_create_reports(setup_browser):
    driver = setup_browser
    #For Reports
    open_reports = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/nav/div[2]/a")

    # Assert that the open_reports element is present
    assert open_reports is not None
    open_reports.click()
    time.sleep(5)

    #for finding the dashboard and creating the reports
    locate_dashboard = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[2]/div[2]/div/div/div[2]/a/div/div[1]/div[2]/h5")

    # Assert that the locate_dashboard element is present
    assert locate_dashboard is not None
    locate_dashboard.click()
    time.sleep(5)

    #for creating report
    create_report_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[2]/div[1]/div")

    # Assert that the create_report_button element is present
    assert create_report_button is not None
    create_report_button.click()
    time.sleep(5)

    #for adding report - here adding incomplete chart based on the tasks
    add_report = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/h5")

    # Assert that the add_report element is present
    assert add_report is not None
    add_report.click()
    time.sleep(2)

    #for creating report after confirming everything
    confirm_create_report = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]")

    # Assert that the confirm_create_report element is present
    assert confirm_create_report is not None
    confirm_create_report.click()
    time.sleep(5)
    
"""
def test_create_goal(setup_browser):
    driver = setup_browser
    #for adding the goal
    add_goal = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[2]/div/div/div/div[1]/div[2]/div")
    assert add_goal is not None
    add_goal.click()
    time.sleep(2)

    #for goal name
    goal_name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/input")
    assert goal_name.is_displayed(), "Goal name input field is not displayed"
    goal_name.click()
    time.sleep(2)

    goal_name.send_keys("sample goal")
    assert save_goal.is_displayed(), "Save Goal button is not displayed"
    goal_name.send_keys(Keys.RETURN)
    time.sleep(5)

    #For saving a goal
    save_goal = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]")
    save_goal.click()
    
"""

def test_create_portfolio(setup_browser):
    driver = setup_browser
    # Find and click on the "Portfolios" link
    select_portfolio = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/nav/div[3]/a")

    # Assert that the select_portfolio element is present
    assert select_portfolio is not None
    select_portfolio.click()
    time.sleep(5)

    #for viewing the portfolio
    portfolio_view = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[2]/div[2]/div/div/div[2]/a/div/div[2]")

    # Assert that the Portfolio_view element is present
    assert portfolio_view is not None
    portfolio_view.click()
    time.sleep(5)

    # Navigate back to Portfolios
    back_to_portfolios = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/nav/div[3]/a")

    # Assert that the back_to_portfolios element is present
    assert back_to_portfolios is not None
    back_to_portfolios.click()
    time.sleep(2)

    # Find and click on "Create Portfolio"
    create_portfolio = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/main/div[2]/div[2]/div/div/div[2]/div/div[2]")

    # Assert that the create_portfolio element is present
    assert create_portfolio is not None
    create_portfolio.click()
    time.sleep(2)

    # Enter a name for the portfolio
    portfolio_name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div[2]/input")

    # Assert that the portfolio_name element is present
    assert portfolio_name is not None
    portfolio_name.send_keys("Sample Portfolio")

    # Confirm and create the portfolio
    confirm_portfolio_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[3]")

    # Assert that the confirm_portfolio_button element is present
    assert confirm_portfolio_button is not None
    confirm_portfolio_button.click()
    time.sleep(5)


def test_view_workspace(setup_browser):
    driver = setup_browser
    # Find and click on the "Workspace" link
    open_workspace = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div[3]/nav/div[2]")

    # Assert that the open_workspace element is present
    assert open_workspace is not None
    open_workspace.click()
    time.sleep(5)

    # Find and click on the "Home" link to return to the home page
    home = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/nav/div[1]/a")
    # Assert that the home element is present
    assert home is not None
    home.click()
    time.sleep(5)


def test_close_browser(setup_browser):
    driver = setup_browser
    driver.quit()


if __name__ == "_main_":
     pytest.main(args=["-v", "--html=report.html"])

