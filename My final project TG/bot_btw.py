# Перед запуском Telegram-бота, потрібно обовязково встановити бібліотеку!! pip install python-telegram-bot --upgrade
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    CallbackQueryHandler, MessageHandler, filters
)
import random
import requests
import transliterate

# =========================
#  Налаштування
# =========================
BOT_TOKEN = "8064796302:AAGm10B85J4kwTCr1mCK7nz935Dj4zbmZYA"


# =========================
#  /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я оновлений бот 😊\n"
        "/help – команди\n"
        "/weather <місто>\n"
        "/game – міні гра з кнопками\n"
        "/quiz – вікторина"
    )

# =========================
#  /help
# =========================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Доступні команди:\n"
        "/weather <місто>\n"
        "/game\n"
        "/quiz\n"
    )

# =========================
#  /weather (виправлена версія)
# =========================
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("❗ Введи місто. Наприклад: /weather Київ")
        return

    city = " ".join(context.args)

    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url).json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        wind = current["windspeedKmph"]

        await update.message.reply_text(
            f"🌤 Погода в *{city}*:\n"
            f"Температура: {temp}°C\n"
            f"Опис: {desc}\n"
            f"Вітер: {wind} км/год",
            parse_mode="Markdown"
        )

    except Exception as e:
        await update.message.reply_text("⚠️ Не вдалося отримати погоду. Спробуй інше місто.")


# =========================
#  /game (нова міні гра)
# =========================
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 5)
    context.user_data["game_number"] = number

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data="g1"),
            InlineKeyboardButton("2", callback_data="g2"),
            InlineKeyboardButton("3", callback_data="g3"),
            InlineKeyboardButton("4", callback_data="g4"),
            InlineKeyboardButton("5", callback_data="g5"),
        ]
    ]

    await update.message.reply_text(
        "🎮 Я загадав число від 1 до 5. Вгадай!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Обробка натиснень кнопок для гри
async def game_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_choice = int(query.data[1])
    correct = context.user_data.get("game_number")

    if user_choice == correct:
        await query.edit_message_text(f"🎉 Ти вгадав! Це було число {correct}")
    else:
        await query.edit_message_text(f"❌ Невірно. Правильне число: {correct}")

# =========================
#  /quiz (нова логіка)
# =========================

QUIZ_DATA = [
    ("Столиця Франції?", "париж"),
    ("Скільки буде 5*6?", "30"),
    ("Столиця Італії?", "рим"),
    ("Яка планета третя від сонця?", "земля"),
]

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question, answer = random.choice(QUIZ_DATA)

    context.user_data["quiz_answer"] = answer.lower()

    await update.message.reply_text(
        f"🧠 *Питання:*\n{question}\n\nВідповідай текстом.",
        parse_mode="Markdown"
    )

# Обробка текстових відповідей на вікторину
async def quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct_answer = context.user_data.get("quiz_answer")

    if not correct_answer:
        return  # користувач не в режимі вікторини

    user_ans = update.message.text.lower().strip()

    if user_ans == correct_answer:
        await update.message.reply_text("🎉 Правильно!")
    else:
        await update.message.reply_text(f"❌ Неправильно. Правильна відповідь: {correct_answer}")

    context.user_data["quiz_answer"] = None

# =========================
#  Запуск бота
# =========================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("game", game))
    app.add_handler(CommandHandler("quiz", quiz))

    app.add_handler(CallbackQueryHandler(game_button, pattern="g"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, quiz_answer))

    print("Бот запущений ✔")
    app.run_polling()

if __name__ == "__main__":
    main()
