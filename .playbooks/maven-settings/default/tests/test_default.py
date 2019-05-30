import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_settings_file(host):
    home = host.user().home
    f = host.file(home + "/.m2/settings.xml")

    assert f.exists
    assert f.is_file
    assert f.contains("<id>artifactory</id>")
    assert f.contains("<username>${env.MAVEN_REPO_USER}</username>")
    assert f.contains("<password>${env.MAVEN_REPO_PASS}</password>")
    assert f.contains("<pluginGroup>org.eclipse.jetty</pluginGroup>")
    assert f.user == 'root'
    assert f.group == 'root'
