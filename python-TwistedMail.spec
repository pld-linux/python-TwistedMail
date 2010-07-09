%define 	module	TwistedMail
%define		major	8.1
%define		minor	0

Summary:	Mail library for Twisted
Summary(pl.UTF-8):	Biblioteka Mail dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Mail/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	b471434356da5cdfb04dbe38802425ef
URL:		http://twistedmatrix.com/trac/wiki/TwistedMail
BuildRequires:	python-devel >= 2.2
Requires:	python-TwistedCore
Obsoletes:	python-Twisted-mail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail library for Twisted.

%description -l pl.UTF-8
Biblioteka Mail dla Twisted.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

install -d $RPM_BUILD_ROOT%{py_sitedir}
mv -f $RPM_BUILD_ROOT%{py_sitescriptdir}/* $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/mailmail
%{py_sitedir}/*.egg-info
%{py_sitedir}/twisted/mail
%{py_sitedir}/twisted/plugins/twisted_mail.py*
