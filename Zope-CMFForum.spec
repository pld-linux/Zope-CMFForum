%define		zope_subname	CMFForum
Summary:	CMMForum is a Zope product that Anonymous can post by default.
Summary(pl):	CMMForum jest dodatkiem do Zope daj±cy mo¿liwo¶æ wys³ania e-maila
Name:		Zope-%{zope_subname}
Version:	1.0
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://telia.dl.sourceforge.net/sourceforge/collective/%{zope_subname}-%{version}.tgz
# Source0-md5:	dc9ee26b8c78a32238afd2540dcf258c

URL:		http://sourceforge.net/projects/collective
Requires:	python >= 2.2
Requires:	python-modules >= 2.2
Requires:	python-libs >= 2.2
Requires:	Zope
Requires:	CMF
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# define	python_prefix           %(echo `python -c "import sys; print sys.prefix"`)
# define        python_version          %(echo `python -c "import sys; print sys.version[:3]"`)
# define        python_libdir           %{python_prefix}/lib/python%{python_version}
# define        python_sitedir          %{python_libdir}/site-packages

%define		zope_lib	/usr/lib/zope/Addons
%define 	product_dir	/usr/lib/zope/Products

%description
CMMForum is a Zope product - Anonymous can post by default but cant
add Attachments - Anonumous can set Author and e-mail fields. Logged
in user gets 'username' as Author and email from preferences. Security
cleanup.

%description -l pl
CMMForum jest dodatkiem do Zope umo¿liwiaj±cy dodanie formy wysy³ania
e-mail bez mo¿liwo¶ci wysy³ania za³±czników. Anonymous mo¿e ustawiæ
adres e-mail, a je¿eli zaloguje siê jako konkretny u¿ytkownik, wtedy
pobierane s± odpowiednie pola z preferencji. Dodatek sprawdzony pod
wzglêdem bezpieczeñstwa.

%prep
%setup -q -c %{zope_subname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zope_lib}
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{zope_lib}/%{zope_subname}
rm -rf $RPM_BUILD_ROOT%{zope_lib}/%{zope_subname}/*.txt
ln -s %{zope_lib}/%{zope_subname}/ $RPM_BUILD_ROOT%{product_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/*.txt
%{zope_lib}
%{product_dir}
