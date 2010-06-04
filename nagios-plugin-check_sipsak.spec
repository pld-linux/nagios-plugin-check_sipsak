# TODO
# - command and service template definition
%define		plugin	check_sipsak
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check SIP server/device
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania urządzeń i serwerów SIP
Name:		nagios-plugin-%{plugin}
# revision from cvs id
Version:	1.5
Release:	5
License:	GPL
Group:		Networking
# Source0:	http://www.nagiosexchange.org/cgi-bin/jump.cgi?ID=2249&view=File1;d=1
Source0:	%{name}
URL:		http://www.nagiosexchange.org/cgi-bin/jump.cgi?ID=2249;d=1
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
Requires:	nagios-plugins-libs
Requires:	sipsak
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(utils)

%define		plugindir	%{_prefix}/lib/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%description
This plugin will test a SIP server/device for availability and
response time using sipsak tool.

%description -l pl.UTF-8
Wtyczka Nagios-a testująca dostępność i czas odpowiedzi z urządzeń i
serwerów SIP za pomocą narzędzia sipsak.

%prep
%setup -qcT
sed -e '
	1s,#.*bin/perl,#!%{__perl},
	s#/usr/local/libexec/nagios#%{plugindir}#g
' %{SOURCE0} > %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/%{plugin}
