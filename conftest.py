import  pytest

#RUN LIKE THIS
#pytest -v -s --html=reportinterview.html test_interview.py --username=Admin --password=admin123


#declare custom command line --username and --password
#register the command line
def pytest_addoption(parser):
    parser.addoption("--driver_path", action="store", help="input useranme")
    parser.addoption("--username", action="store", help="input useranme")
    parser.addoption("--password", action="store", help="input password")

@pytest.fixture
def params(request):
    params = {}
    params['driver_path'] = request.config.getoption('--driver_path')
    params['username'] = request.config.getoption('--username')
    params['password'] = request.config.getoption('--password')
    if params['username'] is None or params['password'] is None:
        pytest.skip()
    return params