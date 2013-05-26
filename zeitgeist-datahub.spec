Summary:	The datahub provides passive plugins which insert events into Zeitgeist
Summary(pl.UTF-8):	Datahub udostępnia pasywne wtyczki umieszczające zdarzenia w Zeitgeiście
Name:		zeitgeist-datahub
Version:	0.9.5
Release:	1
License:	LGPL v3+
Group:		Applications
Source0:	http://launchpad.net/zeitgeist-datahub/0.9/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	b2b76b82b67363c45e5fe4f39a172775
URL:		https://launchpad.net/zeitgeist-datahub
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	json-glib-devel >= 0.14.0
BuildRequires:	libzeitgeist-devel >= 0.3.18
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel >= 0.18.0
BuildRequires:	vala >= 2:0.16.0
Requires:	glib2 >= 1:2.26.0
Requires:	gtk+2 >= 2:2.16.0
Requires:	json-glib >= 0.14.0
Requires:	libzeitgeist >= 0.3.18
Requires:	telepathy-glib >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The datahub provides passive plugins which insert events into
Zeitgeist.

%description -l pl.UTF-8
Datahub udostępnia pasywne wtyczki umieszczające zdarzenia w
Zeitgeiście.

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
%doc AUTHORS NEWS
%{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%attr(755,root,root) %{_bindir}/zeitgeist-datahub
%{_mandir}/man1/zeitgeist-datahub.1*
