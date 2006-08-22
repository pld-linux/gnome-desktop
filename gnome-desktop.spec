Summary:	The core programs for the GNOME GUI desktop environment
Summary(pl):	Podstawowe programy ¶rodowiska graficznego GNOME
Name:		gnome-desktop
Version:	2.15.92
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-desktop/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	93c5edd6c047777263e6fcaf05fc9e59
Source1:	pld-logo.svg
Patch0:		%{name}-crystalsvg.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-vfs2-devel >= 2.15.92
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.15.91
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

%description -l pl
GNOME (GNU Network Object Model Environment) jest zestawem
przyjaznych dla u¿ytkownika programów i narzêdzi biurkowych, których
u¿ywa siê wraz z zarz±dc± okien systemu X Window. GNOME przypomina
wygl±dem i zakresem funkcjonalno¶ci CDE i KDE, jednak GNOME opiera
siê w ca³o¶ci na wolnym oprogramowaniu.

Ten pakiet zawiera aplikacje zwi±zane w desktopem GNOME.

%package libs
Summary:	gnome-desktop library
Summary(pl):	Biblioteka gnome-desktop
Group:		Development/Libraries
Requires:	libgnomeui >= 2.15.91

%description libs
This package contains gnome-desktop library.

%description libs -l pl
Pakiet ten zawiera bibliotekê gnome-desktop.

%package devel
Summary:	GNOME desktop includes
Summary(pl):	Pliki nag³ówkowe bibliotek GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgnomeui-devel >= 2.15.91
Requires:	startup-notification-devel >= 0.8

%description devel
GNOME desktop header files.

%description devel -l pl
Pliki nag³ówkowe bibliotek GNOME desktop.

%package static
Summary:	GNOME desktop static libraries
Summary(pl):	Statyczne biblioteki GNOME desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
GNOME desktop static libraries.

%description static -l pl
Statyczne biblioteki GNOME desktop.

%package apidocs
Summary:	gnome-desktop API documentation
Summary(pl):	Dokumentacja API gnome-desktop
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnome-desktop API documentation.

%description apidocs -l pl
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
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{tk,ug,yo}

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
%attr(755,root,root) %{_bindir}/*
%doc %{_mandir}/man1/*
%{_datadir}/gnome-about
%{_pixmapsdir}/*
%{_omf_dest_dir}/fdl
%{_omf_dest_dir}/gnome-feedback
%{_omf_dest_dir}/gpl
%{_omf_dest_dir}/lgpl
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-desktop-2.0
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*
