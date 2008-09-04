Summary:	The core programs for the GNOME GUI desktop environment
Summary(pl.UTF-8):	Podstawowe programy środowiska graficznego GNOME
Name:		gnome-desktop
Version:	2.23.91
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	a07b31b16cf8f429a131c0fb1fc15d1c
Source1:	pld-logo.svg
Patch0:		%{name}-crystalsvg.patch
Patch1:		%{name}-recently-used-apps.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.8
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	gnome-core
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.

This package contains applications related to GNOME desktop.

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest zestawem przyjaznych
dla użytkownika programów i narzędzi biurkowych, których używa się
wraz z zarządcą okien systemu X Window. GNOME przypomina wyglądem i
zakresem funkcjonalności CDE i KDE, jednak GNOME opiera się w całości
na wolnym oprogramowaniu.

Ten pakiet zawiera aplikacje związane w desktopem GNOME.

%package libs
Summary:	gnome-desktop library
Summary(pl.UTF-8):	Biblioteka gnome-desktop
Group:		X11/Libraries
Requires:	libgnomeui >= 2.22.0

%description libs
This package contains gnome-desktop library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gnome-desktop.

%package devel
Summary:	GNOME desktop includes
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgnomeui-devel >= 2.22.0
Requires:	startup-notification-devel >= 0.8

%description devel
GNOME desktop header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek GNOME desktop.

%package static
Summary:	GNOME desktop static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
GNOME desktop static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNOME desktop.

%package apidocs
Summary:	gnome-desktop API documentation
Summary(pl.UTF-8):	Dokumentacja API gnome-desktop
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnome-desktop API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API gnome-desktop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gnome-distributor="PLD Linux Distribution" \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_pixmapsdir}/gnome-logo-icon-transparent.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/gnome-logo-icon-transparent.svg

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/gnome-about
%{_mandir}/man1/gnome-about.1*
%{_datadir}/gnome-about
%{_pixmapsdir}/*
%{_desktopdir}/gnome-about.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-desktop-2.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so
%{_libdir}/libgnome-desktop-2.la
%{_includedir}/gnome-desktop-2.0
%{_pkgconfigdir}/gnome-desktop-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-desktop-2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-desktop
