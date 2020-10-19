# Seach Disease Activity
A flask app to search for a disease which has no activity on " clinicaltrials.gov " in a given number of days.

### Code style:
Code follows PEP8 Standards

### Cloning the project:
Go to the desired directory and run

    git clone https://github.com/devgk00/iqvia_assignment.git

### Installing and creating virtual env
Go to the project root directory and run

step 1 - Installing virtualenv

    pip install virtualenv

step 2 - Creating virtualenv

    virtualenv -p python3 <virtualenv_name>

step 3 - Activating virtualenv

    source <virtualenv_name>/bin/activate

### Starting the application
After activating the virtualenv do the following

step 1 - Move to project directory
    
    cd iqvia_assignment

step 2 - Installing the requirements
    
    pip install requirement.txt

step 3 - Exporting the flask app

    export FLASK_APP=app.py

step 4 - Starting flask server

    flask run
    
### Running the test cases:

Run the following command on terminal - 

    python -m unittest tests/test_disease.py

### Technologies Used:

Framework : Flask

Language: Python 3.8

UI-Designing: Bootstrap4, HTML, CSS
