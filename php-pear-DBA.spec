%define		_class		DBA
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	11
Summary:	Berkeley-style Database Class
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/DBA/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Implements a DBM-style database using either PHP's DBA functions or a
simple DBM class written in PHP. Also provides a relational database
system with support for selects, joins, sorts, projects, multiple
tables, type checking, autoincrements and more.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{_class}-%{version}/docs/*
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-8mdv2012.0
+ Revision: 741838
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7
+ Revision: 679279
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-6mdv2011.0
+ Revision: 613625
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.1-5mdv2010.1
+ Revision: 479285
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-4mdv2010.0
+ Revision: 440970
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2009.1
+ Revision: 321947
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2009.0
+ Revision: 236819
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2008.0
+ Revision: 15647
- 1.1.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2007.0
+ Revision: 81479
- Import php-pear-DBA

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package (PLD import)

