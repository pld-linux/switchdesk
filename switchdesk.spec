%define kdeprefix /usr
%define qtver  qt >= 1.42
%define kdename switchdesk
Name: %{kdename}
Summary: Desktop Switcher - switch between GNOME, KDE and AnotherLevel.
Version: 1.7.0
Release: 1
Source: %{kdename}-%{version}.tar.gz
Copyright: GPL
Group: X11/Window Managers/Tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires: textutils
Prefix: %{kdeprefix}

%description
The Desktop Switcher is a tool which enables users to easily switch between
various desktop environments that they have installed.  The tool includes
support for GNOME, KDE, and AnotherLevel.  Support for different environments
on different computers is available, as well as setting a "global default."

%package kde
Group: X11/KDE
Summary: KDE interface to the Desktop Switcher.
Requires: %{qtver} kdesupport

%description kde
Provides the desktop switching Tool with a KDE look and feel.

%package gnome
Group: X11/GNOME
Summary: GNOME interface to the Desktop Switcher.

%description gnome
Provides the desktop switching tool with a GNOME look and feel.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{kdename}-%{version}

%build
export KDEDIR=%{kdeprefix}
%{__make} -f Makefile.cvs
./configure \
	--prefix=%{kdeprefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--disable-path-check
%{__make} CXXFLAGS="$RPM_OPT_FLAGS" KDEDIR=%{kdeprefix}

%install
export KDEDIR=%{kdeprefix}
%{__make} install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
/usr/bin/switchdesk
/usr/bin/switchdesk-helper
#/usr/X11R6/share/applnk/System/switchdesk.desktop
/usr/share/applnk/System/switchdesk.kdelnk
/usr/share/apps/switchdesk

%files kde
/usr/bin/switchdesk-kde

%files gnome
/usr/bin/switchdesk-gnome
