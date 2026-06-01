import { test } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { ProductsPage } from '../pages/ProductsPage';

test.describe('SauceDemo Login Tests', () => {
  test('successful login test and product page validation', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const productsPage = new ProductsPage(page);

    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');

    await productsPage.expectProductsPageLoaded();
  });

  test('invalid login test and error message validation', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.login('wrong_user', 'wrong_password');

    await loginPage.expectInvalidLoginError();
  });
});