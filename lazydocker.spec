%global debug_package %{nil}

Name:		lazydocker
Version:	0.24.1
Release:	2
Source0:	https://github.com/jesseduffield/lazydocker/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.gz
Summary:	The lazier way to manage everything docker
URL:		https://github.com/jesseduffield/lazydocker
License:	MIT
Group:		System/Configuration/Other
BuildRequires:	go


%description
%summary.

%prep
%autosetup -p1
tar zxf %{S:1}

%build
export GOFLAGS="-buildmode=pie -mod=readonly -modcacherw"
go build -o %{name}

%install
install -Dpm775 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
