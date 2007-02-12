%define		zope_subname	CMFForum
Summary:	A Zope product that Anonymous can post by default
Summary(pl.UTF-8):	Dodatek do Zope dający możliwość wysłania e-maila
Name:		Zope-%{zope_subname}
Version:	1.0
Release:	10
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tgz
# Source0-md5:	dc9ee26b8c78a32238afd2540dcf258c
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.5.1
Requires:	Zope-CMF >= 1:1.4
Conflicts:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CMMForum is a Zope product - Anonymous can post by default but can't
add Attachments - Anonymous can set Author and e-mail fields. Logged
in user gets 'username' as Author and email from preferences. Security
cleanup.

%description -l pl.UTF-8
CMMForum jest dodatkiem do Zope umożliwiającym dodanie formy wysyłania
e-mailem bez możliwości wysyłania załączników. Anonymous może ustawić
adres e-mail, a jeżeli zaloguje się jako konkretny użytkownik, wtedy
pobierane są odpowiednie pola z preferencji. Dodatek sprawdzony pod
względem bezpieczeństwa.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,interfaces,skins,*.py,*.gif,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt HISTORY.txt INSTALL.txt README.txt TODO.txt
%{_datadir}/%{name}
