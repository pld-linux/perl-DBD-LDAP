%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	LDAP
Summary:	DBD::LDAP perl module
Summary(pl):	Modu³ perla DBD::LDAP
Name:		perl-DBD-LDAP
Version:	0.05
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI >= 1.03
BuildRequires:	perl-ldap >= 0.01
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::LDAP - a DBI driver for LDAP databases.

%description -l pl
DBD::LDAP - sterownik DBI do baz danych LDAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/DBD/LDAP.pm
%{perl_sitelib}/JLdap.pm
%dir %{perl_sitelib}/auto/DBD/LDAP
%{perl_sitelib}/auto/DBD/LDAP/autosplit.ix
%{_mandir}/man3/*
