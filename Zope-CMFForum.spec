%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFForum
Summary:	A Zope product that Anonymous can post by default
Summary(pl):	Dodatek do Zope daj±cy mo¿liwo¶æ wys³ania e-maila
Name:		Zope-%{zope_subname}
Version:	1.0
Release:	7
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tgz
# Source0-md5:	dc9ee26b8c78a32238afd2540dcf258c
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope >= 2.5.1
Requires:	Zope-CMF >= 1.3
Requires(post,postun):  /usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF

%description
CMMForum is a Zope product - Anonymous can post by default but can't
add Attachments - Anonymous can set Author and e-mail fields. Logged
in user gets 'username' as Author and email from preferences. Security
cleanup.

%description -l pl
CMMForum jest dodatkiem do Zope umo¿liwiaj±cym dodanie formy wysy³ania
e-mailem bez mo¿liwo¶ci wysy³ania za³±czników. Anonymous mo¿e ustawiæ
adres e-mail, a je¿eli zaloguje siê jako konkretny u¿ytkownik, wtedy
pobierane s± odpowiednie pola z preferencji. Dodatek sprawdzony pod
wzglêdem bezpieczeñstwa.

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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt HISTORY.txt INSTALL.txt README.txt TODO.txt
%{_datadir}/%{name}
