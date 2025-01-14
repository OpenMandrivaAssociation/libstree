%define rname stree

%define major 0
%define libname %mklibname %{rname} %{major}
%define develname %mklibname %{rname} -d
%define staticdevelname %mklibname %{rname} -s -d

Summary: 	A generic library for string algorithms based on suffix trees
Name: 		libstree
Version: 	0.4.2
Release: 	9
License: 	BSD
Group: 		Development/Other
URL: 		https://www.cl.cam.ac.uk/~cpk25/libstree/index.html
Source0: 	http://www.cl.cam.ac.uk/~cpk25/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	libtool

%description
LibSTree is a library containing generic versions of string
algorithms based on suffix trees. The underlying implementation is
based on Ukkonen's linear suffix tree creation algorithm,
supporting multiple strings per tree.

%package -n	%{libname}
Summary:	Header files and development documentation for libnet
Group:		System/Libraries
Provides:	libstree

%description -n %{libname}
LibSTree is a library containing generic versions of string
algorithms based on suffix trees. The underlying implementation is
based on Ukkonen's linear suffix tree creation algorithm,
supporting multiple strings per tree.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libstree-devel = %{EVRD}
Obsoletes:	%{mklibname %{rname} 0 -d}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{staticdevelname}
Summary:	Static %{libname} library
Group:		Development/C
Requires:	%{develname} = %{version}
Provides:	libstree-static-devel = %{EVRD}
Obsoletes:	%{mklibname %{rname} 0 -s -d}

%description -n	%{staticdevelname}
Static %{libname} library.

%prep

%setup -q

%build

%serverbuild

%configure2_5x

%make

%install
%makeinstall_std

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(0755,root,root) %{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(0644,root,root,755)
%attr(0755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/stree
%doc %{_datadir}/gtk-doc/html/%{name}

%files -n %{staticdevelname}
%defattr(0644,root,root,755)
%{_libdir}/lib*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-8mdv2011.0
+ Revision: 620230
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-7mdv2010.0
+ Revision: 429835
- rebuild

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-6mdv2009.0
+ Revision: 233753
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 19 2007 Funda Wang <fwang@mandriva.org> 0.4.2-5mdv2008.1
+ Revision: 100402
- fix devel requires

* Mon Oct 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-4mdv2008.0
+ Revision: 94144
- rebuilt due to missing packages

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.2-3mdv2008.0
+ Revision: 89850
- rebuild

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-2mdv2008.0
+ Revision: 83748
- new devel naming


* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-1mdv2007.0
+ Revision: 94101
- Import libstree

* Tue May 30 2006 Emmanuel Andry <eandry@mandriva.org> 0.4.2-1mdk
- 0.4.2
- mkrel

* Mon Jan 16 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-1mdk
- 0.4.1

* Tue Jul 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdk
- rebuild

* Wed Jun 30 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.4.0-1mdk
- 0.4.0

