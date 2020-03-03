import os
from utils.loader import load_yaml
from utils.runner import runner_yaml
import pytest


class TestSingleApi:


    def test_single_api(self):
        #single_api_yml="E:/httprunnerDeom/api/mubu_homepage.yml"
        self.single_api_yml=os.path.join(os.path.dirname(__file__),"api","mubu_homepage.yml")
        self.load= load_yaml(self.single_api_yml)
        assert self.load["request"]["url"] =="https://mubu.com/"

    def test_run_single_api(self):
        self.single_api_yml = os.path.join(os.path.dirname(__file__), "api", "mubu_login_submit.yml")
        self.result = runner_yaml(self.single_api_yml)
        assert self.result == True

        self.single_api_yml=os.path.join(os.path.dirname(__file__),"api","mubu_homepage.yml")
        self.result = runner_yaml(self.single_api_yml)
        assert self.result == True

