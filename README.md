# E-Commerce Automation Testing

This repository contains a simple Selenium WebDriver script written in Python for automating a series of actions on an e-commerce demo store. The automation script executes a sequence of test cases from user login attempts to navigating the cart and checkout process.

## Quick Start

### Prerequisites

Before running the test script, ensure you have the following installed:
- Python 3
- pip
- Selenium WebDriver
- ChromeDriver (or another driver for your preferred browser)

### Installation

To set up the testing environment, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Ezz24/qa_yassir.git
```

2. Navigate to the repository directory:
```bash
cd qa_yassir.git
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Running the Tests

To run the automated tests, execute the script `demo_script.py`:

```bash
python demo_script.py
```

## Test Cases

The script includes the following test cases:

1. Invalid user login attempt.
2. New user registration.
3. Login with a newly registered user.
4. Adding an item to the shopping cart.
5. Updating item quantity in the shopping cart.
6. Proceeding to the checkout page.

## Future Enhancements

The current automation script is kept simple due to time constraints and workload. Future enhancements could include:

- Expanding the test cases to cover more features of the e-commerce platform.
- Implementing the Page Object Model (POM) design pattern for better code maintainability.
- Adding test case for placing an order to complete the end-to-end user journey.
- Integrating the test suite with a continuous integration (CI) system for automated test runs.
- Utilizing Docker for creating a consistent testing environment across different machines.
- Writing behavior-driven development (BDD) tests using Cucumber to describe test cases in natural language.

## Contributing

Contributions to enhance the automation script are welcome. Please feel free to fork the repository, make changes, and open a pull request with your improvements.
