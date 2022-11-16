Name:		texlive-tlcockpit
Version:	54857
Release:	1
Summary:	A GUI frontend to TeX Live Manager (tlmgr)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tlcockpit
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
%doc %{_texmfdistdir}/texmf-dist/source/support/tlcockpit
%{_texmfdistdir}/texmf-dist/scripts/tlcockpit
%doc %{_texmfdistdir}/texmf-dist/doc/support/tlcockpit
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tlcockpit.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tlcockpit.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
