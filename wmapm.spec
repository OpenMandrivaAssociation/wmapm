Summary:  Battery/Power status monitor for WindowMaker on laptops
Name:		wmapm
Version:	3.1
Release:	%mkrel 12
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Source10:		wmapm-16x16.png
Source11:		wmapm-32x32.png
Source12:		wmapm-48x48.png
URL:		http://nis-www.lanl.gov/~mgh/
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
WMAPM monitors the APM statistics through the APM support in
the Linux and FreeBSD Kernels.  This information, presented in
a nice visual format, can be invaluable on laptops (as I have
found in my recent/continual travels as a Field Engineer for a
small computer hardware manufacturer).
WMAPM currently provides:

        * Status of power supply (battery or AC);
        * Percentage of battery remaining (numeric and meter);
        * Battery charging status;
        * Time left to battery depletion;
        * High/Low/Critical battery status (Red/Yellow/Green);

%prep
rm -rf %buildroot
%setup -q

%build
make -C %name COPTS="$RPM_OPT_FLAGS"

%install
[ -d %buildroot ] && rm -rf %buildroot

mkdir -p %buildroot{%_bindir,%_miconsdir,%_liconsdir,%_mandir/man1/}
install -m 755 wmapm/wmapm %buildroot%_bindir
install -m 644 wmapm/wmapm.1 %buildroot%_mandir/man1/

install -m 644 %SOURCE10 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE11 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE12 %buildroot%_liconsdir/%name.png


install -m 755 -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=WmApm
Comment=Battery/Power status monitor for WindowMaker on laptops
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF


%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}

%files
%defattr (-,root,root)
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO
%_bindir/*
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop
%_mandir/man1/*


