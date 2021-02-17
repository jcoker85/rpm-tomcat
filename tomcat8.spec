# To Build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget -P ~/rpmbuild/SOURCES https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.42/bin/apache-tomcat-8.5.42.tar.gz
#
# wget https://github.com/inab/rpm-tomcat/archive/8.5.42.tar.gz
# tar xf 8.5.42.tar.gz
# cp -p rpm-tomcat-8.5.42/tomcat8.spec ~/rpmbuild/SPECS
# cp -p rpm-tomcat-8.5.42/tomcat8.{init,sysconfig,logrotate} ~/rpmbuild/SOURCES
# rpmbuild -bb ~/rpmbuild/SPECS/tomcat8.spec

%define __jar_repack %{nil}
%define tomcat_home /usr/share/tomcat
%define tomcat_group tomcat
%define tomcat_user tomcat

Summary:    Apache Servlet/JSP Engine, RI for Servlet 3.1/JSP 2.3 API
Name:       tomcat8
Version:    8.5.63
BuildArch:  noarch
Release:    1
License:    Apache Software License
Group:      Networking/Daemons
URL:        http://tomcat.apache.org/
Source0:    apache-tomcat-%{version}.tar.gz
Source1:    %{name}.init
Source2:    %{name}.sysconfig
Source3:    %{name}.logrotate
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be
a collaboration of the best-of-breed developers from around the world.
We invite you to participate in this open development project. To
learn more about getting involved, click here.

This package contains the base tomcat installation that depends on Oracle's JDK and not
on JPP packages.

%package lib
Group: Development/Compilers
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name} = %{version}-%{release}

%description lib
Libraries needed to run the Tomcat Web container

%package admin-webapps
Group: System Environment/Applications
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: System Environment/Applications
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package examples-webapp
Group: System Environment/Applications
Summary: The examples web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description examples-webapp
The examples web application for Apache Tomcat.

%package root-webapp
Group: System Environment/Applications
Summary: The ROOT web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description root-webapp
The ROOT web application for Apache Tomcat.

%prep
%setup -q -n apache-tomcat-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{tomcat_home}/
cp -R * %{buildroot}/%{tomcat_home}/

# Drop init script
install -d -m 755 %{buildroot}/%{_initddir}
install    -m 755 %_sourcedir/%{name}.init %{buildroot}/%{_initddir}/%{name}

%clean
rm -rf %{buildroot}

%pre
getent group %{tomcat_group} >/dev/null || groupadd -r %{tomcat_group}
getent passwd %{tomcat_user} >/dev/null || /usr/sbin/useradd --comment "Tomcat Daemon User" --shell /bin/bash -M -r -g %{tomcat_group} --home %{tomcat_home} %{tomcat_user}

%files
%defattr(-,%{tomcat_user},%{tomcat_group})
%{tomcat_home}/
%defattr(-,root,root)
%{_initddir}/%{name}

%post
chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
  service %{name} stop > /dev/null 2>&1
  chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
  service %{name} condrestart >/dev/null 2>&1
fi

%changelog
* Mon Feb 15 2021 Jamie Coker <jamie.coker@sap.com>
- 8.5.63
- Reworked spec file and removed unneeded stuff
- Removed .sysconfig and .logrotate files 
* Tue Jun 25 2019 José María Fernández <jose.m.fernandez@bsc.es>
- 8.5.42
* Sat May 25 2019 José María Fernández <jose.m.fernandez@bsc.es>
- 8.5.41 (which fixes a deaadlock https://bz.apache.org/bugzilla/show_bug.cgi?id=63251)
* Tue Jan 15 2019 José María Fernández <jose.m.fernandez@bsc.es>
- 8.5.37
* Fri Dec 14 2018 José María Fernández <jose.m.fernandez@bsc.es>
- 8.5.35
* Mon Oct 30 2017 José María Fernández <jose.m.fernandez@bsc.es>
- 8.5.23
* Tue Feb 21 2017 José María Fernández <jmfernandez@cnio.es>
- 7.0.75
* Wed Dec 14 2016 José María Fernández <jmfernandez@cnio.es>
- 7.0.73
* Wed Jun 8 2016 José María Fernández <jmfernandez@cnio.es>
- 7.0.69
* Wed Apr 7 2016 José María Fernández <jmfernandez@cnio.es>
- 7.0.68
* Wed Nov 4 2015 José María Fernández <jmfernandez@cnio.es>
- 7.0.65
* Wed Jul 22 2015 Jeremy McMillan <jeremy.mcmillan@gmail.com>
- 7.0.63
* Mon May 11 2015 Forest Handford <foresthandford+VS@gmail.com>
- 7.0.61
* Thu Sep 4 2014 Edward Bartholomew <edward@bartholomew>
- 7.0.55
* Fri Apr 4 2014 Elliot Kendall <elliot.kendall@ucsf.edu>
- Update to 7.0.53
- Changes to more closely match stock EL tomcat package
* Mon Jul 1 2013 Nathan Milford <nathan@milford.io>
- 7.0.41
