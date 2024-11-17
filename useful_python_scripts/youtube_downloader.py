import yt_dlp
import os


def download_youtube_video(video_url, save_path):
    try:
        # Налаштування yt-dlp
        ydl_opts = {
            'format': 'best',  # Найкраща якість
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'progress_hooks': [lambda d: print(f'Завантажено: {d["_percent_str"]}' if d["status"] == "downloading" else "")],
        }

        # Отримання інформації про відео
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Отримання інформації про відео...")
            info = ydl.extract_info(video_url, download=False)
            
            print("\nІнформація про відео:")
            print(f"Назва: {info['title']}")
            print(f"Автор: {info['uploader']}")
            print(f"Тривалість: {info['duration'] // 60} хв {info['duration'] % 60} с")
            print(f"Якість: {info['resolution']}")
            
            print("\nПочинаю завантаження...")
            ydl.download([video_url])
            
        print(f"\nВідео успішно завантажено в {save_path}")

    except Exception as e:
        print(f"Сталася помилка: {str(e)}")
        print("Спробуйте використати інше відео або перевірте з'єднання з інтернетом.")


if __name__ == "__main__":
    # URL відео
    video_url = input("Введіть URL відео з YouTube: ").strip()
    if not video_url:
        video_url = "https://www.youtube.com/watch?v=b298ye_-ORQ"  

    # Шлях для збереження
    save_path = "/home/smiroshnychenko/GeneralPython"

    download_youtube_video(video_url, save_path)
