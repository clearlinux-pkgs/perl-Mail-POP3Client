#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mail-POP3Client
Version  : 2.19
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-2.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SD/SDOWD/Mail-POP3Client-2.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmail-pop3client-perl/libmail-pop3client-perl_2.19-1.debian.tar.xz
Summary  : 'Perl 5 module to talk to a POP3 (RFC1939) server'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Mail-POP3Client-license = %{version}-%{release}
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

%description dev
dev components for the perl-Mail-POP3Client package.


%package license
Summary: license components for the perl-Mail-POP3Client package.
Group: Default

%description license
license components for the perl-Mail-POP3Client package.


%prep
%setup -q -n Mail-POP3Client-2.19
cd ..
%setup -q -T -D -n Mail-POP3Client-2.19 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Mail-POP3Client-2.19/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mail-POP3Client
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Mail-POP3Client/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Mail/POP3Client.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mail::POP3Client.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mail-POP3Client/deblicense_copyright
