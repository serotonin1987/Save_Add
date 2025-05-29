import aiohttp
import asyncio
import os
import json

# URL для получения массива постов
URL = "https://jsonplaceholder.typicode.com/posts"
FOLDER_NAME = "downloaded_posts"

# Создаём папку, если её нет
os.makedirs(FOLDER_NAME, exist_ok=True)

# Загружаем данные с сайта
async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

# Сохраняем каждый JSON-объект в файл
async def save_posts():
    async with aiohttp.ClientSession() as session:
        print("🔄 Загружаем данные...")
        data = await fetch_data(session, URL)
        
        for post in data:
            file_name = os.path.join(FOLDER_NAME, f"post_{post['id']}.json")
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(post, f, indent=4, ensure_ascii=False)
            print(f"✅ Сохранён: {file_name}")

# Запуск асинхронной задачи
if __name__ == "__main__":
    asyncio.run(save_posts())
