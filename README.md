# RAT
# Python Remote Access Tool (RAT)

A basic multi-client command and control server built with Python using `socket`, `threading`, and `colorama`. This tool allows you to remotely execute commands on connected clients from a terminal-based control panel.

> ⚠️ **Warning**  
> This project is intended for **educational purposes** and **authorized use only**. Unauthorized access to computers or networks is illegal and unethical.

---

## 🚀 Features

- Handle multiple client connections using threading.
- Broadcast commands to all clients or send to a specific client.
- Command response output is printed in real-time.
- Terminal title updates with active client count.
- ASCII art branding for visual flair.

---

## 🧠 How It Works

1. The server listens for incoming connections.
2. When a client connects, it's added to the list of active sessions.
3. The server admin can select individual clients or broadcast a command to all.
4. Each client sends the output of the command back to the server.
5. Disconnected clients are automatically removed.

---

## 🛠 Requirements

- Python 3.x
- `colorama` (install via pip)

```bash
pip install colorama


🛰️ Python RAT Client

This is the client component of the Python Remote Access Tool (RAT). Once executed, it connects to the server and listens for incoming commands, executing them locally and sending back the output.

> ⚠️ **Disclaimer**  
> This software is for **educational** and **authorized penetration testing** use only. Unauthorized deployment is illegal and unethical.

---

## 📌 Features

- Connects to the server using TCP sockets.
- Executes received shell commands and returns output.
- Special built-in commands like:
  - `getip`: Retrieves public IP address using ipify API.
  - `exit`: Terminates connection.
- Hides the console window on Windows (uses `ctypes`).

---

## 🛠 Requirements

- Python 3.x
- `requests` module

Install dependencies:

```bash
pip install requests
