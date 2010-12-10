%define rname stree

%define major 0
%define libname %mklibname %{rname} %{major}
%define develname %mklibname %{rname} -d
%define staticdevelname %mklibname %{rname} -s -d

Summary: 	A generic library for string algorithms based on suffix trees
Name: 		libstree
Version: 	0.4.2
Release: 	%mkrel 8
License: 	BSD
Group: 		Development/Other
URL: 		http://www.cl.cam.ac.uk/~cpk25/libstree/index.html
Source0: 	http://www.cl.cam.ac.uk/~cpk25/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	libtool
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	libstree-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{rname} 0 -d}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{staticdevelname}
Summary:	Static %{libname} library
Group:		Development/C
Requires:	%{develname} = %{version}
Provides:	libstree-static-devel = %{version}-%{release}
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
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(0755,root,root) %{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(0644,root,root,755)
%attr(0755,root,root) %{_libdir}/lib*.so
%attr(0755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_includedir}/stree
%doc %{_datadir}/gtk-doc/html/%{name}

%files -n %{staticdevelname}
%defattr(0644,root,root,755)
%{_libdir}/lib*.a
