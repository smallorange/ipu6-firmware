%global __brp_check_rpaths %{nil}
%global debug_package %{nil}

Name:           ipu6-bin
Summary:        Binaries for Intel IPU6
Version:        0.0.1
Release:        2%{?dist}
License:        Proprietory

URL:            https://github.com/smallorange
Source0:        %{url}/ipu6-camera-bins/releases/download/%{version}/ipu6-camera-bins-%{version}.tar.xz
Source1:        %{url}/ivsc-firmware/releases/download/%{version}/ivsc-firmware-%{version}.tar.xz

BuildRequires:  systemd-rpm-macros
# For kmod package
Provides:       %{name} = %{version}-%{release}

BuildArch:      x86_64

%description
This provides the necessary firmwares for Intel IPU6, including IPU6 itself
and iVSC.

This package contains the binary firmware for %{name}.

%prep

%setup -q -c -a 1

echo "xxx"
cp ivsc-firmware-%{version}/LICENSE ./

%build
# Nothing to build


%install
# ipu6 bin
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libgcss.so.0 %{buildroot}%{_libdir}/ipu6/libgcss.so.0
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_aiq_file_debug.so %{buildroot}%{_libdir}/ipu6/libia_aiq_file_debug.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_cca.so %{buildroot}%{_libdir}/ipu6/libia_cca.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_dvs.so %{buildroot}%{_libdir}/ipu6/libia_dvs.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_lard.so %{buildroot}%{_libdir}/ipu6/libia_lard.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_mkn.so %{buildroot}%{_libdir}/ipu6/libia_mkn.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libipu6.a %{buildroot}%{_libdir}/ipu6/libipu6.a
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libbroxton_ia_pal.so %{buildroot}%{_libdir}/ipu6/libbroxton_ia_pal.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libgcss.so.0.0.0 %{buildroot}%{_libdir}/ipu6/libgcss.so.0.0.0
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_aiq.so %{buildroot}%{_libdir}/ipu6/libia_aiq.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_cmc_parser.so %{buildroot}%{_libdir}/ipu6/libia_cmc_parser.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_exc.so %{buildroot}%{_libdir}/ipu6/libia_exc.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_log.so %{buildroot}%{_libdir}/ipu6/libia_log.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_nvm.so %{buildroot}%{_libdir}/ipu6/libia_nvm.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libgcss.so %{buildroot}%{_libdir}/ipu6/libgcss.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_aiqb_parser.so %{buildroot}%{_libdir}/ipu6/libia_aiqb_parser.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_bcomp.so %{buildroot}%{_libdir}/ipu6/libia_bcomp.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_coordinate.so %{buildroot}%{_libdir}/ipu6/libia_coordinate.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_isp_bxt.so %{buildroot}%{_libdir}/ipu6/libia_isp_bxt.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_ltm.so %{buildroot}%{_libdir}/ipu6/libia_ltm.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/libia_p2p_ipu6.a %{buildroot}%{_libdir}/ipu6/libia_p2p_ipu6.a

# ipu6ep bin
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libbroxton_ia_pal.so %{buildroot}%{_libdir}/ipu6ep/libbroxton_ia_pal.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libgcss.so %{buildroot}%{_libdir}/ipu6ep/libgcss.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libgcss.so.0 %{buildroot}%{_libdir}/ipu6ep/libgcss.so.0
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libgcss.so.0.0.0 %{buildroot}%{_libdir}/ipu6ep/libgcss.so.0.0.0
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_aiqb_parser.so %{buildroot}%{_libdir}/ipu6ep/libia_aiqb_parser.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_aiq_file_debug.so %{buildroot}%{_libdir}/ipu6ep/libia_aiq_file_debug.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_aiq.so %{buildroot}%{_libdir}/ipu6ep/libia_aiq.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_bcomp.so %{buildroot}%{_libdir}/ipu6ep/libia_bcomp.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_cca.so %{buildroot}%{_libdir}/ipu6ep/libia_cca.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_cmc_parser.so %{buildroot}%{_libdir}/ipu6ep/libia_cmc_parser.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_coordinate.so %{buildroot}%{_libdir}/ipu6ep/libia_coordinate.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_dvs.so %{buildroot}%{_libdir}/ipu6ep/libia_dvs.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_exc.so %{buildroot}%{_libdir}/ipu6ep/libia_exc.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_isp_bxt.so %{buildroot}%{_libdir}/ipu6ep/libia_isp_bxt.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_lard.so %{buildroot}%{_libdir}/ipu6ep/libia_lard.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_log.so %{buildroot}%{_libdir}/ipu6ep/libia_log.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_ltm.so %{buildroot}%{_libdir}/ipu6ep/libia_ltm.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_mkn.so %{buildroot}%{_libdir}/ipu6ep/libia_mkn.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_nvm.so %{buildroot}%{_libdir}/ipu6ep/libia_nvm.so
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libia_p2p_ipu6ep.a %{buildroot}%{_libdir}/ipu6ep/libia_p2p_ipu6ep.a
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/libipu6ep.a %{buildroot}%{_libdir}/ipu6ep/libipu6ep.a


