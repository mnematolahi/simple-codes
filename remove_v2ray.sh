#!/bin/bash

# اسکریپت حذف کامل V2Ray نصب شده به صورت دستی

echo "--- شروع فرآیند حذف V2Ray ---"

# مرحله ۱: توقف و غیرفعال کردن سرویس
echo "مرحله ۱: در حال توقف و غیرفعال کردن سرویس v2ray..."
systemctl stop v2ray > /dev/null 2>&1
systemctl disable v2ray > /dev/null 2>&1

# مرحله ۲: حذف فایل سرویس
echo "مرحله ۲: در حال حذف فایل سرویس از systemd..."
rm -f /etc/systemd/system/v2ray.service
systemctl daemon-reload

# مرحله ۳: حذف فایل‌های اجرایی
echo "مرحله ۳: در حال حذف فایل اجرایی v2ray..."
rm -f /usr/local/bin/v2ray

# مرحله ۴: حذف پوشه‌های دیتا و کانفیگ
echo "مرحله ۴: در حال حذف پوشه‌های دیتا و کانفیگ..."
rm -rf /usr/local/share/v2ray
rm -rf /usr/local/etc/v2ray

# مرحله ۵: حذف پوشه لاگ (اختیاری)
echo "مرحله ۵: در حال حذف پوشه لاگ..."
rm -rf /var/log/v2ray

echo ""
echo "--- V2Ray با موفقیت به طور کامل حذف شد. ---"
