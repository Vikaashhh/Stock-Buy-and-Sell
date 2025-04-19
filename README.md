# 📈 Day 7 - Stock Buy and Sell

This repository contains the solution for the classic **Stock Buy and Sell** problem, implemented in Python. This problem is part of the **#gfg160** challenge and **#geekstreak2025** initiative.

## 🚀 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You can buy and sell the stock multiple times to maximize your profit. However, you must **sell the stock before you buy again**.

Your task is to calculate the **maximum profit** you can achieve.

---

## 💡 Approach

We are allowed to perform multiple transactions. The main idea is to take **every increasing price sequence** and consider it a profitable transaction.

### ✅ Strategy:

- Traverse through the prices list.
- Compare the current day's price with the previous day's price.
- If the price is higher than the previous day, it means we can earn a profit.
- Add the difference to the total profit.

This greedy approach ensures we gain profit on every rise.

---
## 🔖 Tags
#gfg160 #geekstreak2025 #Day7 #Python #Greedy #DSA #StockBuySell
---
## 🤝 Connect
Follow my progress on LinkedIn or explore more DSA solutions on GitHub.
LinkedIn:- https://www.linkedin.com/in/vikaashhh/
