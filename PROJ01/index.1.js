const request = require("request-promise");
//https://nodejs.org/dist/latest-v10.x/docs/api/fs.html
const fs = require("fs");
const cheerio = require('cheerio');


async function main() {

    const html = await request.get(
        "https://reactnativetutorial.net/css-selectors/lesson2.html"
    );

    fs.writeFileSync("./test.html", html);

    /** Scrapping */
    const $ = await cheerio.load(html);
    $("h2").each( (index, element) => {
        console.log($(element).text());
    });
}

main();