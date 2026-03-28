# Binance Trading Bot 🚀

## 📌 Overview

This project is a Python-based trading bot that interacts with Binance API to place and manage orders.

## ⚙️ Features

* Connects to Binance API
* Places buy/sell orders
* Logging and validation system
* Configurable using YAML

## 📂 Project Structure

```
trading_bot/
│── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
│── cli.py
│── config.yaml
│── Dockerfile
│── README.md
```

## ▶️ Run Locally

```
python cli.py
```

## 🔐 Environment Variables

Create a `.env` file:

```
API_KEY=your_key
API_SECRET=your_secret
```

## 🐳 Docker Usage

```
docker build -t trading-bot .
docker run trading-bot
```

## 📊 Notes

* This bot is for educational purposes
* Use testnet before real trading


