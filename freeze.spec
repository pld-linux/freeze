Summary:	freeze/melt/fcat compression utilities
Summary(pl.UTF-8):	Narzędzia do kompresji freeze/melt/fcat
Name:		freeze
Version:	2.5.0
Release:	1
License:	distributable
Group:		Applications/Archiving
Source0:	http://www.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
# Source0-md5:	3ca4b267c0d49451ff58cf403671b98a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freeze is an old file compressor and decompressor that is not in
common use anymore, but can be useful if the need ever arises to
dearchive files compressed with it.

Freeze uses the Lempel-Ziv algorithm on the first pass and the dynamic
Huffman algorithm on the second one.

%description -l pl.UTF-8
Freeze to stary kompresor i dekompresor plików, nie będący już w
powszechnym użyciu, ale przydatny w przypadku konieczności
rozpakowania plików nim skompresowanych.

Freeze używa algorytmu Lempel-Ziv w pierwszym przebiegu i dynamicznego
algorytmu Huffmana w drugim.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install freeze statist $RPM_BUILD_ROOT%{_bindir}
ln -sf freeze $RPM_BUILD_ROOT%{_bindir}/fcat
ln -sf freeze $RPM_BUILD_ROOT%{_bindir}/melt
ln -sf freeze $RPM_BUILD_ROOT%{_bindir}/unfreeze
install freeze.1 statist.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo '.so freeze.1' > $RPM_BUILD_ROOT%{_mandir}/man1/fcat.1
echo '.so freeze.1' > $RPM_BUILD_ROOT%{_mandir}/man1/melt.1
echo '.so freeze.1' > $RPM_BUILD_ROOT%{_mandir}/man1/unfreeze.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
