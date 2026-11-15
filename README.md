
# ⚡️ ElecnoTech Wi-Fi Tool v6.1

[![YouTube](https://img.shields.io/badge/YouTube-@ElecnoTech-red)](https://www.youtube.com/@ElecnoTech)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

> 🌐 Language / زبان: English (default) — | — [🇮🇷 فارسی (click here)](README.fa.md)

Wi-Fi scanner & wordlist-based password tester.
Use ONLY on networks you own or have written permission to test!

---

## ✨ Features

- 🔍 Nearby network scan with signal strength + BSSID
- 🎯 Multi-target selection (e.g. `1,3,5`)
- 📂 Any wordlist you want (`rockyou.txt`, `common.txt`, ...)
- 📊 Live progress bar + final summary of found passwords
- 🖥 Clean, plain-text console output (no broken characters on any Windows console)
- ⚡️ Ready-made EXE — no Python installation required

## 🚀 Quick Start (EXE — recommended)

1. Download `ElecnoTech-WiFi-Tool.exe` from the [Releases](../../releases) section.
2. Run as Administrator (required to access your Wi-Fi adapter).
3. Pick target networks by number, comma-separated (e.g. `1,3`).
4. Point to your wordlist path (e.g. `C:\wordlists\rockyou.txt`).
5. Wait for results! ✅

## 🐍 Run with Python

```bash
pip install pywifi colorama tqdm
python wifi.py -w C:\wordlists\rockyou.txt
```

> Requires Windows (pywifi limitation) + a Wi-Fi adapter.

## 🔨 Build the EXE yourself

Two options:

- One-click: double-click `build_exe.bat` on any Windows machine with Python installed.
- Automatic (GitHub Actions): push this repo → go to the Actions tab → Build Windows EXE → Run workflow → download the EXE from Artifacts (~2 min).

## 🛠 How it works

1. Scans nearby networks using your Wi-Fi adapter (pywifi).
2. You select one or more targets.
3. It loads your wordlist and tries each password against the target.
4. When a password works, it is shown instantly and listed in the final summary.

## ⚠️ Legal

This tool is for educational purposes and authorized security testing only.
Unauthorized access to computer networks is illegal in most countries.
You are fully responsible for any misuse.

---

## 📺 YouTube

More awesome tech tricks & tools on our channel 🎬
[Subscribe → @ElecnoTech](https://www.youtube.com/@ElecnoTech)

## 📬 Contact

- YouTube: [@ElecnoTech](https://www.youtube.com/@ElecnoTech)

## 📄 License

MIT — free to use, share and modify (educational use only).
See [LICENSE](LICENSE).

