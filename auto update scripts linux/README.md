# Linux Auto Update Scripts

This directory contains Python scripts to automatically update your Linux system using your distribution's package manager (Arch, Debian, Fedora).

## Scripts
- **Arch/arch-update.py**: Updates Arch Linux using pacman
- **Arch/yay-update.py**: Updates Arch Linux and AUR packages using yay
- **Debian/debian-updates.py**: Updates Debian/Ubuntu using apt
- **Fedora/fedora-update.py**: Updates Fedora using dnf

## Requirements
- Python 3
- The appropriate package manager for your distribution (pacman, yay, apt, dnf)

## How to Set Up Auto-Update at Boot (systemd)

You can use a systemd service to run these scripts automatically every time your machine boots.

### 1. Make the Script Executable

```sh
chmod +x /path/to/your/script.py
```

### 2. Create a systemd Service File

Create a file like `/etc/systemd/system/auto-update.service` with the following content (replace the script path and user as needed):

```
[Unit]
Description=Automatic System Update
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /path/to/your/script.py
User=yourusername

[Install]
WantedBy=multi-user.target
```

- Replace `/path/to/your/script.py` with the full path to your update script (e.g., `/home/yourusername/auto update scripts linux/Debian/debian-updates.py`).
- Replace `yourusername` with your actual username.

### 3. Reload systemd and Enable the Service

```sh
sudo systemctl daemon-reload
sudo systemctl enable auto-update.service
```

This will run the update script at every boot.

### 4. (Optional) Run the Service Immediately

```sh
sudo systemctl start auto-update.service
```

## Notes
- The update scripts require root privileges to install updates. The service will prompt for a password unless you configure passwordless sudo for the update commands (not recommended for security reasons).
- You can modify the service to run at a different schedule using a systemd timer or cron if you prefer.
- For AUR updates with yay, ensure yay is installed and available in your PATH.

## Troubleshooting
- Check the status and logs with:
  ```sh
  sudo systemctl status auto-update.service
  journalctl -u auto-update.service
  ```
- Make sure the script runs correctly when executed manually before automating. 