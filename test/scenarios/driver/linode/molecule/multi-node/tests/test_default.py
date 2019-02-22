import os
import re

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.skip(reason='Scenario tests not implemented yet')
def test_hostname(host):
    assert re.search(r'instance-[12]', host.check_output('hostname -s'))


@pytest.mark.skip(reason='Scenario tests not implemented yet')
def test_etc_molecule_directory(host):
    f = host.file('/etc/molecule')

    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755


@pytest.mark.skip(reason='Scenario tests not implemented yet')
def test_etc_molecule_ansible_hostname_file(host):
    filename = '/etc/molecule/{}'.format(host.check_output('hostname -s'))
    f = host.file(filename)

    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
