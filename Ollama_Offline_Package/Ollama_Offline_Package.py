# --- مرحله ۱: نصب و اجرای اولیه اولاما ---
import os
import time

print("⏳ در حال نصب اولاما در محیط کولب...")
# دانلود و اجرای اسکریپت نصب رسمی اولاما
!curl -fsSL https://ollama.com/install.sh | sh
print("✅ اولاما با موفقیت نصب شد.")

# اجرای سرور اولاما در پس‌زمینه
!ollama serve &

# کمی صبر برای اجرای کامل سرور
print("⏳ منتظر بمانید تا سرور اولاما آماده شود...")
time.sleep(10)
print("✅ سرور اولاما آماده است.")


# --- مرحله ۲: دانلود تمام مدل‌های مورد نیاز (نسخه کامل) ---
models_to_pull = [
    # مدل‌های عمومی و مکالمه
    "llama3",
    "qwen2:7b",
    "mistral",
    "gemma:7b",
    "command-r",
    
    # مدل‌های تخصصی کدنویسی
    "codestral",          # <--- مدل کدنویسی میسترال
    "deepseek-coder"      # <--- مدل کدنویسی دیپ‌سیک
]

print("\n" + "="*50)
print("⏳ شروع دانلود مدل‌ها با اولاما...")
print("این فرآیند بسته به تعداد و حجم مدل‌ها ممکن است بسیار طولانی شود.")
print("="*50)

for model in models_to_pull:
    print(f"\n--- 📥 در حال دانلود مدل: {model} ---")
    !ollama pull {model}

print("\n✅ تمام مدل‌های درخواستی دانلود شدند.")


# --- مرحله ۳: آرشیو کردن اولاما و مدل‌های آن ---
print("\n" + "="*50)
print("⏳ در حال ساخت پکیج آفلاین نهایی...")
print("="*50)

# اتصال به گوگل درایو
from google.colab import drive
drive.mount('/content/drive')

# تعریف نام و مسیر فایل خروجی
archive_path = "/content/drive/MyDrive/Ollama_Offline_Package_Complete.tar.gz"

# فشرده‌سازی فایل اجرایی اولاما و پوشه مدل‌ها
!tar -czf {archive_path} /usr/local/bin/ollama /root/.ollama

print("\n" + "="*50)
print(f"🎉🎉🎉 پکیج آفلاین با موفقیت ساخته و در گوگل درایو شما ذخیره شد!")
print(f"مسیر فایل: {archive_path}")
print("="*50)
