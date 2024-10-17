Name:		texlive-tlcockpit
Version:	54857
Release:	2
Summary:	A GUI frontend to TeX Live Manager (tlmgr)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tlcockpit
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlcockpit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlcockpit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlcockpit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims at being a GUI for tlmgr, the TeX Live
Manager, with a modern look and feel. We take inspiration from
the excellent TeX Live Utility for MacOS.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/source/support/tlcockpit
%{_texmfdistdir}/scripts/tlcockpit
%doc %{_texmfdistdir}/doc/support/tlcockpit
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
