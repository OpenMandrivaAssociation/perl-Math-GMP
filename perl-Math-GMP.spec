%define upstream_name    Math-GMP
%define upstream_version 2.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:        High speed arbitrary size integer math
License:        GPL
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:  gmp-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Math::GMP was designed to be a drop-in replacement both for
Math::BigInt and for regular integer arithmetic. Unlike
BigInt,  though,  Math::GMP  uses  the  GNU  gmp  library
for  all of its calculations, as opposed to straight Perl
functions. This can result in speed improvements.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
