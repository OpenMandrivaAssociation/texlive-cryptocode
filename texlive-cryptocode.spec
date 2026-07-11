%global tl_name cryptocode
%global tl_revision 60249

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.44
Release:	%{tl_revision}.1
Summary:	Typesetting pseudocode, protocols, game-based proofs and black-box reductions...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cryptocode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cryptocode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cryptocode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cryptocode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The cryptocode package provides a set of macros to ease the typesetting
of pseudocode, algorithms and protocols. In addition it comes with a
wide range of tools to typeset cryptographic papers. This includes
simple predefined commands for concepts such as a security parameter or
advantage terms but also flexible and powerful environments to layout
game-based proofs or black-box reductions.

