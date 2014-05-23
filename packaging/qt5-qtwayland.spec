# The MIT License (MIT)
# 
# Copyright (c) 2013 Tomasz Olszak <olszak.tomasz@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This file is based on qtwayland.spec from Mer project
# http://merproject.org
%bcond_with wayland
%bcond_with x

Name:       qt5-qtwayland
Summary:    Qt Wayland compositor
Version:    5.3.0
Release:    0
Group:      Base/Libraries
License:    LGPL-2.1+ or GPL-3.0
URL:        http://qt.digia.com
Source0:    %{name}-%{version}.tar.bz2
%if %{with wayland}
Source1001: %{name}.manifest
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PlatformSupport)
%if %{with x}
BuildRequires:  pkgconfig(Qt5DBus)
%endif
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libffi-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(mtdev)
%endif
%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor for wayland_egl
%if %{with wayland}
%package devel
Summary:        Qt Wayland compositor - development files
Group:          Base/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor development files for wayland_egl


#### Build section

%prep
%setup -q -n %{name}-%{version}/qtwayland
cp %{SOURCE1001} .

%build
export QTDIR=/usr/share/qt5
export QT_WAYLAND_GL_CONFIG=wayland_egl
touch .git
qmake -qt=5 

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake_install

%fdupes %{buildroot}%{_includedir}


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig


#### File section

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5WaylandClient.so.5*
%{_libdir}/qt5/plugins/platforms/libqwayland-generic.so
%{_libdir}/qt5/plugins/platforms/libqwayland-egl.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-client/libwayland-egl.so
%{_libdir}/qt5/plugins/wayland-graphics-integration-client/libdrm-egl-server.so


%files devel
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_libdir}/libQt5WaylandClient.so
%{_includedir}/qt5/*
%{_libdir}/libQt5WaylandClient.la
%{_libdir}/libQt5WaylandClient.prl
%{_libdir}/pkgconfig/Qt5WaylandClient.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_waylandclient.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_waylandclient_private.pri
%{_libdir}/qt5/bin/qtwaylandscanner
%{_libdir}/cmake
%endif
#### No changelog section, separate $pkg.changes contains the history
