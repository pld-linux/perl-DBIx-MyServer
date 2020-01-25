#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	DBIx
%define	pnam	MyServer
Summary:	DBIx::MyServer - Server-side implementation of the MySQL network protocol
Name:		perl-DBIx-MyServer
Version:	0.42
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ee5f09c206aae6af3f10c467c847a63
URL:		http://search.cpan.org/dist/DBIx-MyServer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-SHA1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module emulates the server side of the MySQL protocol. This
allows you to run your own faux-MySQL servers which can accept
commands and queries and reply accordingly.

Please see examples/myserver.pl for a system that allows building
functional mysql servers that rewrite queries or return arbitary data.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/myserver.pl
%{perl_vendorlib}/DBIx/*.pm
%{perl_vendorlib}/DBIx/MyServer
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
