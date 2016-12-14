rpm-tomcat7
===========

An RPM spec file to build Tomcat 7.0 RPMs.

Steps to build them:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

wget -P ~/rpmbuild/SOURCES https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.73/bin/apache-tomcat-7.0.73.tar.gz

wget https://github.com/inab/rpm-tomcat7/archive/7.0.73.tar.gz
tar xf 7.0.73.tar.gz
cp -p rpm-tomcat7-7.0.73/tomcat7.spec ~/rpmbuild/SPECS
cp -p rpm-tomcat7-7.0.73/{tomcat7.init,tomcat7.sysconfig,tomcat7.logrotate} ~/rpmbuild/SOURCES
rpmbuild -bb ~/rpmbuild/SPECS/tomcat7.spec
```

then you can install the RPMs available at ~/rpmbuild/RPMS/noarch using either `yum` or `rpm`
