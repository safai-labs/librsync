Summary:  	Rsync libraries
Name:     	librsync
Version:  	0.9.4pre
Release:  	1
Copyright:	LGPL
Group:    	System Environment/Libraries
Source:  	http://ftp1.sourceforge.net/rproxy/librsync-0.9.4pre.tar.gz
URL:       	http://www.sf.net/projects/rproxy
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient than
and incompatible with rsync 2.4.6.

%package devel
Summary: Headers and development libraries for librsync
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient than
and incompatible with rsync 2.4.6.

This package contains header files necessary for developing programs
based on librsync.

%prep 
%setup
# The next line is only needed if there are any non-upstream patches.  In
# this distribution there are none.
#%patch 

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make  DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING NEWS README
%{_libdir}/librsync.la
%{_bindir}/rdiff
%{_mandir}/man3/librsync.3.gz
%{_mandir}/man1/rdiff.1.gz

%files devel
%defattr(-,root,root)
%{_prefix}/include/*
%{_libdir}/librsync.a

%changelog