Summary:	Simple SMTP client
Summary(pl):	Prosty klient SMTP
Name:		smtpclient
Version:	1.0.0
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://freshmeat.net/redir/smtpclient/9732/url_tgz/%{name}-%{version}.tar.gz
# Source0-md5:	8b5d9260572107bb901edf6aacbf3747
Patch0:		%{name}-ac.patch
Patch1:		%{name}-raw.patch
URL:		http://www.engelschall.com/sw/smtpclient/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smtpclient is a minimal SMTP client that takes an email message body and
passes it on to a SMTP server. Since it is completely self-supporting, it
is especially suitable for use in restricted environments.

%description -l pl
smtpclient jest minimalnym klientem SMTP który bierze tre¶æ wiadomo¶ci i
przesy³a j± do serwera SMTP. Poniewa¿ jest ca³kowicie samowystarczalny,
nadaje siê zw³aszcza do ¶rodowisk z du¿± ilo¶ci± na³o¿onych ograniczeñ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install smtpclient $RPM_BUILD_ROOT%{_bindir}
install smtpclient.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README PORTING VERSIONS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
