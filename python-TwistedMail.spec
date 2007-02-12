%define 	module	TwistedMail

Summary:	Mail library for Twisted
Summary(pl.UTF-8):   Biblioteka Mail dla Twisted
Name:		python-%{module}
Version:	0.2.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Mail/0.2/%{module}-%{version}.tar.bz2
# Source0-md5:	bae977d92cfcb1a3a5e884262ed444cc
URL:		http://twistedmatrix.com/projects/mail
BuildRequires:	python-Twisted >= 2.0
BuildRequires:	python-devel >= 2.2
Requires:	python-Twisted >= 2.0
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
%{py_sitedir}/twisted/mail
%{py_sitedir}/twisted/plugins/twisted_mail.py*
