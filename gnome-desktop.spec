# TODO:
# play with --with-kde-datadir
Summary:	The core programs for the GNOME2 GUI desktop environment
Summary(pl):	Podstawowe programy �rodowiska graficznego GNOME2
Name:		gnome-desktop
Version:	2.3.90
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	80053aa2bce1d8b4c532b17e055fc54a
#Patch0:		%{name}-locale-sr.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.3.90
BuildRequires:	gtk+2-devel >= 2.2.3
BuildRequires:	libgnomeui-devel >= 2.3.7
BuildRequires:	libgnomecanvas-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	startup-notification-devel >= 0.5
Requires:	libgnomeui >= 2.3.7
Conflicts:	gnome-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME2 (GNU Network Object Model Environment) is a user-friendly set
of applications and desktop tools to be used in conjunction with a
window manager for the X Window System. GNOME2 is similar in purpose
and scope to CDE and KDE, but GNOME2 is based completely on free
software.

This package contains applications related to GNOME2 desktop.

%description -l pl
GNOME2 (GNU Network Object Model Environment) jest zestawem
przyjaznych dla u�ytkownika program�w i narz�dzi biurkowych, kt�rych
u�ywa si� wraz z zarz�dc� okien systemu X Window. GNOME2 przypomina
wygl�dem i zakresem funkcjonalno�ci CDE i KDE, jednak GNOME2 opiera
si� w ca�o�ci na wolnym oprogramowaniu.

Ten pakiet zawiera aplikacje zwi�zane w desktopem GNOME2.

%package devel
Summary:	GNOME2 desktop includes
Summary(pl):	Pliki nag��wkowe bibliotek GNOME2 desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	libgnomeui-devel >= 2.3.7
Requires:	startup-notification-devel >= 0.5

%description devel
GNOME2 desktop header files.

%description devel -l pl
Pliki nag��wkowe bibliotek GNOME2 desktop.

%package static
Summary:	GNOME2 desktop static libraries
Summary(pl):	Statyczne biblioteki GNOME2 desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description static
GNOME2 desktop static libraries.

%description static -l pl
Statyczne biblioteki GNOME2 desktop.

%prep
%setup -q
#%patch0 -p1

# sr_YU is latin2, sr_YU@cyrillic is cyrillic in glibc
#mv -f po/{sr.po,sr@cyrillic.po}
#mv -f po/{sr@Latn.po,sr.po}

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gnome-distributor="PLD Linux Distribution"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%doc %{_mandir}/man1/*
%{_datadir}/gnome/vfolders
%{_datadir}/gnome-about
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-desktop-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
