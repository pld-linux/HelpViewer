Summary:	Online help viewer for GNUstep
Summary(pl):	Przegl±darka pomocy online dla GNUstepa
Name:		HelpViewer
Version:	0.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.roard.com/helpviewer/download/%{name}-%{version}.tgz
# Source0-md5:	9e3c1c07cdbe0187ce6e0152d3e8870d
URL:		http://www.roard.com/helpviewer/
BuildRequires:	gnustep-gui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%define		gstriple	%{gscpu}/%{gsos}/%{libcombo}

%description
HelpViewer is an online help viewer for GNUstep programs.

%description -l pl
HelpViewer to przegl±darka pomocy online dla programów z GNUstepa.

%prep
%setup -q

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	debug=no \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install debug=no \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%dir %{_prefix}/System/Applications/HelpViewer.app
%attr(755,root,root) %{_prefix}/System/Applications/HelpViewer.app/HelpViewer
%dir %{_prefix}/System/Applications/HelpViewer.app/Resources
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.desktop
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.plist
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.tiff

%dir %{_prefix}/System/Applications/HelpViewer.app
%dir %{_prefix}/System/Applications/HelpViewer.app/%{gscpu}
%dir %{_prefix}/System/Applications/HelpViewer.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/HelpViewer.app/%{gstriple}
%attr(755,root,root) %{_prefix}/System/Applications/HelpViewer.app/%{gstriple}/HelpViewer
%{_prefix}/System/Applications/HelpViewer.app/%{gstriple}/*.openapp
%{_prefix}/System/Applications/HelpViewer.app/HelpViewer
%dir %{_prefix}/System/Applications/HelpViewer.app/Resources
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.plist
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.desktop
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/HelpViewer.app/%{gscpu}
%dir %{_prefix}/System/Applications/HelpViewer.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/HelpViewer.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/HelpViewer.app/%{gstriple}/HelpViewer
%{_prefix}/System/Applications/HelpViewer.app/%{gstriple}/*.openapp

%{_prefix}/System/Applications/HelpViewer.app/Resources/*.help
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.gorm
%{_prefix}/System/Applications/HelpViewer.app/Resources/*.png
