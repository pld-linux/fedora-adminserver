Summary:	Fedora Admin Server - administration engine
Summary(pl):	Fedora Admin Server - silnik administracyjny
Name:		fedora-adminserver
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	ab7b4809b135e28f114c8367264e9394
URL:		http://directory.fedora.redhat.com/wiki/AdminServer
#BuildRequires:	apr-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel >= 4.0
#BuildRequires:	fedora-adminutil
#BuildRequires:	fedora-setuputil
BuildRequires:	gdbm-devel >= 1.6
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtermcap-devel
BuildRequires:	mozldap-devel
BuildRequires:	net-snmp-devel >= 5.2.1
BuildRequires:	nspr-devel >= 4.4.1
BuildRequires:	nss-devel
BuildRequires:	rpmbuild(macros) >= 1.228
#BuildRequires:	which
#BuildRequires:	zip
#Requires:	libicu >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Admin Server is the HTTP based adminstration engine used by the
Directory Server to run the console and the web based applications
such as Admin Express, DS Gateway, Org Chart, and others. It consists
of a collection of CGI binary programs and scripts, HTML pages and
Javascript code, the adminserver console module, setuputil modules and
programs, and config files. It was formerly based on the Netscape
Enterprise Server but has been ported to use the Apache 2.x webserver
using the Worker model (multi-threaded mode, not multi process). The
main HTTP functionality consists of the Apache module mod_admserv, and
the TLS/SSL functionality is provided by the Apache module mod_nss.
Support for starting up servers on low port numbers is provided by
mod_restartd.

%description -l pl
Admin Server to oparty na HTTP silnik administracyjny u�ywany przez
Directory Server do uruchamiania konsoli i aplikacji WWW takich jak
Admin Express, DS Gateway, Org Chart i innych. Sk�ada si� z zestawu
program�w binarnych i skrypt�w CGI, stron HTML i kodu w
Javascripcie, modu�u konsoli adminservera, modu��w i program�w
setuputil oraz plik�w konfiguracyjnych. Wcze�niej by� oparty na
serwerze Netscape Enterprise ale zosta� przeportowany do u�ywania
serwera WWW Apache 2.x w modelu Worker (wielow�tkowym, nie
wieloprocesowym). G��wna funkcjonalno�� HTTP sk�ada si� z modu�u
Apache'a mod_admserv, a funkcjonalno�� TLS/SSL jest dostarczana przez
modu� Apache'a mod_nss. Obs�uga uruchamiania serwer�w na niskich
numerach port�w jest dostarczana przez mod_restartd.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	MAKE="%{__make}"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
