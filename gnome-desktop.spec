#
# Conditional build:
%bcond_without	apidocs	# API documentation
%bcond_without	gtk3	# legacy libgnome-desktop-3.0
%bcond_without	gtk4	# libgnome-*-4 libraries

Summary:	gnome-desktop library
Summary(pl.UTF-8):	Biblioteka gnome-desktop
Name:		gnome-desktop
Version:	42.4
Release:	2
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-desktop/42/%{name}-%{version}.tar.xz
# Source0-md5:	d1523a08b36cf35d6891d1bf897c07de
URL:		https://www.gnome.org/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.36.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.27.0
%if %{with gtk3}
BuildRequires:	gtk+3-devel >= 3.4.0
%endif
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
%if %{with gtk4}
BuildRequires:	gtk4-devel >= 4.4.0
%endif
BuildRequires:	iso-codes
%ifnarch alpha ia64 m68k sh4 sparc sparcv9 sparc64
BuildRequires:	libseccomp-devel
%endif
BuildRequires:	libxkbregistry-devel
BuildRequires:	meson >= 0.56.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libXext-devel >= 1.1
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	gdk-pixbuf2 >= 2.36.5
Requires:	glib2 >= 1:2.54.0
Requires:	gsettings-desktop-schemas >= 3.27.0
Requires:	gtk+3 >= 3.4.0
Requires:	iso-codes
Requires:	xkeyboard-config
Requires:	xorg-lib-libXext >= 1.1
Requires:	xorg-lib-libXrandr >= 1.3
Obsoletes:	gnome-desktop-libs < 3.0.0
Obsoletes:	gnome-desktop3 < 3.0.0
Obsoletes:	gnome-desktop3-libs < 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This package contains gnome-desktop library.

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest zestawem przyjaznych
dla użytkownika programów i narzędzi biurkowych, których używa się
wraz z zarządcą okien systemu X Window. GNOME przypomina wyglądem i
zakresem funkcjonalności CDE i KDE, jednak GNOME opiera się w całości
na wolnym oprogramowaniu.

Pakiet ten zawiera bibliotekę gnome-desktop.

%package devel
Summary:	GNOME desktop includes
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.54.0
Requires:	gsettings-desktop-schemas-devel >= 3.27.0
Requires:	gtk+3-devel >= 3.4.0
Obsoletes:	gnome-desktop-static < 3.2.0
Obsoletes:	gnome-desktop3-devel < 3.0.0
Obsoletes:	gnome-desktop3-static < 3.0.0

%description devel
GNOME desktop header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNOME desktop.

%package apidocs
Summary:	gnome-desktop API documentation
Summary(pl.UTF-8):	Dokumentacja API gnome-desktop
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	gnome-desktop3-apidocs < 3.0.0
BuildArch:	noarch

%description apidocs
gnome-desktop API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gnome-desktop.

%package -n gnome-desktop4
Summary:	gnome-desktop 4 libraries
Summary(pl.UTF-8):	Biblioteki gnome-desktop 4
Group:		Libraries

%description -n gnome-desktop4
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This package contains gnome-desktop 4 libraries.

%description -n gnome-desktop4 -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest zestawem przyjaznych
dla użytkownika programów i narzędzi biurkowych, których używa się
wraz z zarządcą okien systemu X Window. GNOME przypomina wyglądem i
zakresem funkcjonalności CDE i KDE, jednak GNOME opiera się w całości
na wolnym oprogramowaniu.

Pakiet ten zawiera biblioteki gnome-desktop 4.

%package -n gnome-desktop4-devel
Summary:	GNOME desktop 4 includes
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek GNOME desktop 4
Group:		Development/Libraries
Requires:	gnome-desktop4 = %{version}-%{release}

%description -n gnome-desktop4-devel
GNOME desktop 4 includes.

%description -n gnome-desktop4-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek GNOME desktop 4.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	%{!?with_gtk4:-Dbuild_gtk4=false} \
	-Dgnome_distributor="PLD Linux Distribution" \
	%{?with_apidocs:-Dgtk_doc=true} \
	%{!?with_gtk3:-Dlegacy_library=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n gnome-desktop4 -p /sbin/ldconfig
%postun	-n gnome-desktop4 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-3.so.19
%dir %{_libexecdir}/gnome-desktop-debug
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/gnome-rr-debug
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/test-desktop-thumbnail
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/test-idle-monitor
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/test-languages
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/test-pnp-ids
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/test-wall-clock
%attr(755,root,root) %{_libexecdir}/gnome-desktop-debug/test-xkb-info
%{_datadir}/gnome/gnome-version.xml
%{_libdir}/girepository-1.0/GnomeDesktop-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so
%{_datadir}/gir-1.0/GnomeDesktop-3.0.gir
%{_includedir}/gnome-desktop-3.0
%{_pkgconfigdir}/gnome-desktop-3.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-desktop3
%endif

%if %{with gtk4}
%files -n gnome-desktop4
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/GnomeBG-4.0.typelib
%{_libdir}/girepository-1.0/GnomeDesktop-4.0.typelib
%{_libdir}/girepository-1.0/GnomeRR-4.0.typelib
%attr(755,root,root) %{_libdir}/libgnome-bg-4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-bg-4.so.1
%attr(755,root,root) %{_libdir}/libgnome-desktop-4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-4.so.1
%attr(755,root,root) %{_libdir}/libgnome-rr-4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-rr-4.so.1

%files -n gnome-desktop4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-bg-4.so
%attr(755,root,root) %{_libdir}/libgnome-desktop-4.so
%attr(755,root,root) %{_libdir}/libgnome-rr-4.so
%{_datadir}/gir-1.0/GnomeBG-4.0.gir
%{_datadir}/gir-1.0/GnomeDesktop-4.0.gir
%{_datadir}/gir-1.0/GnomeRR-4.0.gir
%{_includedir}/gnome-desktop-4.0
%{_pkgconfigdir}/gnome-bg-4.pc
%{_pkgconfigdir}/gnome-desktop-4.pc
%{_pkgconfigdir}/gnome-rr-4.pc
%endif
