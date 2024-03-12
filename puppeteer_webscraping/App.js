const puppeteer = require("puppeteer");

(async()=>{
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto("https://ebravo.pk/classic/softwares");

    const getName = await page.evaluate(()=>{
        const nmTag = document.querySelectorAll(".info.col-sm-12.col-xs-7 div div div");
        let items = [];
        nmTag.forEach((tgs)=>{
            items.push(tgs.innerText);
        })
        return items;
    });
    console.log(getName);
    await browser.close();
})();