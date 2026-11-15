
# ⚡️ ElecnoTech Wi-Fi Tool v6.1

[![YouTube](https://img.shields.io/badge/YouTube-@ElecnoTech-red)](https://www.youtube.com/@ElecnoTech)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

> 🌐 زبان / Language: [🇬🇧 English (کلیک کنید)](README.md) — | — 🇮🇷 فارسی (فعلی)

ابزار اسکن و تست رمز وای‌فای با وردلیست — فقط برای تست روی شبکه‌های خودتان یا با مجوز کتبی صاحب شبکه!
دسترسی غیرمجاز به شبکه‌های وای‌فای در اکثر کشورها جرم است.

---

## ✨ امکانات

- 🔍 اسکن شبکه‌های اطراف با نمایش قدرت سیگنال و BSSID
- 🎯 انتخاب چند هدف به‌صورت همزمان (مثلاً `1,3,5`)
- 📂 تست با وردلیست دلخواه (`rockyou.txt`, `common.txt`, ...)
- 📊 نوار پیشرفت زنده + خلاصهٔ نتایج در پایان
- 🖥 خروجی ساده و بدون کاراکتر خراب در تمام کنسول‌های ویندوز
- ⚡️ فایل EXE آماده — نیازی به نصب پایتون نیست

## 🚀 اجرای سریع (فایل EXE — پیشنهادی)

1. فایل `ElecnoTech-WiFi-Tool.exe` را از بخش [Releases](../../releases) دانلود کنید.
2. Run as Administrator اجرا کنید (برای دسترسی به مودم وای‌فای لازم است).
3. از منو، شمارهٔ شبکه‌های هدف را با کاما جدا کنید (مثلاً `1,3`).
4. مسیر وردلیست را بدهید (مثلاً `C:\wordlists\rockyou.txt`).
5. صبر کنید تا نتیجه بیاید! ✅

## 🐍 اجرا با پایتون

```bash
pip install pywifi colorama tqdm
python wifi.py -w C:\wordlists\rockyou.txt
```

> فقط روی ویندوز کار می‌کند (محدودیت pywifi) + نیاز به کارت وای‌فای دارد.

## 🔨 ساخت فایل EXE

دو روش:

- یک‌کلیکی: فایل `build_exe.bat` را روی هر ویندوزی که پایتون دارد دابل‌کلیک کنید.
- خودکار (GitHub Actions): ریپو را push کنید → تب Actions → Build Windows EXE → Run workflow → EXE را از Artifacts دانلود کنید (~۲ دقیقه).

## 🛠 نحوهٔ کار

1. شبکه‌های اطراف با کارت وای‌فای شما اسکن می‌شوند (pywifi).
2. یک یا چند هدف انتخاب می‌کنید.
3. وردلیست لود می‌شود و هر رمز روی هدف تست می‌شود.
4. وقتی رمز درست پیدا شد، فوراً نمایش داده می‌شود و در خلاصهٔ نهایی می‌آید.

## ⚠️ هشدار حقوقی

این ابزار صرفاً برای مصارف آموزشی و آزمایش امنیت شبکهٔ خودتان است.
دسترسی غیرمجاز به شبکه‌های رایانه‌ای در اکثر کشورها جرم است.
مسئولیت هر سوءاستفاده کاملاً بر عهدهٔ کاربر است.

---

## 📺 یوتیوب

ترفندها و ابزارهای خفن تکنولوژی را در کانال ما دنبال کنید 🎬
[Subscribe → @ElecnoTech](https://www.youtube.com/@ElecnoTech)

## 📬 ارتباط

- YouTube: [@ElecnoTech](https://www.youtube.com/@ElecnoTech)

## 📄 لایسنس

MIT — آزاد برای استفاده، اشتراک‌گذاری و تغییر (فقط مصرف آموزشی).
مشاهدهٔ [LICENSE](LICENSE).
