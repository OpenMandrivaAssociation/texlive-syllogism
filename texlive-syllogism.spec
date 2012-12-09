# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/syllogism
# catalog-date 2008-10-28 11:39:06 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-syllogism
Version:	1.2
Release:	2
Summary:	Typeset syllogisms in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/syllogism
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syllogism.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syllogism.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 756374
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719623
- texlive-syllogism
- texlive-syllogism
- texlive-syllogism
- texlive-syllogism

