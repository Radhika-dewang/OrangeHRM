libraries to install:

pytest

pyest-html (for HTML report generation)

selenium

conftest.py is a configuration file where pytest fixture is mentioned

It accepts the username and password entered from the command line

The test cases first runs calling the  fixture in the  config file thus making username and password  accessible 


RUNNING COMMAND:
pytest -v -s --html=reportinterview.html test_interview.py --username=Admin --password=admin123

