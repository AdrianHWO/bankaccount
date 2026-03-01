# Simple Bank Account System 🏦

A lightweight Python implementation of a banking system demonstrating Object-Oriented Programming (OOP) principles, including encapsulation, static methods, and basic transaction logic.

## Features

* **Account Initialization**: Create accounts with an owner name and an initial balance.
* **Secure Deposits**: Validates deposit amounts before updating the balance.
* **Smart Withdrawals**: Prevents withdrawals that would fall below the required **Minimum Balance (100)**.
* **Static Validation**: Includes a utility to check if an interest rate is within a valid range (0-5%).
* **Readable Output**: Uses the `__str__` method for clean, formatted account summaries.

## How It Works

The system enforces a `MIN_BALANCE` rule. For example, if you have 500 in your account, you can only withdraw up to 400 to ensure the 100 minimum remains.

### Class Methods
* `deposit(amount)`: Adds funds to the account.
* `withdraw(amount)`: Deducts funds if the minimum balance is maintained.
* `is_valid_interest_rate(rate)`: A static utility method to validate percentage inputs.

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AdrinaHWO/bankaccount.git](https://github.com/AdrianHWO/bankaccount.git)
