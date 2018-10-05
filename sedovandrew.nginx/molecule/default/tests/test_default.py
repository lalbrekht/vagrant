import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_is_installed(host):
    host.package("nginx").is_installed


def test_nginx_is_running(host):
    host.service("nginx").is_running


def test_nginx_is_enabled(host):
    host.service("nginx").is_enabled


def test_nginx_listen_port(host):
    host.socket("tcp://0.0.0.0:80").is_listening
