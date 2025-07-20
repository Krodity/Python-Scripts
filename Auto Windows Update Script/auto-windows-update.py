import subprocess
import sys
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def relaunch_as_admin():
    print("Requesting administrator privileges (UAC popup)...")
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]])
    # Use ShellExecuteW to show UAC popup
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{script}" {params}', None, 1
    )
    sys.exit(0)

def run_windows_update():
    print("Running Windows system updates (this may take a while)...")
    try:
        import_cmd = "Import-Module PSWindowsUpdate"
        update_cmd = "Get-WindowsUpdate -AcceptAll -Install -AutoReboot"
        full_cmd = f"{import_cmd}; {update_cmd}"
        result = subprocess.run([
            "powershell",
            "-Command",
            full_cmd
        ], check=False)
        if result.returncode != 0:
            print("PSWindowsUpdate module not found. Attempting to install for current user...")
            install_cmd = "Install-Module PSWindowsUpdate -Force -Scope CurrentUser"
            full_cmd = f"{install_cmd}; {import_cmd}; {update_cmd}"
            subprocess.run([
                "powershell",
                "-Command",
                full_cmd
            ], check=True)
        print("Windows system updates completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Windows Update: {e}")
        sys.exit(1)

def run_winget_update():
    print("Running winget upgrades for all packages...")
    try:
        subprocess.run(["winget", "upgrade", "--all", "--silent"], check=True)
        print("winget package updates completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during winget update: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if not is_admin():
        relaunch_as_admin()
    run_windows_update()
    run_winget_update()