# IPU6 firmwares
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6/lib/firmware/intel/ipu6_fw.bin %{buildroot}%{_prefix}/lib/firmware/intel/ipu6_fw.bin
install -D -m 0644 ipu6-camera-bins-%{version}/ipu6ep/lib/firmware/intel/ipu6ep_fw.bin %{buildroot}%{_prefix}/lib/firmware/intel/ipu6ep_fw.bin

#iVSC firmwares
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti5678_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti5678_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti2740_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti2740_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti9738_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9738_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti2740_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti2740_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti02c1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti02c1_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_fw.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_fw_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti01af_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01af_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti01a0_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01a0_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti9734_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9734_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_hi556_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_hi556_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti01as_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01as_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti9738_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9738_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti5678_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti5678_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti02c1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti02c1_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti01as_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01as_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_ovti01af_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01af_0_1_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_himx11b1_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_himx11b1_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti9734_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9734_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_hi556_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_hi556_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_pkg_ovti01a0_0.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01a0_0_a1_prod.bin
install -D -m 0644 ivsc-firmware-%{version}/firmware/ivsc_skucfg_himx11b1_0_1.bin %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_himx11b1_0_1_a1_prod.bin

%files
%license LICENSE

%{_libdir}/ipu6/libgcss.so.0
%{_libdir}/ipu6/libia_aiq_file_debug.so
%{_libdir}/ipu6/libia_cca.so
%{_libdir}/ipu6/libia_dvs.so
%{_libdir}/ipu6/libia_lard.so
%{_libdir}/ipu6/libia_mkn.so
%{_libdir}/ipu6/libipu6.a
%{_libdir}/ipu6/libbroxton_ia_pal.so
%{_libdir}/ipu6/libgcss.so.0.0.0
%{_libdir}/ipu6/libia_aiq.so
%{_libdir}/ipu6/libia_cmc_parser.so
%{_libdir}/ipu6/libia_exc.so
%{_libdir}/ipu6/libia_log.so
%{_libdir}/ipu6/libia_nvm.so
%{_libdir}/ipu6/libgcss.so
%{_libdir}/ipu6/libia_aiqb_parser.so
%{_libdir}/ipu6/libia_bcomp.so
%{_libdir}/ipu6/libia_coordinate.so
%{_libdir}/ipu6/libia_isp_bxt.so
%{_libdir}/ipu6/libia_ltm.so
%{_libdir}/ipu6/libia_p2p_ipu6.a

# ipu6ep
%{_libdir}/ipu6ep/libbroxton_ia_pal.so
%{_libdir}/ipu6ep/libgcss.so
%{_libdir}/ipu6ep/libgcss.so.0
%{_libdir}/ipu6ep/libgcss.so.0.0.0
%{_libdir}/ipu6ep/libia_aiqb_parser.so
%{_libdir}/ipu6ep/libia_aiq_file_debug.so
%{_libdir}/ipu6ep/libia_aiq.so
%{_libdir}/ipu6ep/libia_bcomp.so
%{_libdir}/ipu6ep/libia_cca.so
%{_libdir}/ipu6ep/libia_cmc_parser.so
%{_libdir}/ipu6ep/libia_coordinate.so
%{_libdir}/ipu6ep/libia_dvs.so
%{_libdir}/ipu6ep/libia_exc.so
%{_libdir}/ipu6ep/libia_isp_bxt.so
%{_libdir}/ipu6ep/libia_lard.so
%{_libdir}/ipu6ep/libia_log.so
%{_libdir}/ipu6ep/libia_ltm.so
%{_libdir}/ipu6ep/libia_mkn.so
%{_libdir}/ipu6ep/libia_nvm.so
%{_libdir}/ipu6ep/libia_p2p_ipu6ep.a
%{_libdir}/ipu6ep/libipu6ep.a

%package firmware
Summary: IPU6 firmware

%description firmware
This provides the necessary firmwares for Intel IPU6, including IPU6 itself
and iVSC.

This package contains the binary firmware for %{name}.

%files firmware
%license LICENSE
# IPU6 firmware
%{_prefix}/lib/firmware/intel/ipu6_fw.bin
%{_prefix}/lib/firmware/intel/ipu6ep_fw.bin

#iVSC firmware
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti5678_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti2740_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9738_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti2740_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti02c1_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_fw_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01af_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01a0_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9734_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_hi556_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01as_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti9738_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti5678_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti02c1_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01as_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_ovti01af_0_1_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_himx11b1_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti9734_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_hi556_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_pkg_ovti01a0_0_a1_prod.bin
%{_prefix}/lib/firmware/vsc/soc_a1_prod/ivsc_skucfg_himx11b1_0_1_a1_prod.bin


%changelog
* Tue Oct 25 2022 Kate Hsuan <hpa@redhat.com> - 0.0.1
- First commit
