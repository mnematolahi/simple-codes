# --- مرحله ۱: اتصال به درایو و ورود به حساب Hugging Face ---
from google.colab import drive
from google.colab import userdata
from huggingface_hub import login
import os

# اتصال به گوگل درایو
drive.mount('/content/drive')

# خواندن توکن از قسمت Secrets و ورود به حساب
try:
    hf_token = userdata.get('HF_TOKEN')
    login(token=hf_token)
    print("✅ با موفقیت به حساب Hugging Face وارد شدید.")
except Exception as e:
    print("⚠️ توکن Hugging Face در قسمت Secrets پیدا نشد. برای دانلود مدل‌های محدود، به آن نیاز خواهید داشت.")


# --- مرحله ۲: تنظیمات اصلی و لیست‌های به‌روز شده ---
base_dir = "/content/drive/MyDrive/AI_Offline_Toolkit_2025"
os.makedirs(base_dir, exist_ok=True)

# === لیست کتابخانه‌های PyPI (کامل و به‌روز شده) ===
python_libraries = list(set([
    # Core AI & Deep Learning
    "torch", "torchvision", "torchaudio", "tensorflow", "scikit-learn", 
    "pandas", "numpy", "matplotlib", "seaborn",
    # Hugging Face Ecosystem
    "transformers", "accelerate", "bitsandbytes", "datasets", "peft", 
    "huggingface_hub", "optimum", "auto-gptq", "awq",
    # LLM Inference, RAG & Serving
    "langchain", "langchain-community", "langchain-text-splitters", 
    "chromadb", "faiss-cpu", "sentence-transformers", "llama-cpp-python",
    "vllm", "fastapi", "uvicorn",
    # Data Handling & Utilities
    "PyMuPDF", "pdf2image", "PyYAML", "Pillow", "tqdm", "jupyter",
    # App & UI
    "streamlit", "streamlit-mermaid", "gradio",
    # Evaluation & Monitoring
    "lm-eval", "pynvml"
]))

# === لیست مدل‌های هوش مصنوعی (جدیدترین‌ها تا جولای ۲۰۲۵) ===
models_to_download = {
    # Qwen2 Models
    "qwen2-7b-instruct": "TheBloke/Qwen2-7B-Instruct-GGUF/qwen2-7b-instruct.Q5_K_M.gguf",
    "qwen2-72b-instruct": "TheBloke/Qwen2-72B-Instruct-GGUF/qwen2-72b-instruct.Q4_K_M.gguf",
    # Mistral Models
    "mixtral-8x22b-instruct": "TheBloke/Mixtral-8x22B-Instruct-v0.1-GGUF/mixtral-8x22b-instruct-v0.1.Q4_K_M.gguf",
    "codestral-22b": "TheBloke/Codestral-22B-v0.1-GGUF/codestral-22b-v0.1.Q5_K_M.gguf",
    # DeepSeek V2 Models
    "deepseek-v2-chat": "TheBloke/DeepSeek-V2-Chat-GGUF/deepseek-v2-chat.Q5_K_M.gguf",
    "deepseek-coder-v2": "TheBloke/DeepSeek-Coder-V2-GGUF/deepseek-coder-v2.Q5_K_M.gguf",
    # Gemma 2 Models
    "gemma-2-9b-it": "TheBloke/gemma-2-9b-it-GGUF/gemma-2-9b-it.Q5_K_M.gguf",
    "gemma-2-27b-it": "TheBloke/gemma-2-27b-it-GGUF/gemma-2-27b-it.Q4_K_M.gguf",
    # Cohere Model
    "command-r-plus": "TheBloke/Command-R-Plus-GGUF/command-r-plus.Q4_K_M.gguf"
}

# === لیست پروژه‌های GitHub ===
github_repos_to_clone = {
    "llama_cpp": "https://github.com/ggerganov/llama.cpp.git",
    "text_generation_webui": "https://github.com/oobabooga/text-generation-webui.git",
    "ollama": "https://github.com/ollama/ollama.git",
    "open_webui": "https://github.com/open-webui/open-webui.git",
    # Circumvention Tools
    "v2ray_core": "https://github.com/v2ray/v2ray-core.git",
    "nekoray": "https://github.com/MatsuriDayo/nekoray.git",
    "proxychains_ng": "https://github.com/rofl0r/proxychains-ng.git",
    "tor": "https://github.com/torproject/tor.git",
    # Firewall Source
    "opnsense_core": "https://github.com/opnsense/core.git"
}


# --- مرحله ۳: ساخت پوشه‌ها و شروع دانلود ---
pypi_dir = os.path.join(base_dir, "PyPI_Libraries")
models_dir = os.path.join(base_dir, "AI_Models_GGUF")
github_dir = os.path.join(base_dir, "GitHub_Projects")

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
for name, path in models_to_download.items():
    try:
        parts = path.split('/')
        repo_id = f"{parts[0]}/{parts[1]}"
        filename = parts[2]
        print(f"--- در حال دانلود مدل: {name} ---")
        !huggingface-cli download {repo_id} {filename} --local-dir {models_dir}/{name} --local-dir-use-symlinks False
    except Exception as e:
        print(f"❌ خطایی در دانلود مدل {name} رخ داد: {e}")
print("✅ دانلود مدل‌های هوش مصنوعی تمام شد.")

# ۳. دانلود ابزارهای گیت‌هاب
print("\n⏳ شروع دانلود پروژه‌های گیت‌هاب...")
for name, url in github_repos_to_clone.items():
    try:
        target_path = os.path.join(github_dir, name)
        print(f"--- در حال کلون کردن پروژه: {name} ---")
        !git clone {url} {target_path}
    except Exception as e:
        print(f"❌ خطایی در کلون کردن پروژه {name} رخ داد: {e}")
print("✅ دانلود پروژه‌های گیت‌هاب تمام شد.")


# --- مرحله ۴: فشرده‌سازی (اختیاری) ---
# در صورت تمایل می‌توانید این بخش را از حالت کامنت خارج کنید تا کل پکیج فشرده شود
# print(f"\n⏳ شروع فشرده‌سازی کل پوشه...")
# archive_name = "AI_Offline_Toolkit_2025.tar.gz"
# archive_path = f"/content/drive/MyDrive/{archive_name}"
# !tar -czf {archive_path} -C {os.path.dirname(base_dir)} {os.path.basename(base_dir)}
# print(f"\n🎉🎉🎉 عملیات با موفقیت تمام شد و فایل فشرده در گوگل درایو شما ذخیره شد: {archive_path} 🎉🎉🎉")

print("\n🎉🎉🎉 تمام عملیات دانلود با موفقیت انجام شد. فایل‌ها در گوگل درایو شما ذخیره شدند. 🎉🎉🎉")
