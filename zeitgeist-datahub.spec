Summary:	The datahub provides passive plugins which insert events into Zeitgeist
Name:		zeitgeist-datahub
Version:	0.7.0
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://launchpad.net/zeitgeist-datahub/0.7/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	ebf822fc4aafbfe93784db60e1f9917a
URL:		https://launchpad.net/zeitgeist-datahub
BuildRequires:	autoconf
BuildRequires:	automake >= 1.11
BuildRequires:	intltool >= 0.35.0
BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	vala >= 0.11.2
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+2-devel >= 2.16.0
BuildRequires:	libzeitgeist-devel >= 0.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The datahub provides passive plugins which insert events into
Zeitgeist.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%attr(755,root,root) %{_bindir}/zeitgeist-datahub
%{_mandir}/man1/zeitgeist-datahub.1*
