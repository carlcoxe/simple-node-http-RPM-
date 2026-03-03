# simple-node-http (RPM)

Simple Node.js HTTP service packaged as an RPM for Rocky Linux / RHEL-like systems.

The service starts via `systemd`, listens on port **3000**, and responds with `OK`.

This project demonstrates:
- RPM packaging
- systemd service integration
- separation of code and configuration
- proper install / upgrade / remove lifecycle

---

## 🚀 Installation methods

You can run this service in **two ways**:

1. Install as a **native RPM package**
2. Run as a **container using Podman**

Choose the method that fits your environment.

## 🧩 Method 1: Install via RPM (native system service)

## 📦 Requirements

Node.js **must be installed on the system** before installing this RPM.

Install Node.js using DNF:

```bash
sudo dnf install nodejs
```
Verify instalation 
```bash
node --version
```
# RPM Build
```bash
sudo dnf install rpm-build
```
# Build package
```bash
rpmbuild -ba SPECS/simple-node-http.spec
```
# The RPM will be created in:
```bash
~/rpmbuild/RPMS/x86_64/
```
# Install
```bash
sudo rpm -Uvh simple-node-http-*.rpm
```

# ▶️ Service management
Enable and start the service:
```bash
sudo systemctl enable simple-node.service
sudo systemctl start simple-node.service
```
# Check status
```bash
systemctl status simple-node.service
```
# Test
```bash
curl http://localhost:3000
```
# Exception output
OK

# Remove
```bash
sudo rpm -e simple-node-http  
```
# Method  2: Run via Podman container
Requirements
```bash
sudo dnf install -y podman
```

🧩 ##  Build container image
```bash
podman build -t simple-node-http .
```
## 🧩  Run container
```bash
podman run -p 3000:3000 simple-node-http
```
##🧩   test
``` bash
podman run -p 3000:3000 simple-node-http
```

simple-node-http-RPM-/
├── Containerfile
├── README.md
├── requirements.txt
├── SOURCES/
│   ├── server.js
│   ├── simple-node.service
│   └── config.env
├── SPECS/
│   └── simple-node-http.spec

