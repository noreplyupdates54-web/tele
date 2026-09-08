import requests


def send_telegram_message(api_token: str, chat_id: str, message: str) -> None:
    """Sends a text message to a specified Telegram chat via the Bot API."""
    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        print("Notification sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")


if __name__ == "__main__":
    # Your credentials
    API_TOKEN = "6357773411:AAFp3itETAYfauYxgOqJp8M9xoSnGCx9UPY"
    CHAT_ID = "-1002009482520"

    # Test Message
    test_message = (
        "🚀 *Test Notification*\n\nYour Telegram bot is live and working!"
    )

    send_telegram_message(API_TOKEN, CHAT_ID, test_message)