%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check SIP server/device
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania urządzeń i serwerów SIP
Name:		nagios-plugin-check_sipsak
# revision from cvs id
Version:	1.5
Release:	4
License:	GPL
Group:		Networking
# Source0:	http://www.nagiosexchange.org/cgi-bin/jump.cgi?ID=2249&view=File1;d=1
Source0:	%{name}
URL:		http://www.nagiosexchange.org/cgi-bin/jump.cgi?ID=2249;d=1
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
Requires:	sipsak
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_prefix}/lib/nagios/plugins
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
s#/usr/local/libexec/nagios#%{_plugindir}#g
' %{SOURCE0} > nagios-plugin-check_sipsak

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
install nagios-plugin-check_sipsak $RPM_BUILD_ROOT%{_plugindir}/check_sipsak

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*
