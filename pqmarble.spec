%define git  20230311

Name:           pqmarble
Version:        2.0.0
Release:        0.%{git}.0
Summary:        A simple user-friendly terminal emulator for the GNOME desktop
License:        GPL-3.0
URL:            https://gitlab.gnome.org/raggesilver/marble/
Source:         https://gitlab.gnome.org/raggesilver/marble/-/archive/master/marble-master.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)

%description
Utility library for GNOME apps.

%prep
%autosetup -n marble-master -p1

%build
%meson
%meson_build

%install
%meson_install


%files
