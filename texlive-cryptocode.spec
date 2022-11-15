Name:		texlive-cryptocode
Version:	60249
Release:	1
Summary:	Typesetting pseudocode, protocols, game-based proofs and black-box reductions in cryptography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cryptocode
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryptocode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryptocode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryptocode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cryptocode package provides a set of macros to ease the
typesetting of pseudocode, algorithms and protocols. In
addition it comes with a wide range of tools to typeset
cryptographic papers. This includes simple predefined commands
for concepts such as a security parameter or advantage terms
but also flexible and powerful environments to layout
game-based proofs or black-box reductions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cryptocode
%{_texmfdistdir}/tex/latex/cryptocode
%doc %{_texmfdistdir}/doc/latex/cryptocode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
