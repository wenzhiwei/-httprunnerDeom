import os

from utils.loader import load_yaml
from utils.runner import runner_yaml



class TestSingleApi:


    def test_single_api(self):
        single_api_yml="E:/httprunnerDeom/api/mubu_homepage.yml"
        load= load_yaml(single_api_yml)
        assert load["request"]["url"] =="http://mubu.com/"

    def test_run_single_api(self):
        single_api_yml = "E:/httprunnerDeom/api/mubu_login_submit.yml"
        result = runner_yaml(single_api_yml)
        assert result == True

        single_api_yml = "E:/httprunnerDeom/api/mubu_homepage.yml"
        result = runner_yaml(single_api_yml)
        assert result == True

