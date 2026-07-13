"""
Создание QR-кода для опубликованной открытки.

1. Установите библиотеку:
   pip install qrcode[pil]

2. Запустите:
   python generate_qr.py https://ваша-ссылка-на-сайт.ru
"""
import sys
from pathlib import Path

try:
    import qrcode
except ImportError:
    raise SystemExit("Сначала выполните: pip install qrcode[pil]")

if len(sys.argv) != 2:
    raise SystemExit("Использование: python generate_qr.py https://ваша-ссылка.ru")

url = sys.argv[1].strip()
if not (url.startswith("https://") or url.startswith("http://")):
    raise SystemExit("Ссылка должна начинаться с http:// или https://")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=14,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="#65152d", back_color="#fffafc")
output = Path("qr_postcard.png")
img.save(output)
print(f"Готово: {output.resolve()}")
