# ⚡ ElecnoTech Wi-Fi Tool v6.1

[![YouTube](https://img.shields.io/badge/YouTube-@ElecnoTech-red)](https://www.youtube.com/@ElecnoTech)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)]()

**English below / فارسی پایین 👇**

---

## 🇮🇷 فارسی

ابزار اسکن و تست رمز وای‌فای با وردلیست — **فقط برای تست روی شبکه‌های خودتان یا با مجوز کتبی صاحب شبکه!** دسترسی غیرمجاز به شبکه‌های وای‌فای در اکثر کشورها جرم است.

### ✨ امکانات
- 🔍 اسکن شبکه‌های اطراف با نمایش قدرت سیگنال و BSSID
- 🎯 انتخاب چند هدف به‌صورت همزمان (مثلاً `1,3,5`)
- 📂 تست با وردلیست دلخواه (`rockyou.txt`, `common.txt`, ...)
- 📊 نوار پیشرفت زنده + خلاصهٔ نتایج در پایان
- 🖥 خروجی ساده و بدون کاراکتر خراب در تمام کنسول‌های ویندوز
- ⚡ فایل EXE آماده — نیازی به نصب پایتون نیست

### 🚀 اجرای سریع (فایل EXE)
1. فایل `ElecnoTech-WiFi-Tool.exe` را از بخش [Releases](../../releases) دانلود کنید.
2. **Run as Administrator** کنید (برای دسترسی به مودم وای‌فای لازم است).
3. از منو، شمارهٔ شبکه‌های هدف را با کاما جدا کنید (مثلاً `1,3`).
4. مسیر وردلیست را بدهید (مثلاً `C:\wordlists\rockyou.txt`).
5. صبر کنید تا نتیجه بیاید! ✅

### 🐍 اجرا با پایتون
```bash
pip install pywifi colorama tqdm
python wifi.py -w C:\wordlists\rockyou.txt
```

### ⚠️ هشدار حقوقی
این ابزار صرفاً جنبهٔ آموزشی و آزمایش امنیت شبکهٔ خودتان را دارد.
هر سوءاستفاده بر عهدهٔ کاربر است.

---

## 🇬🇧 English

Wi-Fi scanner & wordlist-based password tester.
**Use ONLY on networks you own or have written permission to test!**

### Features
- 🔍 Nearby network scan with signal strength + BSSID
- 🎯 Multi-target selection (e.g. `1,3,5`)
- 📂 Any wordlist you want (`rockyou.txt`, ...)
- 📊 Live progress bar + final summary
- 🖥 Clean, plain-text console output
- ⚡ Ready-made EXE — no Python installation required

### Quick Start (EXE)
1. Download `ElecnoTech-WiFi-Tool.exe` from [Releases](../../releases).
2. Run as Administrator.
3. Pick target networks by number (comma-separated).
4. Point to your wordlist path.
5. Wait for results! ✅

### Run with Python
```bash
pip install pywifi colorama tqdm
python wifi.py -w C:\wordlists\rockyou.txt
```

### ⚠️ Legal
Educational purpose only. Misuse is your own responsibility.

---

## 📺 YouTube
- ترفندها و ابزارهای خفن تکنولوژی را در کانال ما دنبال کنید 🎬
- **[Subscribe @ElecnoTech](https://www.youtube.com/@ElecnoTech)**

## 📬 Contact
- YouTube: [@ElecnoTech](https://www.youtube.com/@ElecnoTech)

## 📄 License
MIT — free to use, share and modify (educational use only).
