#!/bin/sh
BASEDIR="`dirname "$0"`"
case "$BASEDIR" in
	/*)
		# Absolute path
		true
		;;
	*)
		# Relative path
		BASEDIR="${PWD}/${BASEDIR}"
		;;
esac
rpmdev-setuptree
cd "${BASEDIR}"
tomcat_version="`grep -F Version tomcat8.spec | sed 's/^[^ ]* *//'`"
cp apache-tomcat-${tomcat_version}.tar.gz "${HOME}"/rpmbuild/SOURCES
cp tomcat8.spec "${HOME}"/rpmbuild/SPECS
rpmbuild -bb "${HOME}"/rpmbuild/SPECS/tomcat8.spec
