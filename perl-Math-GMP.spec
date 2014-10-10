%define upstream_name    Math-GMP
%define upstream_version 2.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:        High speed arbitrary size integer math
License:        GPL
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Math/Math-GMP-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:  gmp-devel

%description
Math::GMP was designed to be a drop-in replacement both for
Math::BigInt and for regular integer arithmetic. Unlike
BigInt,  though,  Math::GMP  uses  the  GNU  gmp  library
for  all of its calculations, as opposed to straight Perl
functions. This can result in speed improvements.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%clean

%files
%doc LICENSE README
%{perl_vendorarch}/*
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.60.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 2.60.0-1mdv2010.0
+ Revision: 444248
- update to 2.06

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.0
+ Revision: 407800
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdv2009.1
+ Revision: 292556
- drop x86_64-only patch, useless now
- update to new version 2.05

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.04-7mdv2009.0
+ Revision: 257815
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.04-6mdv2009.0
+ Revision: 245840
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.04-4mdv2008.1
+ Revision: 152126
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-3mdv2008.0
+ Revision: 86600
- rebuild


* Thu Apr 13 2006 Oden Eriksson <oeriksson@mandriva.com> 2.04-2mdk
- Apply patch to fix broken testsuite on 64-bit arches (CPAN RT#12751)

* Wed Feb 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.04-1mdk
- 2.04

* Thu Nov 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.03-2mdk
- Rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 2.03-1mdk
- New package


