%global tl_name syllogism
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Typeset syllogisms in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/syllogism
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syllogism.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syllogism.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple, configurable, way for neatly typesetting
syllogisms and syllogistic-like arguments, composed of two premises and
a conclusion.

