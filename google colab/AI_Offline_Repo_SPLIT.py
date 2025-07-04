# --- مرحله ۱: اتصال به گوگل درایو ---
from google.colab import drive
drive.mount('/content/drive')
import os

# --- مرحله ۲: تنظیمات ---

# نام فایل فشرده بزرگی که در مرحله قبل ساختید
archive_name = "AI_Offline_Repo_FULL.tar.gz"
archive_path = f"/content/drive/MyDrive/{archive_name}"

# پوشه‌ای جدید برای ذخیره فایل‌های تقسیم شده
split_dir = "/content/drive/MyDrive/AI_Offline_Repo_SPLIT"
os.makedirs(split_dir, exist_ok=True)

# حجم هر قطعه (مثلا 900M برای ۹۰۰ مگابایت یا 1G برای ۱ گیگابایت)
split_size = "900M"


# --- مرحله ۳: تقسیم فایل ---
if not os.path.exists(archive_path):
    print(f"❌ خطا: فایل {archive_path} پیدا نشد. لطفاً ابتدا اسکریپت اول را اجرا کنید.")
else:
    print(f"⏳ شروع تقسیم فایل {archive_name} به قطعات {split_size}...")
    # پیشوند فایل‌های خروجی: archive_name.part_
    !split -b {split_size} {archive_path} {split_dir}/{archive_name}.part_

    print("\n🎉🎉🎉 عملیات تقسیم با موفقیت انجام شد! 🎉🎉🎉")
    print(f"فایل‌های تقسیم شده در پوشه زیر در گوگل درایو شما ذخیره شدند:\n{split_dir}")
