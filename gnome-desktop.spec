# TODO:
# play with --with-kde-datadir
Summary:	The core programs for the GNOME2 GUI desktop environment
Summary(pl):	Podstawowe programy ¶rodowiska graficznego GNOME2
Name:		gnome-desktop
Version:	2.7.1
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	c164eb625325399e175e787cef94008e
Source1:	http://www.pld-linux.org/Members/krzak/pld-logo.svg
# Source1-md5:	9fda4ca70a6e8e82e8e5bebe0e28db74
Patch0:		%{name}-crystalsvg.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-omf.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gnome-vfs2-devel >= 2.7.1
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libgnomeui-devel >= 2.7.1
BuildRequires:	libgnomecanvas-devel >= 2.7.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.6
BuildRequires:	scrollkeeper
Requires(post):	/sbin/ldconfig
Requires(post):	scrollkeeper
Requires:	libgnomeui >= 2.7.1
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
przyjaznych dla u¿ytkownika programów i narzêdzi biurkowych, których
u¿ywa siê wraz z zarz±dc± okien systemu X Window. GNOME2 przypomina
wygl±dem i zakresem funkcjonalno¶ci CDE i KDE, jednak GNOME2 opiera
siê w ca³o¶ci na wolnym oprogramowaniu.

Ten pakiet zawiera aplikacje zwi±zane w desktopem GNOME2.

%package devel
Summary:	GNOME2 desktop includes
Summary(pl):	Pliki nag³ówkowe bibliotek GNOME2 desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgnomeui-devel >= 2.7.1
Requires:	startup-notification-devel >= 0.6

%description devel
GNOME2 desktop header files.

%description devel -l pl
Pliki nag³ówkowe bibliotek GNOME2 desktop.

%package static
Summary:	GNOME2 desktop static libraries
Summary(pl):	Statyczne biblioteki GNOME2 desktop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
GNOME2 desktop static libraries.

%description static -l pl
Statyczne biblioteki GNOME2 desktop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po

%build
gnome-doc-common --copy
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
	
rm -rf $RPM_BUILD_ROOT/%{_pixmapsdir}/gnome-logo-icon-transparent.png
install %{SOURCE1} $RPM_BUILD_ROOT/%{_pixmapsdir}/gnome-logo-icon-transparent.svg

%find_lang %{name} --with-gnome --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

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
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-desktop-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
