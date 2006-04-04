#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	LDAP
Summary:	DBD::LDAP - a DBI driver for LDAP databases
Summary(pl):	DBD::LDAP - sterownik DBI do baz danych LDAP
Name:		perl-DBD-LDAP
Version:	0.07
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66cb22e36e537e143f5bb31d2fb26243
Patch0:		%{name}-paths.patch
BuildRequires:	perl-DBI >= 1.03
BuildRequires:	perl-ldap >= 0.01
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::LDAP - a DBI driver for LDAP databases.

%description -l pl
DBD::LDAP - sterownik DBI do baz danych LDAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBD/LDAP.pm
%{perl_vendorlib}/JLdap.pm
#%{perl_vendorlib}/auto/DBD
%{_mandir}/man3/*
