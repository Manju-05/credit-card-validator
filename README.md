# 💳 Credit Card Validator

A smart and interactive Python script to check whether a credit card number is **valid** or **invalid**, and even detect its **card type** (like Visa, MasterCard, AmericanExpress, etc.) — using the industry-standard **Luhn algorithm**.

---

## ✨ Features

- 🧠 Uses the Luhn checksum formula for accurate validation  
- 🔍 **Detects card types** like Visa, MasterCard, American Express, Discover, and more  
- 🔄 Accepts numbers with or without spaces or dashes  
- 📦 No external libraries required — pure Python  

---

## ⚙️ How It Works

1. preprocess the card-number by removing any spaces or dashes  
2. Reverses the card number to process positions properly  
3. Adds digits at **odd positions** 
4. Doubles digits at **even positions** 
5. Sums everything and check if divisible by 10 and then validate
6. Detects the card type based on the starting digits and length

> ✅ If divisible by 10 → **Valid Card**  
> ❌ Otherwise → **Invalid Card**

---

## 🏷️ Card Type Detection

This tool can identify these major card types:

| Card Type        | Starts With           | Length |
|------------------|------------------------|--------|
| Visa             | 4                      | 13 or 16 |
| MasterCard       | 51–55                  | 16     |
| American Express | 34 or 37               | 15     |
| Discover         | 6011                   | 16     |
| JCB              | 35                     | 16     |
| Diners Club      | 36 or 38               | 14     |

---

## 🚀 Getting Started

1. Clone this repository:

```bash
git clone https://github.com/Manju-05/credit-card-validator.git
cd credit-card-validator

```
## 📌 Disclaimer
- This tool is intended for educational and testing purposes only.
- It does not verify real bank or credit card account status.

### Feel free to fork this project, improve it, and open pull requests 🚀
