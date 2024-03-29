Summary:	Fedora Admin Server - administration engine
Summary(pl.UTF-8):	Fedora Admin Server - silnik administracyjny
Name:		fedora-adminserver
# note: don't try to "update" to 7.1 dated 20051007, it's older than 1.0
Version:	1.0.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	c4c209e2c387a41d8519a52cbe9323a6
URL:		http://directory.fedora.redhat.com/wiki/AdminServer
BuildRequires:	cyrus-sasl-devel
BuildRequires:	db-devel >= 4.0
BuildRequires:	fedora-adminutil-devel >= 1.0
BuildRequires:	fedora-setuputil >= 1.0
BuildRequires:	gdbm-devel >= 1.6
BuildRequires:	libicu-devel >= 3.4
BuildRequires:	libicu-devel < 3.5
BuildRequires:	libstdc++-devel
BuildRequires:	mozldap-devel >= 6.0
BuildRequires:	ncurses-devel
BuildRequires:	net-snmp-devel >= 5.2.1
BuildRequires:	nspr-devel >= 1:4.4.1
BuildRequires:	nss-devel >= 3
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	sed >= 4.0
#BuildRequires:	which
#BuildRequires:	zip
Requires:	apache-mod_admserv >= 1.0
Requires:	apache-mod_nss >= 1.0
Requires:	apache-mod_restartd >= 1.0
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

%description -l pl.UTF-8
Admin Server to oparty na HTTP silnik administracyjny używany przez
Directory Server do uruchamiania konsoli i aplikacji WWW takich jak
Admin Express, DS Gateway, Org Chart i innych. Składa się z zestawu
programów binarnych i skryptów CGI, stron HTML i kodu w
Javascripcie, modułu konsoli adminservera, modułów i programów
setuputil oraz plików konfiguracyjnych. Wcześniej był oparty na
serwerze Netscape Enterprise ale został przeportowany do używania
serwera WWW Apache 2.x w modelu Worker (wielowątkowym, nie
wieloprocesowym). Główna funkcjonalność HTTP składa się z modułu
Apache'a mod_admserv, a funkcjonalność TLS/SSL jest dostarczana przez
moduł Apache'a mod_nss. Obsługa uruchamiania serwerów na niskich
numerach portów jest dostarczana przez mod_restartd.

%prep
%setup -q

# don't BR ldapsdk
sed -i -e 's/build: ldapjdk nmcjdk/build:/' admserv/console/Makefile

%build
%{__make} buildOxygen \
	ARCH_DEBUG="%{rpmcflags}" \
	ARCH_OPT="%{rpmcflags}" \
	BUILD_DEBUG=%{?debug:full}%{!?debug:optimize} \
	CC="%{__cc}" \
	CCC="%{__cxx}" \
	CXX="%{__cxx}" \
	MAKE="%{__make}" \
	CURSES="-lncurses" \
	NSOS_TEST=PLD \
	MOD_ADMSERV= \
	MOD_NSS= \
	MOD_RESTARTD= \
	ADMINUTIL_INCLUDE=/usr/include/adminutil-1.0 \
	ADMINUTIL_LIBPATH=%{_libdir} \
	ICU_BINPATH=/usr/bin \
	ICU_INCLUDE=/usr/include \
	ICU_LIBPATH=%{_libdir} \
	LDAPOBJNAME='libldap$(LDAP_LIB_VERSION)$(LDAP_DLL_PRESUF).$(LDAP_DLL_SUFFIX)' \
	LDAPSDK_INCLUDE=/usr/include/mozldap \
	LDAPSDK_LIBPATH=%{_libdir} \
	NSPR_INCLUDE=/usr/include/nspr \
	NSPR_LIBPATH=%{_libdir} \
	SECURITY_INCLUDE=/usr/include/nss \
	SECURITY_LIBPATH=%{_libdir} \
	SETUPUTIL_INCLUDE=/usr/include/fedora-setuputil \
	SETUPUTIL_LIBPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%files
#%defattr(644,root,root,755)
