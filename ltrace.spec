Summary:	Tracks runtime library calls from dynamically linked executables.
Summary(pl):	�ledzenie odwo�a� do bibliotek w plikach linkowanych dynamicznie.
Name:		ltrace
Version:	0.3.8
Release:	1
Source:		ftp://ftp.debian.org/debian/dists/unstable/main/source/utils/%{name}_%{version}.tar.gz
Copyright:	GPL
Group:		Development/Debuggers
ExclusiveArch:	i386 i486 i586 i686
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Ltrace is a debugging program which runs a specified command until the
command exits.  While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process and
the signals received by the executed process.  Ltrace can also intercept
and print system calls executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%description -l pl
Ltrace jest programem wspomagaj�cym debugowanie program�w. Ltrace uruchamia
dane polecenie przechwytuj�c i zapisuj�c odwo�ania do bibliotek linkowanych
dynamicznie oraz sygna�y otrzymane przez program. Ltrace potrafi tak�e
przechwytywa� i wy�wietla� odwo�ania systemowe wykonywane przez program.

Je�li potrzebujesz narz�dzia administracyjnego, przydatnego do �ledzenia
dzia�ania program�w, powiniene� zainstalowa� ltrace.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README TODO BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config /etc/ltrace.conf
%attr(755,root,root) %{_bindir}/ltrace
%{_mandir}/man1/*
