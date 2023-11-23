%define debug_package %{nil}

Name:           demokritos-scripts
Version:        1.4
Release:        0
Group:          Productivity/Scientific/Physics
License:        GPL-3.0
Summary:        Scripts made at Demokritos lab
Url:            https://github.com/psaxioti/demokritos-scripts

BuildArch:      noarch

Requires:       demokritos-programs

%description
This package has useful scripts made and used at the demokritos Lab, for converting data between formats, or run Talys and geant4

%prep
%setup -q -n %{_sourcedir}/%{name}-%{version} -T -D

%build

%install
install -Dm755 Scripts/evnt2dat   %{buildroot}%{_bindir}/evnt2dat
install -Dm755 Scripts/geant_make   %{buildroot}%{_bindir}/geant_make
install -Dm755 Scripts/mpa2ascii   %{buildroot}%{_bindir}/mpa2ascii
install -Dm755 Scripts/Talys_script   %{buildroot}%{_bindir}/Talys_script
install -Dm755 Scripts/Talys_script   %{buildroot}%{_bindir}/Talys_script_mt

%files
%{_bindir}/*
