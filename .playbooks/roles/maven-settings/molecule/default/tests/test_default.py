import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_settings_file(host):
    home = host.user().home
    f = host.file(home + "/.m2/settings.xml")

    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'

    assert f.contains("<id>artifactory</id>")
    assert f.contains("<username>${env.MAVEN_REPO_USER}</username>")
    assert f.contains("<password>${env.MAVEN_REPO_PASS}</password>")
    assert f.contains("<pluginGroup>org.eclipse.jetty</pluginGroup>")

    assert f.contains("<id>central</id>")
    assert f.contains("<username>admin</username>")
    assert not f.contains("<password>ignoredbecauseofprivatekey</password>")
    assert f.contains("<privateKey>${user.home}/.ssh/id_rsa</privateKey>")
    assert f.contains("<passphrase>helloworld</passphrase>")
    assert f.contains("<filePermissions>664</filePermissions>")
    assert f.contains("<directoryPermissions>775</directoryPermissions>")

    assert f.contains("<id>planetmirror.com</id>")
    assert f.contains("<name>PlanetMirror Australia</name>")
    assert f.contains("<url>http://downloads.planetmirror.com/pub/maven2</url>")

    assert f.contains("<id>test</id>")
    assert f.contains("<jdk>1.5</jdk>")
    assert f.contains("<arch>x86</arch>")
    assert f.contains("<user.install>${user.home}/our-project</user.install>")
    assert f.contains("<url>http://snapshots.maven.codehaus.org/maven2</url>")
    assert f.contains("<layout>default</layout>")
    assert f.contains("<layout>legacy</layout>")
    assert f.contains("<activeProfile>test</activeProfile>")
