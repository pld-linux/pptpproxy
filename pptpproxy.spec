Summary:	Proxy server for pptp protocol
Summary(pl):	Serwer proxy dla protoko³u pptp
Name:		pptpproxy
Version:	1.10
Release:	0.1
License:	GPL
Source0:	http://www.mgix.com/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	e6847e8c4a04bfcfb402e796a2f364b3
Group:		Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proxy server for pptp protocol.

%description -l pl
Serwer proxy dla protoko³u pptp

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install pptpproxy $RPM_BUILD_ROOT%{_sbindir}
install pptpproxy.8 $RPM_BUILD_ROOT/%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc todo.txt
%attr(0755,root,root) %{_sbindir}/pptpproxy
%{_mandir}/man8/*
