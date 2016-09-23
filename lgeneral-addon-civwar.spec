Summary:	LGeneral game - Civwar mod
Summary(pl.UTF-8):	Gra Linux General - modyfikacja Civwar
Name:		lgeneral-addon-civwar
Version:	1.0
Release:	1
License:	unknown
Group:		Applications/Games
Source0:	http://lgames.sourceforge.net/LGeneral/addons/civwar.zip
# Source0-md5:	721e8aa9a466e9c5ff33f0c371e2e280
URL:		http://lgames.sourceforge.net/LGeneral/addons.php
Requires:	lgeneral
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Civwar (American Civil War) mod
including military style maps and icons.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera modyfikacje Civwar (American Civil War),
zawierającą mapy oraz ikony w stylu militarnym.

%prep
%setup -q -n civwar

# junk
%{__rm} maps/*.tdb~ nations/*.ndb~ units/*.udb~

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -a * $RPM_BUILD_ROOT%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/lgeneral/gfx/flags/civwar.bmp
%{_datadir}/lgeneral/gfx/terrain/civwar
%{_datadir}/lgeneral/gfx/units/civwar*.bmp
%{_datadir}/lgeneral/maps/civwar.tdb
%{_datadir}/lgeneral/nations/civwar.ndb
%{_datadir}/lgeneral/sounds/civwar
%{_datadir}/lgeneral/units/civwar.udb
