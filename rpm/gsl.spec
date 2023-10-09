Summary: The GNU Scientific Library for numerical analysis
Name: gsl
Version: 2.7.1
Release: 1
License: GPLv3+
URL: http://www.gnu.org/software/gsl/
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package devel
Summary: Libraries and the header files for GSL development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The gsl-devel package contains the header files necessary for 
developing programs using the GSL (GNU Scientific Library).

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
# disable FMA
%ifarch aarch64 x86_64
export CFLAGS="%{optflags} -ffp-contract=off"
%endif
./autogen.sh
%configure
%make_build

%install
%make_install

# remove unpackaged files from the buildroot
rm -rf %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_infodir}/gsl*
rm -rf %{buildroot}%{_mandir}/man*
rm -f %{buildroot}%{_libdir}/*.la
# remove static libraries
rm -rf %{buildroot}%{_libdir}/*.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_libdir}/libgsl.so.27*
%{_libdir}/libgslcblas.so.0*

%files devel
%{_bindir}/gsl-config
%{_libdir}/libgsl.so
%{_libdir}/libgslcblas.so
%{_libdir}/pkgconfig/gsl.pc
%{_datadir}/aclocal/gsl.m4
%{_includedir}/gsl/
