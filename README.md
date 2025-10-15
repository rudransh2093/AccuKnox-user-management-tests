# AccuKnox-user-management-tests

1. Project Setup Steps
Follow these instructions to set up the environment and dependencies:

Clone the Repository:

git clone [https://github.com/rudransh2093/AccuKnox-user-management-tests.git](https://github.com/rudransh2093/AccuKnox-user-management-tests.git)
cd AccuKnox-user-management-tests


Create and Activate Python Virtual Environment:

# Create environment
python -m venv venv

# Activate environment (Windows CMD/VS Code Terminal)
venv\Scripts\activate

# Activate environment (Linux/Mac)
source venv/bin/activate


Install Required Dependencies (Playwright and Pytest):

pip install -r requirements.txt


Install Playwright Browser Binaries:

playwright install


2. How to Run the Test Cases
The tests are executed using pytest. Ensure your virtual environment is active before running.

Scenario

Description

Command to Run

Full E2E Suite

Runs all scenarios (login, add, search, edit, delete, logout).

pytest tests/ -v

Specific Test

Runs a single file/scenario.

pytest tests/test_add_user.py -v

3. Playwright Version Used
The following versions were used for development:

Playwright: 1.55.0

Python Version: 3.14.0