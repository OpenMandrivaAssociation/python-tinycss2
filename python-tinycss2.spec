%define partnme tinycss2 

Name:           python-tinycss2
Summary:        CSS parser for Python
Version:        1.0.2
Release:        1
Group:          System/Libraries
License:        BSD
URL:            http://pythonhosted.org/tinycss2/
Source0:        https://github.com/Kozea/tinycss2/archive/%{partnme}-%{version}.tar.gz

BuildRequires:  dos2unix
BuildRequires:  python-devel python-setuptools python-cython
BuildRequires:  python2-devel python2-setuptools python2-cython

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
#global __provides_exclude_from ^(%%{python_sitearch}|%%{python3_sitearch})/.*\\.so$

%description
tinycss2 is a rewrite of the tinycss CSS parser for Python. It supports
It has a simpler API and is based on the more recent CSS Syntax Level 3 specification.


%package -n python2-tinycss2
Summary:        CSS parser for Python
Group:          System/Libraries

%description -n python2-tinycss2
tinycss2 is a rewrite of the tinycss CSS parser for Python. It supports
It has a simpler API and is based on the more recent CSS Syntax Level 3 specification.

%prep
%autosetup -n tinycss2-%{version}
dos2unix LICENSE

rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python2}|'

%build
%{__python} setup.py build

cd %{py2dir}
%{__python2} setup.py build
cd -

%install
%{__python} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}

cd %{py2dir}
%{__python2} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}
cd -

%files
%doc LICENSE README.rst
%{python3_sitelib}/*/*

%files -n python2-tinycss2
%doc LICENSE README.rst
%{python2_sitelib}/*/*

