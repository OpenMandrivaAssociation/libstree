%define rname	stree

%define	major	0
%define libname	%mklibname %{rname} %{major}
%define	libname_devel	%mklibname %{rname} %{major} -d
%define	libname_static_devel	%mklibname %{rname} %{major} -s -d

Summary: 	A generic library for string algorithms based on suffix trees
Name: 		libstree
Version: 	0.4.2
Release: 	%mkrel 1
License: 	BSD
Group: 		Development/Other
URL: 		http://www.cl.cam.ac.uk/~cpk25/libstree/index.html
Source0: 	http://www.cl.cam.ac.uk/~cpk25/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
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

%package -n	%{libname_devel}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libstree-devel

%description -n	%{libname_devel}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{libname_static_devel}
Summary:	Static %{libname} library
Group:		Development/C
Requires:	%{libname}-devel = %{version}

%description -n	%{libname_static_devel}
Static %{libname} library.

%prep
%setup -q

%build

%serverbuild

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(0755,root,root) %{_libdir}/lib*.so.*

%files -n %{libname_devel}
%defattr(0644,root,root,755)
%attr(0755,root,root) %{_libdir}/lib*.so
%attr(0755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_includedir}/stree
%doc %{_datadir}/gtk-doc/html/%{name}

%files -n %{libname_static_devel}
%defattr(0644,root,root,755)
%{_libdir}/lib*.a


