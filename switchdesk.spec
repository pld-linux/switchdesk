Name:		switchdesk
Summary:	Desktop Switcher - switch between GNOME, KDE and AnotherLevel.
Version:	1.7.0
Release:	1
Source0:	%{name}-%{version}.tar.gz
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	textutils

%define		kdeprefix	/usr

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The Desktop Switcher is a tool which enables users to easily switch
between various desktop environments that they have installed. The
tool includes support for GNOME, KDE, and AnotherLevel. Support for
different environments on different computers is available, as well as
setting a "global default."

%package kde
Group:		X11/KDE
Group(de):	X11/KDE
Group(pl):	X11/KDE
Summary:	KDE interface to the Desktop Switcher.
Requires:	qt >= 1.42 kdesupport

%description kde
Provides the desktop switching Tool with a KDE look and feel.

%package gnome
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Summary:	GNOME interface to the Desktop Switcher.

%description gnome
Provides the desktop switching tool with a GNOME look and feel.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

%build
KDEDIR=%{kdeprefix} ; export KDEDIR
%{__make} -f Makefile.cvs
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
%{__make} CXXFLAGS="%{rpmcflags}" KDEDIR=%{kdeprefix}

%install
rm -rf $RPM_BUILD_ROOT
KDEDIR=%{kdeprefix} ; export KDEDIR
%{__make} install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/switchdesk
%attr(755,root,root) %{_bindir}/switchdesk-helper
%{_applnkdir}/System/switchdesk.desktop
%{_applnkdir}/System/switchdesk.kdelnk
%{_datadir}/apps/switchdesk

%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/switchdesk-kde

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/switchdesk-gnome
