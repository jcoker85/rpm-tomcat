%define apps_home /apps
%define tomcat_home /apps/tomcat
%define temp_home /tmp/tomcat
%define tomcat_group callidus
%define tomcat_user callidus

Summary:    Apache Servlet/JSP Engine, RI for Servlet 3.1/JSP 2.3 API
Name:       calliduscloud-pmpro-tomcat-package-8.5.63
Version:    8.5.63
Release:    1.0
BuildArch:  noarch
License:    Apache Software License
Group:      Networking/Daemons
URL:        https://tomcat.apache.org/
Source0:    apache-%{name}-%{version}.tar.gz
BuildRoot:  %{temp_home}

%description
Apache Tomcat 8.5.63 Archive Installer

%install
install -d %{buildroot}/%{tomcat_home}/
cp -R * %{buildroot}/%{tomcat_home}/
cp -R %{buildroot}/%{tomcat_home}/apache-tomcat-%{version}/* %{buildroot}/%{tomcat_home}/

%files
%defattr(-,%{tomcat_user},%{tomcat_group},-)
%exclude %{tomcat_home}/apache-tomcat-%{version}/
%exclude %{tomcat_home}/webapps/*
%{apps_home}/

%changelog
* Tue Feb 16 2021 Jamie Coker <jamie.coker@sap.com>
- Refactored branches
- Removed .init file from tomcat8 branch
- Removed more unnecessary stuff from .spec file
* Mon Feb 15 2021 Jamie Coker <jamie.coker@sap.com>
- 8.5.63
- Reworked spec file and removed unneeded stuff
- Removed .sysconfig and .logrotate files 

