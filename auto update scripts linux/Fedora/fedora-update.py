#!/usr/bin/env python3
import subprocess
import sys

def run_fedora_update():
    try:
        print("Updating Fedora system (dnf upgrade)...")
        subprocess.run(["sudo", "dnf", "upgrade", "-y"], check=True)
        print("System update completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_fedora_update()
