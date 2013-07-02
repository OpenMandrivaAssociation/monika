%define release_id 2

Summary: PBS monitor tools
Name: monika
Version: 0.4.4
Release: 7
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
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}/%{_var}/www/cgi-bin/%{name}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/

cp -a $RPM_BUILD_DIR/%{name}-%{version}/monika.cgi %{buildroot}/%{_var}/www/cgi-bin
cp -a $RPM_BUILD_DIR/%{name}-%{version}/%{name}/*.pm %{buildroot}/%{_var}/www/cgi-bin/%{name}
cp -a $RPM_BUILD_DIR/%{name}-%{version}/monika.conf %{buildroot}/%{_sysconfdir}/

%clean

%files 
%doc  INSTALL README LICENSE
%attr(755,root,root) %{_var}/www/cgi-bin/monika*
%config(noreplace) %{_sysconfdir}/*conf



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-6mdv2010.0
+ Revision: 430087
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-5mdv2009.0
+ Revision: 252689
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-3mdv2008.1
+ Revision: 133069
- do not try to reinvent %%doc
- kill re-definition of %%buildroot on Pixel's request
- kill packager tag
- use %%mkrel


* Sat Apr 02 2005 <guibo@guibo.mdkc.com> 0.4.4-2mdk
- fix make install

* Fri Mar 18 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.4.4-1mdk
- release 0.4.4-2

* Sat Sep 20 2003 aginies <aginies@mandrakesoft.com> 0.4.3-1mdk
- using .tar.bz2
- adjusting release to 1mdk

* Fri May 16 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.4.3
- rename version

* Thu May 15 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.4-3
- node state bug fixed

* Tue Mar 25 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.4-2
- New look for reservation table.

* Mon Mar 24 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.4-1
- bug fixes
- add reservation table width param: nodes_per_line
- config file self documentation revisited

* Tue Mar 18 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.3-1
- by property node view
- tooltips, back links
- change perl module files location from perl_vendor to the cgi-bin dir

* Wed Mar 12 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.2-1
- code cleaning
- parse `qstat -f' output rather than `qstat -as'
- add detailed status pages

* Fri Mar 07 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.1-2
- Bug fixes

* Wed Feb 26 2003 Pierre Neyron <pierre.neyron@imag.fr> 0.1-1
- First attempt.

