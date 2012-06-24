Summary:	Desktop Switcher - switch between GNOME, KDE and AnotherLevel
Summary(pl):	Prze��cznik desktop�w - prze��cza pomi�dzy GNOME, KDE i AnotherLevel
Name:		switchdesk
Version:	1.7.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	textutils


%define		kdeprefix	%{_prefix}

%description
The Desktop Switcher is a tool which enables users to easily switch
between various desktop environments that they have installed. The
tool includes support for GNOME, KDE, and AnotherLevel. Support for
different environments on different computers is available, as well as
setting a "global default."

%description -l pl
Desktop Switcher to narz�dzie pozwalaj�ce u�ytkownikom �atwo
prze��cza� si� mi�dzy r�nymi �rodowiskami desktopowymi, kt�re s�
zainstalowane. Narz�dzie ma wsparcie dl GNOME, KDE i AnotherLevel.
Wsprarcie dla innych �rodowisk jest mo�liwe, podobnie jak ustawienie
globalnego domy�lnego �rodowiska.

%package kde
Summary:	KDE interface to the Desktop Switcher
Summary(pl):	Interfejs KDE do Desktop Switchera
Group:		X11/Applications
Requires:	qt >= 1.42 kdesupport

%description kde
Provides the desktop switching Tool with a KDE look and feel.

%description kde -l pl
Pakiet zawiera narz�dzie do prze��czania desktop�w z wygl�dem KDE.

%package gnome
Summary:	GNOME interface to the Desktop Switcher
Summary(pl):	Interfejs GNOME do Desktop Switchera
Group:		X11/Applications

%description gnome
Provides the desktop switching tool with a GNOME look and feel.

%description gnome -l pl
Pakiet zawiera narz�dzie do prze��czania desktop�w z wygl�dem GNOME.

%prep
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
