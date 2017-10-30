rpm-tomcat
==========

An RPM spec file to build Tomcat 8.5 RPMs.

Steps to build them:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

wget -P ~/rpmbuild/SOURCES https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.23/bin/apache-tomcat-8.5.23.tar.gz

wget https://github.com/inab/rpm-tomcat/archive/8.5.23.tar.gz
tar xf 8.5.23.tar.gz
cp -p rpm-tomcat-8.5.23/tomcat8.spec ~/rpmbuild/SPECS
cp -p rpm-tomcat-8.5.23/tomcat8.{init,sysconfig,logrotate} ~/rpmbuild/SOURCES
rpmbuild -bb ~/rpmbuild/SPECS/tomcat8.spec
```

then you can install the RPMs available at ~/rpmbuild/RPMS/noarch using either `yum` or `rpm`
