%define release_id 2

Summary: Monika PBS monitor tools
Name: monika
Version: 0.4.4
Release: %mkrel 3
Source: %{name}_%{version}-%{release_id}.tar.bz2
License: GPL
URL:http://ka-tools.sourceforge.net/
Group: Monitoring
Requires: perl-AppConfig, perl-CGI
BuildArchitectures: noarch

%description
Monika is a tool to monitor a PBS cluster. It basically shows an overall 
picture of node reservations, and job states.

%prep

%setup -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT/%{_var}/www/cgi-bin/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/

cp -a $RPM_BUILD_DIR/%{name}-%{version}/{README,INSTALL,LICENSE} $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
cp -a $RPM_BUILD_DIR/%{name}-%{version}/monika.cgi $RPM_BUILD_ROOT/%{_var}/www/cgi-bin
cp -a $RPM_BUILD_DIR/%{name}-%{version}/%{name}/*.pm $RPM_BUILD_ROOT/%{_var}/www/cgi-bin/%{name}
cp -a $RPM_BUILD_DIR/%{name}-%{version}/monika.conf $RPM_BUILD_ROOT/%{_sysconfdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc  INSTALL README LICENSE
%attr(755,root,root) %{_var}/www/cgi-bin/monika*
%config(noreplace) %{_sysconfdir}/*conf

