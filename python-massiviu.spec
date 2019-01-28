# Created by pyp2rpm-2.0.0
%global pypi_name massiviu

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        2%{?dist}
Summary:        MassivIU - Simplified "bulk" insert/update/delete for Django

License:        BSD
URL:            https://github.com/weholt/massiviu
Source0:        https://files.pythonhosted.org/packages/f2/94/48ccceea0c930a0729716b61069b4cd36d8f7a1f35474c614a66174319f4/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
Patch1:         massiviu.patch

 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Obsoletes:  python-dse

%description
MassivIU "bulk" insert/update/delete for Django
=======================================================

* Version : 1.0.0 -
Beta 1
* Author : Thomas Weholt <thomas@weholt.org>
* License : Modified BSD.
*
Status : Beta
* Url : https://github.com/weholt/massiviu.git


Background
----------

* MassivIU is a refactoring and update to the package known as DSE
(https://github.com/weholt/DSE).


%package -n     python2-%{pypi_name}
Summary:        MassivIU - Simplified "bulk" insert/update/delete for Django
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
MassivIU "bulk" insert/update/delete for Django
=======================================================

* Version : 1.0.0 -
Beta 1
* Author : Thomas Weholt <thomas@weholt.org>
* License : Modified BSD.
*
Status : Beta
* Url : https://github.com/weholt/massiviu.git


Background
----------

* MassivIU is a refactoring and update to the package known as DSE
(https://github.com/weholt/DSE).


%prep
%autosetup -n %{pypi_name}-%{version}
%autopatch -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name} 
%doc 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jan 25 2019 Joe Grund <jgrund@whamcloud.com> 0.1.0-2
- Obsolete dse

* Wed Dec 19 2018 Joe Grund <jgrund@whamcloud.com> 0.1.0-1
- Initial package.