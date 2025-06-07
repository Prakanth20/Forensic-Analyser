import os
import platform
import getpass
import socket
import psutil
import browserhistory as bh
from datetime import datetime
from pathlib import Path
import pyautogui

def get_system_info():
    print("\n[+] System Information")
    print("OS:", platform.system(), platform.release())
    print("Username:", getpass.getuser())
    print("Hostname:", socket.gethostname())

def list_logged_in_users():
    print("\n[+] Logged-in Users:")
    try:
        for user in psutil.users():
            print(user.name, "from", user.host, "since", datetime.fromtimestamp(user.started))
    except Exception as e:
        print("[-] Error:", e)

def get_browser_history():
    print("\n[+] Browser History (Chrome/Firefox)")
    try:
        bh_data = bh.get_browserhistory()
        for browser, data in bh_data.items():
            print(f"\n--- {browser} ---")
            for entry in data[:5]:  # show top 5 entries
                print("Visited:", entry[0], "at", entry[2])
    except Exception as e:
        print("[-] Error retrieving browser history:", e)

def list_wifi_profiles():
    print("\n[+] Saved Wi-Fi Networks and Passwords:")
    try:
        if platform.system() == "Linux":
            networks = os.popen("nmcli -t -f NAME connection show").read().splitlines()
            for net in networks:
                print("Wi-Fi:", net, "(Password retrieval not supported in this script on Linux)")
        
        elif platform.system() == "Windows":
            output = os.popen("netsh wlan show profiles").read()
            profiles = []
            for line in output.splitlines():
                if "All User Profile" in line:
                    profile = line.split(":")[1].strip()
                    profiles.append(profile)

            if profiles:
                for profile in profiles:
                    print(f"\n[+] SSID: {profile}")
                    # Attempt to get the password for the profile
                    details = os.popen(f'netsh wlan show profile name="{profile}" key=clear').read()
                    password = None
                    for line in details.splitlines():
                        if "Key Content" in line:
                            password = line.split(":")[1].strip()
                            break
                    if password:
                        print(f"    Password: {password}")
                    else:
                        print("    Password: Not found or not saved.")
            else:
                print("[-] No Wi-Fi profiles found.")
        else:
            print("[-] Unsupported OS for Wi-Fi listing.")
    except Exception as e:
        print("[-] Cannot retrieve Wi-Fi data:", e)

def list_recent_files(home_dir=None):
    print("\n[+] Recently Accessed Files:")
    if home_dir is None:
        home_dir = str(Path.home())

    recent_files = []
    for root, dirs, files in os.walk(home_dir):
        for name in files:
            try:
                full_path = os.path.join(root, name)
                atime = os.path.getatime(full_path)
                recent_files.append((full_path, atime))
            except Exception:
                continue

    recent_files.sort(key=lambda x: x[1], reverse=True)
    for file, atime in recent_files[:5]:
        print(datetime.fromtimestamp(atime), "-", file)

def list_usb_devices():
    print("\n[+] USB Device History:")
    try:
        if platform.system() == "Linux":
            output = os.popen("lsusb").read()
            if output:
                print(output)
            else:
                print("[-] No USB devices found or lsusb not installed.")
        
        elif platform.system() == "Windows":
            print("[*] Fetching USB device history from Windows registry (connected devices)...")
            output = os.popen('powershell "Get-WmiObject Win32_USBControllerDevice | '
                              'ForEach-Object { ([wmi]($_.Dependent)).Name }"').read()
            devices = [line.strip() for line in output.splitlines() if line.strip()]
            if devices:
                for dev in devices:
                    print("USB:", dev)
            else:
                print("[-] No USB devices found or access denied.")
        else:
            print("[-] Unsupported OS for USB listing.")
    except Exception as e:
        print("[-] Error fetching USB devices:", e)

def take_screenshot():
    print("\n[+] Taking Screenshot...")
    try:
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        print(f"[+] Screenshot saved as: {filename}")
    except Exception as e:
        print("[-] Error taking screenshot:", e)

def main():
    print("=== Forensic Analyzer Started ===")
    get_system_info()
    list_logged_in_users()
    get_browser_history()
    list_wifi_profiles()
    list_recent_files()
    list_usb_devices()
    take_screenshot()
    print("\n[✓] Forensic analysis completed.")

if __name__ == "__main__":
    main()
