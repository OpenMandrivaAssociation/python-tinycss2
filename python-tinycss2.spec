%global debug_package %{nil}
%define partnme tinycss2 

Name:           python-tinycss2
Summary:        CSS parser for Python
Version:        1.0.2
Release:        5
Group:          System/Libraries
License:        BSD
URL:            http://pythonhosted.org/tinycss2/
Source0:        https://github.com/Kozea/tinycss2/archive/%{partnme}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  pkgconfig(python) python-setuptools python-cython

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
#global __provides_exclude_from ^(%%{python_sitearch}|%%{python3_sitearch})/.*\\.so$

%description
tinycss2 is a rewrite of the tinycss CSS parser for Python. It supports
It has a simpler API and is based on the more recent CSS Syntax Level 3 specification.

%prep
%autosetup -n tinycss2-%{version}
dos2unix LICENSE

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}

%files
%doc LICENSE README.rst
%{python3_sitelib}/tinycss2
%{python3_sitelib}/*.egg-info
