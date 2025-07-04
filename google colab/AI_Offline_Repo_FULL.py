# --- مرحله ۱: اتصال به گوگل درایو ---
from google.colab import drive
drive.mount('/content/drive')

import os

# --- مرحله ۲: تنظیمات اصلی ---

# مسیر اصلی در گوگل درایو برای ذخیره همه چیز
base_dir = "/content/drive/MyDrive/AI_Offline_Repo_FULL"
# نام فایل فشرده نهایی
archive_name = "AI_Offline_Repo_FULL.tar.gz"
archive_path = f"/content/drive/MyDrive/{archive_name}"

# لیست کامل کتابخانه‌های پایتون (ترکیب لیست قبلی و لیست شما با حذف موارد تکراری)
python_libraries = list(set([
    # Core AI & ML
    "torch", "torchvision", "torchaudio", "tensorflow", "transformers", "accelerate", "bitsandbytes",
    "datasets", "peft", "Pillow", "sentence-transformers", "tqdm",
    # LangChain Ecosystem
    "langchain", "langchain-community", "langchain-text-splitters", "chromadb",
    # Data Handling & PDF
    "PyMuPDF", "pdf2image", "PyYAML",
    # App & UI
    "streamlit", "streamlit-mermaid", "gradio",
    # Other Essentials
    "huggingface_hub", "jupyter", "faiss-cpu"
]))

# لیست مدل‌های هوش مصنوعی برای دانلود (فرمت GGUF از TheBloke)
# می‌توانید هر مدلی را که نمی‌خواهید با گذاشتن # در ابتدای خط آن، غیرفعال کنید
models_to_download = {
    # Gemma Models
    "gemma-2b-it": "TheBloke/gemma-2b-it-GGUF/gemma-2b-it.Q4_K_M.gguf",
    "gemma-7b-it": "TheBloke/gemma-7b-it-GGUF/gemma-7b-it.Q5_K_M.gguf",
    # Llama 3 Models
    "llama-3-8b-instruct": "TheBloke/Meta-Llama-3-8B-Instruct-GGUF/meta-llama-3-8b-instruct.Q4_K_M.gguf",
    "llama-3-70b-instruct": "TheBloke/Meta-Llama-3-70B-Instruct-GGUF/meta-llama-3-70b-instruct.Q4_K_M.gguf", # هشدار: این مدل بسیار بزرگ است (حدود ۴۰ گیگ)
    # DeepSeek Models
    "deepseek-coder-v2-lite": "TheBloke/deepseek-coder-v2-lite-instruct-GGUF/deepseek-coder-v2-lite-instruct.Q4_K_M.gguf",
    "deepseek-llm-7b-chat": "TheBloke/deepseek-llm-7b-chat-GGUF/deepseek-llm-7b-chat.Q5_K_M.gguf",
    # Qwen Models
    "qwen-1.5-4b-chat": "TheBloke/Qwen1.5-4B-Chat-GGUF/qwen1_5-4b-chat.Q5_K_M.gguf",
    "qwen-1.5-14b-chat": "TheBloke/Qwen1.5-14B-Chat-GGUF/qwen1_5-14b-chat.Q5_K_M.gguf"
}

# --- مرحله ۳: ساخت پوشه‌ها و دانلود ---

pypi_dir = os.path.join(base_dir, "PyPI_Libraries")
models_dir = os.path.join(base_dir, "AI_Models")
github_dir = os.path.join(base_dir, "GitHub_Tools")

os.makedirs(pypi_dir, exist_ok=True)
os.makedirs(models_dir, exist_ok=True)
os.makedirs(github_dir, exist_ok=True)
print(f"ساختار پوشه در مسیر {base_dir} ایجاد شد.")

# ۱. دانلود کتابخانه‌های PyPI
print("\n⏳ شروع دانلود کتابخانه‌های PyPI...")
requirements_path = "/content/requirements.txt"
with open(requirements_path, "w") as f:
    f.write("\n".join(python_libraries))
!pip download -r {requirements_path} -d {pypi_dir}
print("✅ دانلود کتابخانه‌های PyPI تمام شد.")

# ۲. دانلود مدل‌های هوش مصنوعی
print("\n⏳ شروع دانلود مدل‌های هوش مصنوعی...")
!pip install -q huggingface_hub
for name, path in models_to_download.items():
    repo_id, filename = path.split('/')
    print(f"--- در حال دانلود مدل: {name} ---")
    !huggingface-cli download {repo_id} {filename} --local-dir {models_dir}/{name} --local-dir-use-symlinks False
print("✅ دانلود مدل‌های هوش مصنوعی تمام شد.")

# ۳. دانلود ابزارهای گیت‌هاب
print("\n⏳ شروع دانلود ابزارهای گیت‌هاب (llama.cpp و text-generation-webui)...")
!git clone https://github.com/ggerganov/llama.cpp.git {github_dir}/llama.cpp
!git clone https://github.com/oobabooga/text-generation-webui.git {github_dir}/text-generation-webui
print("✅ دانلود ابزارهای گیت‌هاب تمام شد.")


# --- مرحله ۴: فشرده‌سازی همه چیز در یک فایل ---
print(f"\n⏳ شروع فشرده‌سازی کل پوشه در فایل {archive_name}...")
# این فرآیند ممکن است بسته به حجم کل فایل‌ها بسیار طولانی شود
!tar -czf {archive_path} -C {os.path.dirname(base_dir)} {os.path.basename(base_dir)}

print("\n🎉🎉🎉 عملیات با موفقیت تمام شد! 🎉🎉🎉")
print(f"فایل فشرده کامل در مسیر زیر در گوگل درایو شما ذخیره شد:\n{archive_path}")
