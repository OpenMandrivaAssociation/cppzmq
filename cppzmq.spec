%define debug_package %nil

%define devname	%mklibname %{name} -d

%global zmqver	%(rpm -q --queryformat "%{VERSION}" %{_lib}zmq-devel )

Name:		cppzmq
Summary:	C++ binding for 0MQ
Version:	4.2.1
Release:	%mkrel 5
License:	MIT
Group:		Development/Other
Url:		https://github.com/zeromq/cppzmq
Source0:	https://github.com/zeromq/cppzmq/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Fix-cppzmqConfig.cmake-to-skip-static-lib-check.patch
BuildRequires:	cmake
BuildRequires:	git-core
BuildRequires:	pkgconfig(libzmq)

%description
C++ binding for 0MQ.

%package -n %{devname}
Summary:	C++ binding for 0MQ
Requires:	zeromq-devel = %{zmqver}
Provides:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{_lib}zeromq-devel < 4.2.2

%description -n %{devname}
C++ binding development headers for 0MQ.

%prep
%autosetup -S git_am

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{devname}
%doc README
%license LICENSE
%{_includedir}/zmq*.hpp
%dir %{_datadir}/cmake/cppzmq/
%{_datadir}/cmake/cppzmq/cppzmqConfig.cmake
%{_datadir}/cmake/cppzmq/cppzmqConfigVersion.cmake
