import re
from pyrogram import Client, filters, types
from pyrogram.enums import UserStatus
import datetime
from loguru import logger
import asyncio
import threading

api_id = 25115216
api_hash = 'bcb14ca55030e1d259d92f8de070240d'

# Глобальные переменные
session_name = "me_client"
me = 1499198721
chat_from = -1002022757177
chat_to = -1002294341866

# Глобальная переменная для отслеживания времени последнего сообщения
last_message_time = None

# Создаем единственный экземпляр клиента
app = Client(name=session_name, api_id=api_id, api_hash=api_hash)


@app.on_message(filters.chat(chat_from) | filters.chat(me))
async def my_handler(client: Client, message: types.Message):
    global last_message_time
    last_message_time = datetime.datetime.now()  # Обновляем время при получении нового сообщения

    if 'BURNED LP' not in message.text:
        return

    try:
        if message.from_user.id != me and message.message_thread_id != 6062:
            return
    except:
        return

    post_text = message.text
    top_5_match = re.search(r"Top 5:\s*([\d.]+)%", post_text)
    market_cap_match = re.search(r"Market Cap:\s*([\d.]+)k", post_text)
    mint_match = re.search(r"Mint:\s*([a-zA-Z0-9]+)", post_text)

    logger.info(f"{message.id} received")

    if not (top_5_match and market_cap_match and mint_match):
        return

    # Преобразовать извлеченные значения в числа
    top_5_percent = float(top_5_match.group(1))
    market_cap_k = float(market_cap_match.group(1))
    mint_address = mint_match.group(1)

    # Проверка условий
    if (
            5 <= top_5_percent <= 29 and
            25.0 <= market_cap_k <= 600.0 and
            mint_address.endswith("pump")
    ):
        logger.info(f"{message.id} forwarded")
        await client.forward_messages(chat_to, message.chat.id, message_ids=message.id)


async def restart_client():
    """Асинхронная функция для перезапуска клиента"""
    global app
    try:
        logger.warning("Restarting client...")
        await app.stop()  # Останавливаем текущий клиент (используем await)
        await asyncio.sleep(2)  # Добавляем небольшую задержку перед перезапуском
        await app.start()  # Запускаем клиента снова (используем await)
        logger.info("Client restarted successfully.")
    except Exception as e:
        logger.error(f"Error during client restart: {e}")


def check_inactivity():
    """Функция для проверки неактивности"""
    global last_message_time
    loop = asyncio.get_event_loop()  # Получаем event loop для выполнения асинхронных задач
    while True:
        if last_message_time:
            elapsed_time = (datetime.datetime.now() - last_message_time).total_seconds()
            if elapsed_time > 60:
                logger.warning("No messages for 60 seconds. Restarting client...")

                # Выполняем асинхронную функцию перезапуска через event loop
                loop.run_until_complete(restart_client())
        time.sleep(5)  # Проверяем каждые 5 секунд


@logger.catch
def main() -> None:
    """
    Функция запускает бота
    """
    logger.add(
        'logs.log',
        level='DEBUG',
        format="{time} {level} {message}",
        rotation='1 week',
        retention='1 week',
        compression='zip'
    )

    # Запускаем поток для проверки неактивности
    inactivity_thread = threading.Thread(target=check_inactivity, daemon=True)
    inactivity_thread.start()

    # Первичный запуск клиента
    app.run()


if name == 'main':
    main()