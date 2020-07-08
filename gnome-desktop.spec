Summary:	gnome-desktop library
Summary(pl.UTF-8):	Biblioteka gnome-desktop
Name:		gnome-desktop
Version:	3.36.4
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	285d5d8a97b7564809151d401199c239
URL:		https://www.gnome.org/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.36.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.27.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	iso-codes
%ifnarch alpha ia64 m68k riscv64 sh4 sparc sparcv9 sparc64
BuildRequires:	libseccomp-devel
%endif
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libX11-devel
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
Obsoletes:	gnome-desktop-libs
Obsoletes:	gnome-desktop3
Obsoletes:	gnome-desktop3-libs
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
Obsoletes:	gnome-desktop3-devel

%description devel
GNOME desktop header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNOME desktop.

%package apidocs
Summary:	gnome-desktop API documentation
Summary(pl.UTF-8):	Dokumentacja API gnome-desktop
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	gnome-desktop3-apidocs
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
gnome-desktop API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gnome-desktop.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	-Dgnome_distributor="PLD Linux Distribution" \
	-Dgtk_doc=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-3.so.19
%attr(755,root,root) %{_libexecdir}/gnome-rr-debug
%{_datadir}/gnome/gnome-version.xml
%{_libdir}/girepository-1.0/GnomeDesktop-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so
%{_includedir}/gnome-desktop-3.0
%{_pkgconfigdir}/gnome-desktop-3.0.pc
%{_datadir}/gir-1.0/GnomeDesktop-3.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-desktop3
