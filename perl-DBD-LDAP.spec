%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	LDAP
Summary:	DBD::LDAP Perl module
Summary(cs):	Modul DBD::LDAP pro Perl
Summary(da):	Perlmodul DBD::LDAP
Summary(de):	DBD::LDAP Perl Modul
Summary(es):	Módulo de Perl DBD::LDAP
Summary(fr):	Module Perl DBD::LDAP
Summary(it):	Modulo di Perl DBD::LDAP
Summary(ja):	DBD::LDAP Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	DBD::LDAP ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul DBD::LDAP
Summary(pl):	Modu³ Perla DBD::LDAP
Summary(pt):	Módulo de Perl DBD::LDAP
Summary(pt_BR):	Módulo Perl DBD::LDAP
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl DBD::LDAP
Summary(sv):	DBD::LDAP Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl DBD::LDAP
Summary(zh_CN):	DBD::LDAP Perl Ä£¿é
Name:		perl-DBD-LDAP
Version:	0.05
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
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
%patch0 -p1

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
%{perl_sitelib}/auto/DBD
%{_mandir}/man3/*
