# File: thien_dao.py
import os
import sys
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Tải biến môi trường từ file .env
load_dotenv()

# Hỗ trợ in tiếng Việt chuẩn trên Windows console
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# Lấy token từ .env (hỗ trợ nhiều tên biến phổ biến)
TOKEN = os.getenv("DISCORD_TOKEN") or os.getenv("TOKEN") or os.getenv("BOT_TOKEN")

# Cấu hình Intents cơ bản (mặc định không yêu cầu quyền đặc biệt trên Developer Portal)
intents = discord.Intents.default()

# Khởi tạo Bot Discord
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    """Sự kiện kích hoạt khi Bot kết nối thành công tới Discord Gateway."""
    print("=" * 50)
    print("✅ Thiên Đạo đã giáng lâm - Kết nối Discord thành công!")
    if bot.user:
        print(f"🤖 Bot Name: {bot.user.name}")
        print(f"🆔 Bot ID: {bot.user.id}")
    print(f"📡 discord.py version: {discord.__version__}")
    print("=" * 50)


def main() -> None:
    """Khởi động Bot."""
    if not TOKEN or not TOKEN.strip():
        print("❌ LỖI: Chưa có Token Bot trong file .env!")
        print("👉 Hãy mở file .env và điền Token vào: DISCORD_TOKEN=your_token_here")
        return

    try:
        bot.run(TOKEN.strip())
    except discord.PrivilegedIntentsRequired:
        print("❌ LỖI PRIVILEGED INTENTS: Bot yêu cầu quyền đặc biệt chưa bật trên Developer Portal.")
        print("👉 Hãy vào https://discord.com/developers/applications/ -> chọn Bot -> bật các mục trong 'Privileged Gateway Intents'.")
    except discord.LoginFailure:
        print("❌ LỖI ĐĂNG NHẬP: Token không hợp lệ. Vui lòng kiểm tra lại file .env!")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi khởi chạy Bot: {e}")


if __name__ == "__main__":
    main()
