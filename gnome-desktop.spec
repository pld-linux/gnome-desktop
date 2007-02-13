Summary:	The core programs for the GNOME GUI desktop environment
Summary(pl.UTF-8):	Podstawowe programy środowiska graficznego GNOME
Name:		gnome-desktop
Version:	2.16.3
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-desktop/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	42c21d18589f4955bb0d70c82236d999
Source1:	pld-logo.svg
Patch0:		%{name}-crystalsvg.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-recently-used-apps.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gnome-vfs2-devel >= 2.16.3
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	gnome-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set
of applications and desktop tools to be used in conjunction with a
window manager for the X Window System. GNOME is similar in purpose
and scope to CDE and KDE, but GNOME is based completely on free
software.

This package contains applications related to GNOME desktop.

%description -l pl.UTF-8
GNOME (GNU Network Object Model Environment) jest zestawem
przyjaznych dla użytkownika programów i narzędzi biurkowych, których
używa się wraz z zarządcą okien systemu X Window. GNOME przypomina
wyglądem i zakresem funkcjonalności CDE i KDE, jednak GNOME opiera
się w całości na wolnym oprogramowaniu.

Ten pakiet zawiera aplikacje związane w desktopem GNOME.

%package libs
Summary:	gnome-desktop library
Summary(pl.UTF-8):	Biblioteka gnome-desktop
Group:		Development/Libraries
Requires:	libgnomeui >= 2.16.1

%description libs
This package contains gnome-desktop library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gnome-desktop.

%package devel
Summary:	GNOME desktop includes
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgnomeui-devel >= 2.16.1
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
%patch2 -p1

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

%find_lang %{name} --with-gnome --all-name

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-about
%doc %{_mandir}/man1/gnome-about.1*
%{_datadir}/gnome-about
%{_pixmapsdir}/*
%{_omf_dest_dir}/fdl
%{_omf_dest_dir}/gpl
%{_omf_dest_dir}/lgpl
%{_desktopdir}/gnome-about.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-desktop-2.so.*.*.*

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
