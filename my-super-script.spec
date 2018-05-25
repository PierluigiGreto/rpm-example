Name: my-super-script
Version: 0.1
Release: 0%{?dist}
Summary: bla bellooooo
License: Apache
Source0: my-super-script.tar.gz

%global debug_package %{nil}

%description
more text lineeeeee
kakak

%prep
%setup -c

%build
echo "build"



%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 my-super-script.sh %{buildroot}/usr/bin/my-super-script.sh




%files
/usr/bin/my-super-script.sh


%changelog
