#!/usr/bin/env python3
import subprocess
import sys

def run_debian_update_upgrade():
    try:
        print("Updating package lists (apt update)...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("Upgrading packages (apt upgrade)...")
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        print("System update and upgrade completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update/upgrade: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_debian_update_upgrade()
