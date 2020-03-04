import jsonpath
import requests
import urllib3
import yaml

from utils import loader


def get_json_path(resp,json_file):
    value=jsonpath.jsonpath(resp.json(),json_file)
    return value[0]
def runner_yaml(file):
    runner_json=loader.load_yaml(file)
    reqs=runner_json["request"]
    url=reqs.pop("url")
    print("url:"+url)
    method=reqs.pop("method")
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    req=requests.request(method,url,**reqs);

    validator_map=runner_json["validate"]
    for key in validator_map:
        if "$" in key:
            actual_value=get_json_path(req,key)
        else:
            actual_value=getattr(req,key)
        expected_value=validator_map[key]

        assert actual_value == expected_value
    return True