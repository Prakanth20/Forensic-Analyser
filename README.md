# 🕵️‍♂️ Forensic Analyzer

A Python-based forensic tool that gathers detailed information from a target system including system data, user sessions, browser history, Wi-Fi profiles, USB device history, and more. It can also capture a screenshot for visual context.

## 📦 Features

* System information (OS, username, hostname)
* Logged-in users and session details
* Browser history (Chrome, Firefox)
* Saved Wi-Fi profiles and passwords (Windows only)
* Recently accessed files
* USB device history
* Full-screen screenshot

## 🛠 Requirements

* Python 3.6+
* Dependencies:

  * `psutil`
  * `browserhistory`
  * `pyautogui`

Install dependencies:

```bash
pip install psutil browserhistory pyautogui
```

> ⚠️ On Linux, `lsusb` must be installed for USB listing:
>
> ```bash
> sudo apt install usbutils
> ```

## 🚀 Usage

Run the script using:

```bash
python forensic_analyzer.py
```

## 📁 Output

* Console logs provide all information gathered.
* Screenshot is saved in the script's directory as `screenshot_YYYYMMDD_HHMMSS.png`.

## 🔒 Platform Support

| Feature                 | Windows           | Linux           | macOS |
| ----------------------- | ----------------- | --------------- | ----- |
| System Info             | ✅                 | ✅               | ✅     |
| Logged-in Users         | ✅                 | ✅               | ✅     |
| Browser History         | ✅                 | ✅               | ✅     |
| Wi-Fi Profiles          | ✅ (with password) | ✅ (no password) | ❌     |
| Recently Accessed Files | ✅                 | ✅               | ✅     |
| USB Devices             | ✅                 | ✅               | ❌     |
| Screenshot              | ✅                 | ✅               | ✅     |

---

## ⚠️ Disclaimer

This tool is intended for **educational and forensic analysis** purposes only. Ensure you have **explicit permission** to use this on any device. Unauthorized usage may be illegal.

---
