# TODO:
# play with --with-kde-datadir
Summary:	The core programs for the GNOME2 GUI desktop environment
Summary(pl):	Podstawowe programy ¶rodowiska graficznego GNOME2
Name:		gnome-desktop
Version:	2.2.0
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.2/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.1.5
BuildRequires:	libgnomecanvas-devel >= 2.1.5
Requires:	libgnomeui >= 2.1.5
Conflicts:	gnome-core

%description
GNOME2 (GNU Network Object Model Environment) is a user-friendly set
of applications and desktop tools to be used in conjunction with a
window manager for the X Window System. GNOME2 is similar in purpose
and scope to CDE and KDE, but GNOME2 is based completely on free
software.

This package contains applications related to GNOME2 desktop.

%description -l pl
GNOME2 (GNU Network Object Model Environment) jest zestawem
przyjaznych dla u¿ytkownika programów i narzêdzi biurkowych, których
u¿ywa siê wraz z zarz±dc± okien systemu X Window. GNOME2 przypomina
wygl±dem i zakresem funkcjonalno¶ci CDE i KDE, jednak GNOME2 opiera
siê w ca³o¶ci na wolnym oprogramowaniu.

Ten pakiet zawiera aplikacje zwi±zane w desktopem GNOME2.

%package devel
Summary:	GNOME2 desktop includes
Summary(pl):	Pliki nag³ówkowe bibliotek GNOME2 desktop
Group:          X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
GNOME2 desktop header files.

%description devel -l pl
Pliki nag³ówkowe bibliotek GNOME2 desktop.

%package static
Summary:	GNOME2 desktop static libraries
Summary(pl):	Statyczne biblioteki GNOME2 desktop
Group:          X11/Development/Libraries
Requires:	%{name} = %{version}

%description static
GNOME2 desktop static libraries.

%description static -l pl
Statyczne biblioteki GNOME2 desktop.

%prep
%setup -q

%build
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%find_lang %{name} --with-gnome --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%doc %{_mandir}/man1/*
%{_datadir}/gnome/vfolders
%{_datadir}/gnome-about
%{_datadir}/pixmaps/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-desktop-2.0
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
