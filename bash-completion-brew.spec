%global srcname bash-completion
Name:           %{srcname}-brew
Version:        2.1
Release:        1%{?dist}
Summary:        Programmable completion for brew cli

License:        GPLv2+
URL:            http://bash-completion.alioth.debian.org/
Source0:        http://bash-completion.alioth.debian.org/files/%{srcname}-%{version}.tar.bz2
Source1:        brew
Source2:        README.package

BuildArch:      noarch
Requires:       bash >= 4.1

# The target OSs that the package support are
# Fedora2X, RHEL6, and RHEL7. For more details
# please read the README.package file.

%if 0%{?rhel} <= 6
Requires:       bash-completion >= 1:2.1
%else
Requires:       bash-completion
%endif

%description
%{name} provides brew cli completion.


%prep
%setup -q -n %{srcname}-%{version}

%build
true


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%if 0%{?rhel} >= 7
install -pm 644 completions/koji \
    $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/koji
%endif

install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/brew

install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/README.package


%files
%{_datadir}/doc/%{name}
%if 0%{?rhel} >= 7
%{_datadir}/bash-completion/completions/koji
%endif
%{_datadir}/bash-completion/completions/brew


%changelog
* Tue Mar 15 2016 Xibo Ning <xing@redhat.com> - 2.1-1
- Init the project.
