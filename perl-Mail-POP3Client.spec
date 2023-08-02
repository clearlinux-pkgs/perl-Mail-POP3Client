#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mail-POP3Client
Version  : 2.21
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-2.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-2.21.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmail-pop3client-perl/libmail-pop3client-perl_2.19-1.debian.tar.xz
Summary  : 'Perl 5 module to talk to a POP3 (RFC1939) server'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Mail-POP3Client-license = %{version}-%{release}
Requires: perl-Mail-POP3Client-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
WHAT IS IT?
This is a POP3 client module for perl5.  It provides an
object-oriented interface to a POP3 server.  It can be used to write
perl-based biff clients, mail readers, or whatever.  See the inline
POD doco for more details.  (perldoc Mail::POP3Client)

%package dev
Summary: dev components for the perl-Mail-POP3Client package.
Group: Development
Provides: perl-Mail-POP3Client-devel = %{version}-%{release}
Requires: perl-Mail-POP3Client = %{version}-%{release}

%description dev
dev components for the perl-Mail-POP3Client package.


%package license
Summary: license components for the perl-Mail-POP3Client package.
Group: Default

%description license
license components for the perl-Mail-POP3Client package.


%package perl
Summary: perl components for the perl-Mail-POP3Client package.
Group: Default
Requires: perl-Mail-POP3Client = %{version}-%{release}

%description perl
perl components for the perl-Mail-POP3Client package.


%prep
%setup -q -n Mail-POP3Client-2.21
cd %{_builddir}
tar xf %{_sourcedir}/libmail-pop3client-perl_2.19-1.debian.tar.xz
cd %{_builddir}/Mail-POP3Client-2.21
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Mail-POP3Client-2.21/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mail-POP3Client
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Mail-POP3Client/1d2020afd1b3499b0c860c71903939a5c5731f0e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mail::POP3Client.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mail-POP3Client/1d2020afd1b3499b0c860c71903939a5c5731f0e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
