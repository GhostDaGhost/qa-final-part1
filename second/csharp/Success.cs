using System;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public partial class LetsUseDataTestClass {
    private static IWebDriver driver = new ChromeDriver();

    [TestMethod]
    public void TestLetsUseData() {
        driver.Navigate().GoToUrl("https://letsusedata.com/index.html");
        driver.FindElement(By.Id("txtUser")).Click();
        driver.FindElement(By.Id("txtUser")).Clear();
        driver.FindElement(By.Id("txtUser")).SendKeys("test1");
        driver.FindElement(By.Id("txtPassword")).Click();
        driver.FindElement(By.Id("txtPassword")).Clear();
        driver.FindElement(By.Id("txtPassword")).SendKeys("Test12456");
        driver.FindElement(By.Id("javascriptLogin")).Click();
    }
}
