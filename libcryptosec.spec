Summary: libcryptosec
Name: libcryptosec
Version: 2.2.8
Release: 1
Source0: %{name}-%{version}.zip
License: GPL
Group: Development/Tools
BuildArch: i386
Requires: libp11
%description
libcryptosec is an OpenSSL c++ wrapper with extra features

%prep
%setup -q
%build
make
strip libcryptosec.so
%install
make install

%files
#arquivos contidos no pacote
%defattr(-,root,root)
%{_libdir}/libcryptosec.so
%{_includedir}/libcryptosec/

%changelog
* Mon Sep 19 2016 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.8
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Fixes bug with empty DN when using alterSubject.
- Automated test cases for altersubject. 

* Fri Jun 17 2016 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.7
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Add backward compability with previous openssl version  in alterSubject. 

* Wed May 11 2016 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.6
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Fixed bug introduced last update in the alterSubject function.

* Mon Apr 18 2016 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.5
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Fixed bug where it was not possible to use alterSubject to change Name Entries values.

* Mon Aug 17 2015 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.4
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Added functions to Certificate Builder that keep the subject's string format field when building from a RDNSequence.

* Wed Aug 05 2015 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.3
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Added functions to Certificate Builder that keep the subject's string format field when building from a CSR.

* Wed Jul 22 2015 Lucas Perin <lucas.perin@posgrad.ufsc.br> - 2.2.2
- Must use OpenSSL 1.0.1h with Brainpool patch if using Brainpool curves;
- Added functions to Certificate and CRL Builder that keep the subject's string format in the Issuer field.  

* Wed Apr 15 2015 Lucas Petry
- Version 2.2.1 RHEL5.5 (OpenSSL 1.0.2.a)
* Wed Dec 17 2014 Lucas Petry
- Version 2.2.0 RHEL5.5 (OpenSSL 1.0.1.h com patch Brainpool)
* Wed Nov 19 2014 Lucas Petry
- Version 2.1.2 RHEL5.5 (OpenSSL 1.0.1.h)
* Tue Sep 02 2014 Lucas Perin
- Version 2.1.1 RHEL5.5 (OpenSSL 1.0.1.h)
* Mon May 24 2010 Cristian Thiago Moecke
- Version 2.0.1 RHEL5.5 (OpenSSL 1.0.0)
* Thu Dec 08 2009 Cristian Thiago Moecke
- Version 1.5.0
* Wed Jun 17 2009 Cristian Thiago Moecke
- Version 1.3.7
* Thu Mar 31 2008 Marcelo Carlomagno Carlos
- Version 1.3.1
* Thu Mar 01 2007 Marcelo Carlomagno Carlos
- Version 1.2.0
* Tue Nov 11 2006 Marcelo Carlomagno Carlos
- Beta version 1.1.0
