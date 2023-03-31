%global debug_package %{nil}
%global _efi_vendor_ %(eval echo $(. /etc/os-release && echo $ID))

Summary: Common RPM Macros for building EFI-related packages
Name: efi-rpm-macros
Version: 5
Release: 2
License: GPLv3+
URL: https://github.com/rhboot/%{name}/
Source0: https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0: https://src.fedoraproject.org/rpms/efi-rpm-macros/raw/rawhide/f/0001-Don-t-have-arm-as-an-alt-arch-of-aarch64.patch
BuildRequires: git
BuildRequires: sed
BuildArch: noarch

%description
%{name} provides a set of RPM macros for use in EFI-related packages.

%package -n efi-srpm-macros
Summary: Common SRPM Macros for building EFI-related packages
BuildArch: noarch
Requires: rpm

%description -n efi-srpm-macros
efi-srpm-macros provides a set of SRPM macros for use in EFI-related packages.

%package -n efi-filesystem
Summary: The basic directory layout for EFI machines
BuildArch: noarch
Requires: filesystem

%description -n efi-filesystem
The efi-filesystem package contains the basic directory layout for EFI
machine bootloaders and tools.

%prep
%autosetup -S git
git config --local --add efi.vendor "%{_efi_vendor_}"
git config --local --add efi.esp-root /boot/efi
git config --local --add efi.arches "x86_64 znver1 aarch64 %{arm} %{ix86}"

%build
%make_build clean all

%install
%make_install

%files -n efi-srpm-macros
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README
%{_rpmmacrodir}/macros.efi-srpm
%{_rpmconfigdir}/brp-boot-efi-times

%files -n efi-filesystem
%defattr(0700,root,root,-)
%dir /boot/efi
%dir /boot/efi/EFI
%dir /boot/efi/EFI/BOOT
%dir /boot/efi/EFI/%{_efi_vendor_}
