rpm-tomcat
==========

An RPM spec file to build Tomcat 8.5 RPMs.

Steps to build them:

```bash
sudo yum -y install rpmdevtools git

git clone -b tomcat8 https://github.com/jcoker85/rpm-tomcat.git

cd rpm-tomcat
./rpm-generator.sh
```

then you can install the RPMs available at ~/rpmbuild/RPMS/noarch using either `yum` or `rpm`
