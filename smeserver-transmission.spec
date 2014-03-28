%define name smeserver-transmission
%define version 0.0.1
%define release 10
Summary: transmission is a helpdesk system to download the SME Server iso
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Distribution: SME Server
License: GNU GPL version 2
Group: SMEserver/addon
Source: smeserver-transmission-%{version}.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/%{name}-%{version}-buildroot
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8.0
Requires: transmission >= 2.70
AutoReqProv: no
Patch0: smeserver-transmission-0.0.1_set_admin_user_and_64_version.patch
%description
transmission is an application adapted as a contrib for SMEserver, to help the  seeding of the SME Server CDROM ISO. 

%changelog
* Sun Nov 17 2013  Stéphane de Labrusse  <stephdl@de-labrusse.fr> 0.0.1-9
- add folder /var/lib/transmission/Downloads to avoid log errors
- add a db command to choose the location of transmission download folder
* Sat Nov 16 2013  Stéphane de Labrusse  <stephdl@de-labrusse.fr> 0.0.1-6
- final release
* Fri Nov 15 2013  Stéphane de Labrusse <stephdl@de-labrusse.fr> 0.0.1-3
- Modified smeserver templates (settings.json,61transmission-reverse-proxy)
- Add a web folder to download torrent https://sme-ip/transmission-dl
* Tue Nov 12 2013  Stéphane de Labrusse <stephdl@de-labrusse.fr> 0.0.12
- The work continue
* Sat Nov 09 2013  CONTRIB MAKER <tests@pialasse.com> 0.0.1-1.sme
- initial release
- builds from unchanged .tar.gz 

%prep
%setup
%patch0 -p1
%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
     > %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre

%post



