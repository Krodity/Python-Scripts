#!/usr/bin/env python3
import subprocess
import sys

def run_pacman_update():
    try:
        print("Updating package database and system with pacman...")
        subprocess.run(["sudo", "pacman", "-Syu"], check=True)
        print("System update completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pacman_update()
