%global debug_package %{nil}

%global commit 4694ba7ee51652d29ef41e7fde846b83a2a1c53b
%global commitdate 20221112
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ipu6-camera-bins
Summary:        Binaries for Intel IPU6
Version:        0.0
Release:        1.%{commitdate}git%{shortcommit}%{?dist}
License:        Proprietory

Source0: https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  chrpath
# For kmod package
Provides:       %{name} = %{version}-%{release}
Provides:       intel-ipu6-kmod-common = %{version}

ExclusiveArch:  x86_64

%description
This provides the necessary binaries for Intel IPU6, including library and firmware.
The library includes necessary image processing algorithms and 3A algorithm for the
camera.

%package firmware
Summary: IPU6 firmware

Provides:         %{name}-firmware = %{version}-%{release}
Requires:         %{name} = %{version}-%{release}

%description firmware
This provides the necessary firmwares for Intel IPU6.

%package devel
Summary: IPU6 header files for development.

%description devel
This provides the necessary header files for IPU6 development.

Provides:         %{name}-devel = %{version}-%{release}
Requires:         %{name} = %{version}-%{release}


%prep

%setup -q -c
cp %{name}-%{commit}/LICENSE ./
cd %{name}-%{commit}
for i in ipu6 ipu6ep; do
  chrpath --delete $i/lib/*.so
done
cd ..

%build
# Nothing to build

%install
for i in ipu6 ipu6ep; do
  mkdir -p %{buildroot}%{_libdir}/$i
  cp -pr %{name}-%{commit}/$i/lib/lib* %{buildroot}%{_libdir}/$i
done
for i in ipu6 ipu6ep; do
  mkdir -p %{buildroot}%{_includedir}/$i
  mkdir -p %{buildroot}%{_libdir}/$i
  cp -pr %{name}-%{commit}/$i/include/* %{buildroot}%{_includedir}/$i/
  cp -pr %{name}-%{commit}/$i/lib/lib* %{name}-%{commit}/$i/lib/pkgconfig %{buildroot}%{_libdir}/$i
  sed -i \
    -e "s|libdir=/usr/lib|libdir=%{_libdir}|g" \
    -e "s|libdir}|libdir}/$i|g" \
    -e "s|includedir}|includedir}/$i|g" \
    %{buildroot}%{_libdir}/$i/pkgconfig/*.pc
done

# IPU6 firmwares
install -D -m 0644 %{name}-%{commit}/ipu6/lib/firmware/intel/ipu6_fw.bin %{buildroot}%{_prefix}/lib/firmware/intel/ipu6_fw.bin
install -D -m 0644 %{name}-%{commit}/ipu6ep/lib/firmware/intel/ipu6ep_fw.bin %{buildroot}%{_prefix}/lib/firmware/intel/ipu6ep_fw.bin

%files
%license LICENSE
%dir %{_libdir}/ipu6
%{_libdir}/ipu6/*.so*
%{_libdir}/ipu6/*.a
%dir %{_libdir}/ipu6ep
%{_libdir}/ipu6ep/*.so*
%{_libdir}/ipu6ep/*.a

%files firmware
%license LICENSE
%{_prefix}/lib/firmware/intel/ipu6_fw.bin
%{_prefix}/lib/firmware/intel/ipu6ep_fw.bin

%files devel
%license LICENSE
%{_includedir}/ipu6
%{_includedir}/ipu6ep
%{_libdir}/ipu6/pkgconfig/
%{_libdir}/ipu6ep/pkgconfig/


%changelog
* Tue Oct 25 2022 Kate Hsuan <hpa@redhat.com> - 0.0.1
- First commit
