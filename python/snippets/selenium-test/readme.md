## Steps to replicate the project

Create a virtual environment and activate it

    python3 -m venv SELENIUM

    source SELENIUM/bin/activate

Create requirements.txt file

    touch requirements.txt

Add: > selenium >= 3.141.0, < 3.142

Install requirements

    python3 -m pip install -r requirements.txt

download Webdriver acording to your Chrome version

    Versión 92.0.4515.159

    https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/

Create a directory to place the executables in, like C:\WebDriver\bin or /opt/WebDriver/bin

Add the directory to your PATH:

    export PATH="$PATH:/opt/WebDriver/bin"

then run:

    python3 google_search.py

Or use this shell script to set the directory path

    zsh ./run.sh

---

## .env file structure example

CUSTOM_PATH="/opt/WebDriver/bin/chromedriver"