# WhatsSched – Python-Based WhatsApp Message Scheduler

WhatsSched is a Python-based automation project that allows users to schedule WhatsApp messages for a specific time. Instead of manually sending a message, users can enter the recipient's phone number, the message content, and the desired sending time. The application uses **PyWhatKit** to interact with WhatsApp Web and automate the message-sending process.

## 🚀 Features

- **Schedule Messages:** Enter a preferred time to send a WhatsApp message.
- **Automatic Time Parsing:** Supports 12-hour time formats, such as `02:45 PM`.
- **Next-Day Scheduling:** Automatically schedules the message for the following day if the selected time has already passed.
- **Countdown Timer:** Displays the remaining time before the scheduled message is sent.
- **WhatsApp Web Integration:** Uses PyWhatKit to open WhatsApp Web and initiate message delivery.
- **Error Handling:** Handles invalid time formats and scheduling exceptions.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **PyWhatKit** – WhatsApp Web automation and message scheduling.
- **DateTime** – Date and time calculations.
- **Time** – Countdown and waiting operations.
- **Sys** – Program exit and error handling.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
https://github.com/tharun-mr/MessageMate.git
cd WhatsSched
```

### 2. Install the required library

```bash
python -m pip install pywhatkit
```

### 3. Run the application

```bash
python whatsapp_scheduler.py
```

### 4. Enter the required details

The program asks for:
1. Recipient's phone number, including the country code.
2. WhatsApp message content.
3. Scheduled sending time in `HH:MM AM/PM` format.

Make sure you are logged in to WhatsApp Web and that your computer has an active internet connection.

## 💡 How It Works

1. The application collects the recipient's phone number, message, and preferred sending time.
2. It converts the entered time into a Python datetime object.
3. It checks whether the selected time has already passed and adjusts the date if necessary.
4. It calculates the waiting period and invokes PyWhatKit to interact with WhatsApp Web.
5. WhatsApp Web opens and attempts to send the message.

## 🔮 Future Enhancements

- Graphical user interface using Tkinter.
- Support for multiple scheduled messages.
- Recurring messages and reminders.
- Message scheduling through a web dashboard.
- Logging and tracking of message-sending results.

## ⚠️ Limitations

- WhatsApp Web must be accessible, and the user must be logged in.
- The computer must remain powered on and connected to the internet while the program is running.
- Browser automation may fail if WhatsApp Web changes or requires additional verification.
- Message delivery is not guaranteed; successful execution should not be treated as proof that the recipient received the message.

## 🎯 Learning Outcomes

This project demonstrates practical use of Python functions, exception handling, date and time manipulation, loops, user input, and browser automation through an external library.

