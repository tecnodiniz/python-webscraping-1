# Python Web Scraping with Selenium lib

This project was developed to help a friend with his searches.

Your objective is acessing a url = "https://portal.cfm.org.br/busca-medicos/", copy the elements we want like "name","phone number" and "address" for exemple.

# Briefing

- access the url: https://portal.cfm.org.br/busca-medicos/

- Get name and phone number

- Copy it into a csv file.

# Why Selenium?

I'm using Selenium because we are handling with a single page aplication. The request to server is asynchronous.

# How to Use

- You need to have Python installed on your machine.

- After cloning the project, activate the virtual environment using the command: source venv/bin/activate, and then run the script with Python.

- $ python script.py


Selenium will open a web browser. Sometimes, you will need to solve a captcha before scraping.

The script will prompt you to enter the number of pages to scrape and the starting page for web scraping.

After entering the required information, just wait and relax until the script finishes the job.

The scraping results will be saved into a file named "quotes.csv."

# Lets Start!






