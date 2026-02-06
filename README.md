# simple-node-http (RPM)

Simple Node.js HTTP service packaged as an RPM for Rocky Linux / RHEL-like systems.

The service starts via `systemd`, listens on port **3000**, and responds with `OK`.

This project demonstrates:
- RPM packaging
- systemd service integration
- separation of code and configuration
- proper install / upgrade / remove lifecycle

---

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
