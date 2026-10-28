
import pywhatkit as pwk
import datetime
import sys

def parse_time_input(time_str):
    try:
        send_time = datetime.datetime.strptime(time_str, "%I:%M %p")
        now = datetime.datetime.now()

        send_time = now.replace(
            hour=send_time.hour,
            minute=send_time.minute,
            second=0,
            microsecond=0
        )

        # Schedule for tomorrow if today's time has passed
        if send_time <= now:
            send_time += datetime.timedelta(days=1)

        return send_time

    except ValueError:
        print("Invalid time! Example: 02:45 PM")
        sys.exit(1)


def send_whatsapp_message(phone_number, message, send_time):
    try:
        now = datetime.datetime.now()
        delay = (send_time - now).total_seconds()

        # Wait until shortly before the scheduled time
        if delay > 60:
            print(f"Message scheduled for {send_time:%d-%m-%Y %I:%M %p}")
            import time
            time.sleep(delay - 30)

        # Recalculate the time after waiting
        now = datetime.datetime.now()
        if now.date() != send_time.date():
            send_time = now.replace(
                hour=send_time.hour,
                minute=send_time.minute,
                second=0,
                microsecond=0
            )

        # Give pywhatkit a future minute to send the message
        target = datetime.datetime.now() + datetime.timedelta(minutes=2)

        print("Opening WhatsApp Web...")
        pwk.sendwhatmsg(
            phone_number,
            message,
            target.hour,
            target.minute,
            wait_time=20,
            tab_close=False
        )

        print("WhatsApp message scheduling process completed.")

    except Exception as e:
        print(f"Failed to send message: {e}")


if __name__ == "__main__":
    phone_number = input(
        "Enter phone number with country code (e.g., +919876543210): "
    ).strip()

    message = input("Enter your message: ").strip()
    time_input = input("Enter sending time (e.g., 02:45 PM): ").strip()

    if not phone_number or not message:
        print("Phone number and message cannot be empty.")
        sys.exit(1)

    send_time = parse_time_input(time_input)
    send_whatsapp_message(phone_number, message, send_time)
