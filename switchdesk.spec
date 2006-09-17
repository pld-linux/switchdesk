Summary:	Desktop Switcher - switch between GNOME, KDE and AnotherLevel
Summary(pl):	Prze³±cznik desktopów - prze³±cza pomiêdzy GNOME, KDE i AnotherLevel
Name:		switchdesk
Version:	4.0.8
Release:	0.1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	%{name}-%{version}-6.tar.bz2
# Source0-md5:	020d27b29a5f02875852d99ea83e38f6
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-pyc.patch
Patch2:		%{name}-PLD.patch
BuildRequires:	intltool
BuildRequires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_switchdeskdir	%{_datadir}/switchdesk

%description
The Desktop Switcher is a tool which enables users to easily switch
between various desktop environments that they have installed. The
tool includes support for GNOME, KDE, Xfce4 and others. Support for
different environments on different computers is available, as well as
setting a "global default."

%description -l pl
Desktop Switcher to narzêdzie pozwalaj±ce u¿ytkownikom ³atwo
prze³±czaæ siê miêdzy ró¿nymi ¶rodowiskami desktopowymi, które s±
zainstalowane. Narzêdzie ma wsparcie dla GNOME, KDE, Xfce4 i innych.
Wsprarcie dla innych ¶rodowisk jest mo¿liwe, podobnie jak ustawienie
globalnego domy¶lnego ¶rodowiska.

%package gui
Summary:	Graphical interface to the Desktop Switcher
Summary(pl):	Graficzny interfejs do Desktop Switchera
Group:		X11/Applications
Requires:	switchdesk >= %{version}-%{release}
Provides:	switchdesk-gnome
Provides:	switchdesk-kde
Obsoletes:	switchdesk-gnome
Obsoletes:	switchdesk-kde

%description gui
Provides the graphical user interface to the Desktop Switcher.

%description gui -l pl
Pakiet zawiera graficzny interfejs do Desktop Switchera.

%prep
%setup -q -n %{name}-%{version}-6
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_switchdeskdir}/*.py
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/switchdesk
%attr(755,root,root) %{_bindir}/switchdesk-helper
%dir %{_switchdeskdir}
%{_switchdeskdir}/Xclients.*
%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1/*

%files gui
%defattr(644,root,root,755)
%{_switchdeskdir}/pixmaps
%{_switchdeskdir}/*.pyc
%{_switchdeskdir}/*.glade
%{_desktopdir}/*.desktop
