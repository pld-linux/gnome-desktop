Summary:	gnome-desktop library
Summary(pl.UTF-8):	Biblioteka gnome-desktop
Name:		gnome-desktop
Version:	3.10.0
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	d9fd5ab4f8432c0a8876ed950565e0fb
Patch0:		%{name}-system-locale-archive-path.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.6.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.6
BuildRequires:	iso-codes
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.1
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.36.0
Requires:	gdk-pixbuf2 >= 2.22.0
Requires:	gsettings-desktop-schemas >= 3.6.0
Requires:	gtk+3 >= 3.4.0
Obsoletes:	gnome-desktop-libs
Obsoletes:	gnome-desktop3
Obsoletes:	gnome-desktop3-libs
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
Requires:	gsettings-desktop-schemas-devel >= 3.6.0
Requires:	glib2-devel >= 1:2.36.0
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

%description apidocs
gnome-desktop API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gnome-desktop.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gnome-distributor="PLD Linux Distribution" \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgnome-desktop-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-3.so.8
%attr(755,root,root) %{_libdir}/gnome-rr-debug
%{_datadir}/gnome/gnome-version.xml
%{_datadir}/libgnome-desktop-3.0
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
