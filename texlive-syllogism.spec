Name:		texlive-syllogism
Version:	15878
Release:	2
Summary:	Typeset syllogisms in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/syllogism
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syllogism.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syllogism.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple, configurable, way for neatly
typesetting syllogisms and syllogistic-like arguments, composed
of two premises and a conclusion.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/syllogism/syllogism.sty
%doc %{_texmfdistdir}/doc/latex/syllogism/Examples.pdf
%doc %{_texmfdistdir}/doc/latex/syllogism/Examples.tex
%doc %{_texmfdistdir}/doc/latex/syllogism/README
%doc %{_texmfdistdir}/doc/latex/syllogism/syllogism.pdf
%doc %{_texmfdistdir}/doc/latex/syllogism/syllogism.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
