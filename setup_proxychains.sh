#!/bin/bash

# #########################################################
# ##  اسکریپت نصب و تنظیم خودکار Proxychains-ng
# ##  این اسکریپت ابزار را نصب و آن را برای استفاده از پراکسی
# ##  SOCKS5 محلی روی پورت 10808 تنظیم می‌کند.
# #########################################################

# اطمینان از اجرای اسکریپت با دسترسی ریشه
if [[ $EUID -ne 0 ]]; then
   echo "خطا: این اسکریپت باید با دسترسی ریشه (sudo) اجرا شود."
   exit 1
fi

echo "--- شروع نصب و تنظیم Proxychains ---"

# مرحله ۱: نصب بسته
echo "مرحله ۱: در حال نصب بسته proxychains-ng..."
apt-get update > /dev/null 2>&1
apt-get install -y proxychains-ng > /dev/null 2>&1
echo "بسته با موفقیت نصب شد."

# مرحله ۲: تنظیم فایل کانفیگ
echo "مرحله ۲: در حال ویرایش فایل کانفیگ..."

# غیرفعال کردن پراکسی پیش‌فرض (خطی که با socks4 شروع می‌شود)
sed -i '/^socks4/s/^/#/' /etc/proxychains4.conf

# افزودن پراکسی SOCKS5 مربوط به V2Ray
# ابتدا چک می‌کنیم که این خط از قبل وجود نداشته باشد
if ! grep -q "socks5 127.0.0.1 10808" /etc/proxychains4.conf; then
    echo "socks5 127.0.0.1 10808" >> /etc/proxychains4.conf
    echo "پراکسی V2Ray با موفقیت به کانفیگ اضافه شد."
else
    echo "پراکسی V2Ray از قبل در کانفیگ وجود داشت."
fi

# مرحله ۳ (اختیاری): برداشتن کامنت از dynamic_chain برای پایداری بیشتر
sed -i 's/^# dynamic_chain/dynamic_chain/' /etc/proxychains4.conf
sed -i '/^strict_chain/s/^/#/' /etc/proxychains4.conf


echo ""
echo "--- تنظیمات Proxychains با موفقیت به پایان رسید! ---"
echo "اکنون می‌توانید با قرار دادن 'proxychains4' قبل از هر دستوری، آن را از طریق پراکسی اجرا کنید."
echo "مثال: proxychains4 curl ipinfo.io"
