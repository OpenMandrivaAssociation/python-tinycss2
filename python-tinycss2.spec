%global debug_package %{nil}
%define module tinycss2

Name:		python-tinycss2
Summary:	CSS parser for Python
Version:	1.5.1
Release:	2
Group:		System/Libraries
License:	BSD
URL:		https://www.courtbouillon.org/tinycss2/
# URL:		https://pypi.org/project/tinycss2/
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(flit)
BuildRequires:  python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(webencodings)
BuildRequires:	python%{pyver}dist(wheel)

%description
tinycss2 is a rewrite of the tinycss CSS parser for Python. It supports
It has a simpler API and is based on the more recent CSS Syntax Level 3 specification.

%prep -a
# flit 4 does not accept the upper bound. The version in the module is dynamic.
sed -i 's/flit_core >=3.2,<4/flit_core >=3.2/' pyproject.toml
sed -i "s/dynamic = \['version'\]/version = \"%{version}\"/" pyproject.toml

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
