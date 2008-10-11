%define module Math-GMP

Summary:        High speed arbitrary size integer math
Name:           perl-%{module}
Version:        2.05
Release:        %mkrel 1
License:        GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel
BuildRequires:  gmp-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Math::GMP was designed to be a drop-in replacement both for
Math::BigInt and for regular integer arithmetic. Unlike
BigInt,  though,  Math::GMP  uses  the  GNU  gmp  library
for  all of its calculations, as opposed to straight Perl
functions. This can result in speed improvements.

%prep
%setup -q -n %{module}-%{version}

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

