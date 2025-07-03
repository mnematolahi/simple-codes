#!/bin/bash

# #########################################################
# ## اسکریپت نصب خودکار و مستقیم V2Ray Core
# ## نویسنده: راهبرد پردازش
# ## تاریخ: 3 جولای 2025
# ## توضیحات: این اسکریپت V2Ray را به صورت دستی و مطمئن نصب می‌کند.
# #########################################################


# --- اطمینان از اجرای اسکریپت با دسترسی ریشه ---
if [[ $EUID -ne 0 ]]; then
   echo "خطا: این اسکریپت باید با دسترسی ریشه (sudo) اجرا شود." 
   exit 1
fi

# --- شروع فرآیند ---
echo "--- شروع فرآیند نصب V2Ray ---"


# --- مرحله ۱: نصب ابزارهای مورد نیاز ---
echo "مرحله ۱: در حال نصب ابزارهای مورد نیاز (curl و unzip)..."
apt-get update > /dev/null 2>&1
apt-get install -y curl unzip > /dev/null 2>&1
echo "ابزارهای مورد نیاز با موفقیت نصب شدند."


# --- مرحله ۲: دانلود و استخراج فایل‌های V2Ray ---
# فایل از همان لینکی که شما ارائه دادید دانلود می‌شود.
V2RAY_URL="https://digitalyn.ir/v2ray-linux-64.zip"
TMP_DIR="/tmp/v2ray-install"

echo "مرحله ۲: در حال دانلود فایل V2Ray از لینک شما..."
mkdir -p "$TMP_DIR"
curl -L -o "${TMP_DIR}/v2ray.zip" "$V2RAY_URL"

# بررسی موفقیت دانلود
if [ $? -ne 0 ]; then
    echo "خطا: دانلود فایل V2Ray با شکست مواجه شد. لطفاً از صحت لینک اطمینان حاصل کنید."
    rm -rf "$TMP_DIR"
    exit 1
fi

echo "در حال استخراج فایل‌ها در پوشه موقت..."
unzip -o "${TMP_DIR}/v2ray.zip" -d "${TMP_DIR}/v2ray-files" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "خطا: استخراج فایل زیپ با شکست مواجه شد."
    rm -rf "$TMP_DIR"
    exit 1
fi


# --- مرحله ۳: کپی کردن فایل‌ها به مسیرهای سیستمی ---
echo "مرحله ۳: در حال نصب فایل‌های اجرایی و دیتا..."

# ساخت پوشه‌های مقصد
mkdir -p /usr/local/bin/
mkdir -p /usr/local/share/v2ray/

# کپی فایل اجرایی اصلی
install -m 755 "${TMP_DIR}/v2ray-files/v2ray" /usr/local/bin/v2ray

# کپی فایل‌های دیتا
install -m 644 "${TMP_DIR}/v2ray-files/geoip.dat" /usr/local/share/v2ray/geoip.dat
install -m 644 "${TMP_DIR}/v2ray-files/geosite.dat" /usr/local/share/v2ray/geosite.dat


# --- مرحله ۴: ساخت فایل سرویس Systemd ---
echo "مرحله ۴: در حال ساخت سرویس Systemd برای اجرای V2Ray در پس‌زمینه..."
tee /etc/systemd/system/v2ray.service > /dev/null <<EOF
[Unit]
Description=V2Ray Service
After=network.target

[Service]
Type=simple
User=nobody
Group=nogroup
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
NoNewPrivileges=true
ExecStart=/usr/local/bin/v2ray run -config /usr/local/etc/v2ray/config.json
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF


# --- مرحله ۵: ساخت فایل کانفیگ اولیه ---
echo "مرحله ۵: در حال ساخت پوشه و فایل کانفیگ اولیه..."

# ساخت پوشه کانفیگ
mkdir -p /usr/local/etc/v2ray/

# ساخت یک فایل کانفیگ خالی استاندارد
tee /usr/local/etc/v2ray/config.json > /dev/null <<< "{}"

# تنظیم دسترسی صحیح
chown nobody:nogroup /usr/local/etc/v2ray/config.json


# --- مرحله ۶: راه‌اندازی نهایی سرویس ---
echo "مرحله ۶: در حال فعال‌سازی و راه‌اندازی سرویس V2Ray..."
systemctl daemon-reload
systemctl enable v2ray
systemctl start v2ray


# --- مرحله ۷: پاک‌سازی ---
echo "مرحله ۷: در حال پاک‌سازی فایل‌های موقت..."
rm -rf "$TMP_DIR"


# --- پایان ---
echo ""
echo "--- نصب با موفقیت به پایان رسید! ---"
echo "سرویس V2Ray اکنون در حال اجرا است."
echo "برای بررسی وضعیت، دستور 'sudo systemctl status v2ray' را اجرا کنید."
echo "برای ویرایش کانفیگ، فایل '/usr/local/etc/v2ray/config.json' را تغییر دهید."
