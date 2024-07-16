%define debug_package %nil

%define devname	%mklibname %{name} -d

%global zmqver	%(rpm -q --queryformat "%{VERSION}" %{_lib}zmq-devel )

Name:		cppzmq
Summary:	C++ binding for 0MQ
Version:	4.10.0
Release:	1
License:	MIT
Group:		Development/Other
Url:		https://github.com/zeromq/cppzmq
Source0:	https://github.com/zeromq/cppzmq/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:		0001-Skip-zeromq-static-targets.patch
#Patch1:		0001-Drop-static-targets-from-FindZeroMQ.cmake.patch
#Patch2:		0001-Fix-FindZeroMQ.cmake-install-location.patch
BuildSystem:	cmake
BuildOption:	-DCPPZMQ_BUILD_TESTS:BOOL=OFF
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

%files -n %{devname}
#doc README
%license LICENSE
%{_includedir}/zmq*.hpp
%dir %{_datadir}/cmake/cppzmq/
%{_datadir}/cmake/cppzmq/*.cmake
%{_datadir}/cmake/cppzmq/libzmq-pkg-config/FindZeroMQ.cmake
%{_libdir}/pkgconfig/cppzmq.pc
