Summary:	Tracks runtime library calls from dynamically linked executables
Summary(es):	Ense�a informaci�n sobre las llamadas a funciones de bibliotecas en binarios din�micamente conectados
Summary(pl):	�ledzenie odwo�a� do bibliotek w plikach konsolidowanych dynamicznie
Summary(pt_BR):	Mostra informa��es sobre as chamadas � fun��es de bibliotecas em bin�rios dinamicamente ligados
Summary(ru):	������� ������ ������������ � ��������� ������� ���������
Summary(uk):	����� ����� ¦�̦������� �� ��������� �����˦� ��������
Name:		ltrace
Version:	0.3.31
Release:	5
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.debian.org/debian/pool/main/l/%{name}/%{name}_%{version}.tar.gz
# Source0-md5:	7bef142861646ad33dc749fbaf96761e
Patch0:		%{name}-Makefile.in.patch
Patch1:		%{name}-sparc.patch
URL:		http://packages.debian.org/unstable/utils/ltrace.html
BuildRequires:	autoconf
BuildRequires:	automake
ExclusiveArch:	%{ix86} m68k armv4b armv4l ppc s390 sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ltrace is a debugging program which runs a specified command until the
command exits. While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process
and the signals received by the executed process. Ltrace can also
intercept and print system calls executed by the process. You should
install ltrace if you need a sysadmin tool for tracking the execution
of processes.

%description -l es
ltrace es un programa que sencillamente ejecuta un comando
especificado hasta su t�rmino. Intercepta y registra las llamadas, a
las funciones de las bibliotecas compartidas, hechas por el programa
en ejecuci�n, y los se�ales recibidos por el proceso. Tambi�n puede
interceptar y ense�ar las llamadas al sistema operativo hechas por el
programa.

%description -l pl
Ltrace jest programem wspomagaj�cym debugowanie program�w. Ltrace
uruchamia dane polecenie przechwytuj�c i zapisuj�c odwo�ania do
bibliotek konsolidowanych dynamicznie oraz sygna�y otrzymane przez
program. Ltrace potrafi tak�e przechwytywa� i wy�wietla� odwo�ania
systemowe wykonywane przez program. Je�li potrzebujesz narz�dzia
administracyjnego, przydatnego do �ledzenia dzia�ania program�w,
powiniene� zainstalowa� ltrace.

%description -l pt_BR
ltrace � um programa que simplesmente executa um comando especificado
at� seu t�rmino. Ele intercepta e registra as chamadas � fun��es a
bibliotecas compartilhadas feitas pelo programa em execu��o e os
sinais recebidos pelo processo. Tamb�m pode interceptar e mostrar as
chamadas ao sistema operacional feitas pelo programa.

%description -l ru
Ltrace - ��� ���������� ���������, ������� ��������� ���������
���������, ������������� � ���������� ��� ������ ������������
���������, ��� � �������, ���������� ������������� ���������. Ltrace
����� ����� ������������� � �������� ��������� ������, �����������
���������.

%description -l uk
Ltrace - �� ��������, ��� �������� ������� �������� �� ��������դ �
�����դ �� ������� ����ͦ���� ¦�̦����, ��� � �������, �˦ �����դ
��������� ������. Ltrace ���� ����� ������������� � ��������� ������Φ
������� ����� �������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO BUGS
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ltrace.conf
%attr(755,root,root) %{_bindir}/ltrace
%{_mandir}/man1/*
