#undefine _debugsource_package

%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major %(echo %{version} |cut -d. -f1-2)

%define libname %mklibname SonicFrameworksOpenCollab
%define devname %mklibname SonicFrameworksOpenCollab -d
#define git 20240217

Name: sonic-frameworks-open-collab
Version: 6.26.0
Release: %{?git:0.%{git}.}1
URL: https://github.com/Sonic-DE/sonic-frameworks-open-collab
Source0: %url/archive/%version/%name-%version.tar.gz
Summary: Qt library that implements the Open Collaboration Services API
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries

BuildSystem:  cmake
BuildOption:  -DBUILD_QCH:BOOL=ON
BuildOption:	-DBUILD_WITH_QT6:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires: cmake(ECM)
# BuildRequires: qmake-qt6
BuildRequires: python
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(EGL)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(xkbcommon)
# for QCH
BuildRequires: qt6-qtbase-sql-sqlite
BuildRequires: doxygen
Requires: %{libname} = %{EVRD}

Conflicts: kf6-attica

%description
Qt library that implements the Open Collaboration Services API

%package -n %{libname}
Summary: Qt library that implements the Open Collaboration Services API
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KF6Attica

%description -n %{libname}
Qt library that implements the Open Collaboration Services API

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KF6Attica-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt library that implements the Open Collaboration Services API

%install -a
rm -rf %{buildroot}/%{_libdir}/cmake
rm -rf %{buildroot}/%{_libdir}/pkgconfig

%files
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KF6/Attica

# pending rename
# %{_libdir}/cmake/KF6Attica
# %{_libdir}/pkgconfig/KF6Attica.pc

%files -n %{libname}
%{_libdir}/libKF6Attica.so*
