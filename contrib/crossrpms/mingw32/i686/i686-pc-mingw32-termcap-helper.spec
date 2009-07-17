Name:           i686-pc-mingw32-termcap-helper
Version:        0.20090122.0
Release:        1%{?dist}
Summary:        RTEMS mingw32 termcap libs helper

Group:          Development
License:        GPLv3+
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:  mingw32-termcap
Requires:       mingw32-termcap
Provides:	i686-pc-mingw32-termcap
Provides:	i686-pc-mingw32-termcap-devel

%description
%{summary}

%prep
%setup -q -c -T -n %{name}-%{version}

%build

%files

%changelog
