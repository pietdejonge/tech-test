import os
import ansible
import pytest
import testinfra.utils.ansible_runner
import subprogess

APP_LABEL = "python-web-app"
APP_ROUTE = "python-web-app-svc-myproject.127.0.0.1.nip.io"

def test_pods():
    pod_status = subprocess.Popen('oc get pods -l name=python-web-app -o jsonpath={.items[*].status.phase} -n myproject', stdout=subprocess.PIPE, shell=True)
    output, err = process.communicate()
    assert "Running" in pod_status

def test_route():
    route_status = subprocess.Popen("curl http://" + APP_ROUTE, stdout=subprocess.PIPE, shell=True)
    output, err = process.communicate()
    assert "Hello World!" in route_status
