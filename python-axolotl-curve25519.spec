Name: python-axolotl-curve25519
Version: 0.1.35
Release: 1%{?dist}
Summary: python wrapper for curve25519
Group: Development/Libraries
License: BSD
URL: https://github.com/tgalal/%{name}
Source: https://github.com/tgalal/%{name}/archive/master.zip
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
BuildRequires: python-devel


%description
This is python wrapper for curve25519 library with ed25519 signatures.


%prep
%setup -q -n %{name}-master


%build
python setup.py build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES


%clean
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}


%files -f INSTALLED_FILES
%defattr(-,root,root)
%{!?_licensedir:%global license %%doc}
%license LICENSE
