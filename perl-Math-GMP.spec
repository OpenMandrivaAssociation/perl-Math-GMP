%define realname Math-GMP

Summary:        High speed arbitrary size integer math
Name:           perl-%{realname}
Version:        2.04
Release:        %mkrel 6
License:        GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{realname}
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/%{realname}-%{version}.tar.bz2
Patch0:		perl-Math-GMP-2.04-x86_64.patch
BuildRequires:  perl-devel gmp-devel
Requires:       perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Math::GMP was designed to be a drop-in replacement both for
Math::BigInt and for regular integer arithmetic. Unlike
BigInt,  though,  Math::GMP  uses  the  GNU  gmp  library
for  all of its calculations, as opposed to straight Perl
functions. This can result in speed improvements.

%prep

%setup -q -n %{realname}-%{version}
%ifarch x86_64 ppc64
%patch0 -p0
%endif

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE README
%{perl_vendorarch}/*
%{_mandir}/*/*

