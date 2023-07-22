%define git  20230311
%define major 2

%define libname %mklibname pqmarble
%define devname %mklibname -d pqmarble
%define girname %mklibname pqmarble-gir

Name:           pqmarble
Version:        2.0.0
Release:        0.%{git}.0
Summary:        Utility library for GNOME apps.
License:        GPL-3.0
URL:            https://gitlab.gnome.org/raggesilver/marble/
Source:         https://gitlab.gnome.org/raggesilver/marble/-/archive/master/marble-master.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Utility library for GNOME apps.

%package -n %{libname}
Summary:        Shared library for %{name}
Requires:	%{girname} = %{version}-%{release}

%description -n %{libname}
Library for gnome utility pqmarble.

%package -n %{girname}
Summary:        Introspection file for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
This package contains introspection file for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -n marble-master -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libpqmarble.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/PQMarble-2.typelib

%files -n %{devname}
%{_includedir}/pqmarble.h
%{_libdir}/libpqmarble.so
%{_libdir}/pkgconfig/pqmarble.pc
%{_datadir}/gir-1.0/PQMarble-2.gir
%{_datadir}/vala/vapi/pqmarble.vapi
%{_datadir}/vala/vapi/pqmarble.deps
