# Playwright TypeScript UI Test Automation Demo

This project is a UI test automation demo using Playwright with TypeScript.  
It automates login validation scenarios on the SauceDemo web application using the Page Object Model design pattern.

## Project Objective

The objective of this project is to demonstrate practical UI test automation skills using Playwright, TypeScript, Page Object Model, and HTML reporting.

## Application Under Test

SauceDemo: https://www.saucedemo.com/

## Tools Used

- Playwright
- TypeScript
- Node.js
- Page Object Model
- HTML Test Report
- Git
- GitHub

## Automated Test Scenarios

### Successful Login Test

This test verifies that a user can log in with valid credentials.

Steps tested:

- Open SauceDemo login page
- Enter valid username
- Enter valid password
- Click login button
- Verify navigation to Products page

### Invalid Login Test

This test verifies that the application shows an error message for invalid credentials.

Steps tested:

- Open SauceDemo login page
- Enter invalid username
- Enter invalid password
- Click login button
- Verify login error message

### Product Page Validation

After successful login, the test verifies:

- Products page URL
- Products page title
- Inventory items are visible
- Shopping cart icon is visible

### Error Message Validation

After invalid login, the test verifies:

- Error message is visible
- Error message contains expected text

## Test Data

| Scenario | Username | Password |
|---|---|---|
| Valid Login | standard_user | secret_sauce |
| Invalid Login | wrong_user | wrong_password |

## Project Structure

```text
ui-test-automation-playwright
│
├── pages
│   ├── LoginPage.ts
│   └── ProductsPage.ts
│
├── tests
│   └── login.spec.ts
│
├── playwright-report
│   └── index.html
│
├── package.json
├── package-lock.json
├── playwright.config.ts
├── tsconfig.json
├── README.md
└── .gitignore
```

## Page Object Model

This project uses the Page Object Model design pattern.

The page object files are stored inside the `pages` folder:

- `LoginPage.ts`
- `ProductsPage.ts`

The test file is stored inside the `tests` folder:

- `login.spec.ts`

This structure keeps selectors, page actions, and test logic separated.  
It makes the automation code easier to read, maintain, and extend.

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/rohanr2906-byte/ui-test-automation-playwright.git
cd ui-test-automation-playwright
```

Install dependencies:

```bash
npm install
```

Install Playwright browsers:

```bash
npx playwright install
```

## Run Tests

Run all tests in headless mode:

```bash
npm test
```

Run tests with browser visible:

```bash
npm run test:headed
```

Run tests in debug mode:

```bash
npm run test:debug
```

Run tests using Playwright UI mode:

```bash
npm run test:ui
```

Open HTML report:

```bash
npm run report
```

## Test Execution Result

Current automated test result:

```text
2 passed
```

The two automated tests cover:

- Successful login and product page validation
- Invalid login and error message validation

## HTML Report

The Playwright HTML report is generated inside:

```text
playwright-report/index.html
```

This report shows:

- Test execution status
- Passed tests
- Failed tests, if any
- Execution time
- Browser used for testing

## Project Outcome

This project demonstrates basic UI test automation using Playwright with TypeScript.  
It includes successful login validation, invalid login validation, product page validation, error message validation, Page Object Model structure, and HTML report generation.

## Future Improvements

- Add cart workflow automation
- Add checkout workflow automation
- Add cross-browser testing using Firefox and WebKit
- Add GitHub Actions for CI test execution