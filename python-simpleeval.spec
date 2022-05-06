%global _empty_manifest_terminate_build 0
Name:		python-simpleeval
Version:	0.9.10
Release:	2
Summary:	A simple, safe single expression evaluator library.
License:	MIT License
URL:		https://github.com/danthedeckie/simpleeval
Source0:	https://files.pythonhosted.org/packages/62/25/aec98426834844b70b7ab24b4cce8655d31e654f58e1fa9861533f5f2af1/simpleeval-0.9.10.tar.gz
Patch0:		remove_2to3.patch
BuildArch:	noarch


%description
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

%package -n python3-simpleeval
Summary:	A simple, safe single expression evaluator library.
Provides:	python-simpleeval
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-simpleeval
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

%package help
Summary:	Development documents and examples for simpleeval
Provides:	python3-simpleeval-doc
%description help
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

%prep
%autosetup -n simpleeval-0.9.10 -p1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-simpleeval -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri May 06 2022 YukariChiba <i@0x7f.cc> - 0.9.10-2
- Remove deprecated use_2to3 attribute

* Mon Sep 06 2021 Python_Bot <Python_Bot@openeuler.org> - 0.9.10-1
- Package Init
