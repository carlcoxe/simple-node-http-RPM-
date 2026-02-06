Name:           simple-node-http
Version:        1.0
Release:        1%{?dist}
Summary:        Simple Node.js HTTP service

License:        MIT
BuildArch:      x86_64
Requires:       nodejs

%Description
Simple Node.js HTTP service managed by systemd.

%Install
mkdir -p %{buildroot}/opt/simple-node
cp %{_sourcedir}/server.js %{buildroot}/opt/simple-node/

mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{_sourcedir}/simple-node.service %{buildroot}/usr/lib/systemd/system/

mkdir -p %{buildroot}/etc/simple-node
cp %{_sourcedir}/config.env %{buildroot}/etc/simple-node/

%Files
/opt/simple-node/server.js
/usr/lib/systemd/system/simple-node.service
/etc/simple-node/config.env

%Post
systemctl daemon-reload || true

%Preun
if [ $1 -eq 0 ]; then
  systemctl stop simple-node.service || true
  systemctl disable simple-node.service || true
fi

%Postun
systemctl daemon-reload || true

