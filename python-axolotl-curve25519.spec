%global pname axolotl-curve25519

Name: python-%{pname}
Version: 0.4.1.2
Release: 2%{?dist}
Summary: python wrapper for curve25519
License: GPLv3+
URL: https://github.com/tgalal/%{name}
Source: https://github.com/tgalal/%{name}/archive/0.4.1-2.tar.gz
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
BuildRequires: gcc

%description
This is python wrapper for curve25519 library with ed25519 signatures.


%if 0%{?fedora} && 0%{?fedora} <= 31
%package -n python2-%{pname}
Summary: python wrapper for curve25519
BuildRequires: python2-devel

%description -n python2-%{pname}
This is python wrapper for curve25519 library with ed25519 signatures.
Python 2 version.
%endif


%package -n python3-%{pname}
Summary: python wrapper for curve25519
BuildRequires: python3-devel

%description -n python3-%{pname}
This is python wrapper for curve25519 library with ed25519 signatures.
Python 3 version.


%prep
%setup -q -n %{name}-0.4.1-2


%build
%if 0%{?fedora} && 0%{?fedora} <= 31
%py2_build
%endif
%py3_build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
%if 0%{?fedora} && 0%{?fedora} <= 31
%py2_install
%endif
%py3_install


%if 0%{?fedora} && 0%{?fedora} <= 31
%files -n python2-%{pname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python2_sitearch}/*.so
%{python2_sitearch}/*.egg-info/
%endif


%files -n python3-%{pname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info/


%changelog
* Sat May  2 2020 Philippe Kueck <projects@unixadm.org> - 0.4.1.2-2
- do not build python2 packages for F32+

* Tue Nov  5 2019 Philippe Kueck <projects@unixadm.org> - 0.4.1.2-1
- new upstream version

* Fri Mar  9 2018 Philippe Kueck <projects@unixadm.org> - 0.1.35-1
- add python3 packages
