#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-azure_devops
Version  : 6.0.0b4
Release  : 3
URL      : https://files.pythonhosted.org/packages/6c/33/73f396eb50229e681d1dbdf461a9ebdb2320383c4ac4ed697f6af1ed5184/azure-devops-6.0.0b4.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/33/73f396eb50229e681d1dbdf461a9ebdb2320383c4ac4ed697f6af1ed5184/azure-devops-6.0.0b4.tar.gz
Summary  : Python wrapper around the Azure DevOps 6.x APIs
Group    : Development/Tools
License  : MIT
Requires: pypi-azure_devops-license = %{version}-%{release}
Requires: pypi-azure_devops-python = %{version}-%{release}
Requires: pypi-azure_devops-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(msrest)

%description
No detailed description available

%package license
Summary: license components for the pypi-azure_devops package.
Group: Default

%description license
license components for the pypi-azure_devops package.


%package python
Summary: python components for the pypi-azure_devops package.
Group: Default
Requires: pypi-azure_devops-python3 = %{version}-%{release}

%description python
python components for the pypi-azure_devops package.


%package python3
Summary: python3 components for the pypi-azure_devops package.
Group: Default
Requires: python3-core
Provides: pypi(azure_devops)
Requires: pypi(msrest)

%description python3
python3 components for the pypi-azure_devops package.


%prep
%setup -q -n azure-devops-6.0.0b4
cd %{_builddir}/azure-devops-6.0.0b4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649715385
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-azure_devops
cp %{_builddir}/azure-devops-6.0.0b4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-azure_devops/1df4926d6584970d76fde7fc7b7e868270b5e225
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-azure_devops/1df4926d6584970d76fde7fc7b7e868270b5e225

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
