Summary:	The core programs for the GNOME2 GUI desktop environment.
Name:		gnome-desktop
Version:	1.5.17
Release:	0.1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	%{name}-libs

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man
%define         _sysconfdir     /etc/X11/GNOME2

%description
GNOME2 (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. GNOME2 is similar in purpose and scope
to CDE and KDE, but GNOME2 is based completely on free software. The
gnome-core package includes the basic programs and libraries that are
needed to install GNOME2.

The GNOME2 panel packages provides the gnome panel, menu's and some
basic applets for the panel.

%package devel
Summary:	GNOME2 panel includes
Group:          X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Panel header files for creating GNOME panels.

%package static
Summary:	GNOME2 panel static libraries
Group:          X11/Development/Libraries
Requires:	%{name} = %{version}

%description static
Panel static libraries for creating GNOME2 panels.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS COPYING ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%doc %{_mandir}/man1/*
%{_datadir}/gnome/vfolders
%{_datadir}/gnome-about/gnome-version
%{_datadir}/pixmaps/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-desktop-2.0
%attr(755,root,root) %{_libdir}/lib*.??
%{_pkgconfigdir}/*.cp

%files static
%defattr(644,root,root,755)
%{_libdir}/*a
