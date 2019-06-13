const request = require("request-promise");
//https://nodejs.org/dist/latest-v10.x/docs/api/fs.html
const fs = require("fs");
const cheerio = require('cheerio');

// const url = "https://sfbay.craigslist.org/sfc/";
const url = "https://sfbay.craigslist.org/d/software-qa-dba-etc/search/sfc/sof"

const scrapExample = {
    title: '',
    description: '',
    datePosted: new Date('2019-06-12'),
    url: '',
    address: '',
    compensation: ''
}

const scrapResults = [];

async function scrapeCraigslist() {

    try {
        const html = await request.get(url);
        fs.writeFileSync("./jobs.html", html);
        /** Scrapping */
        const $ = await cheerio.load(html);
        $('.result-info').each((index, element) => {
            const resultTitle = $(element).children('.result-title');
            const title = resultTitle.text();
            const url = resultTitle.attr("href");
            const scrapResult = { title, url};
            scrapResults.push(scrapResult);
        });

        console.log(scrapResults);
    } catch (err) {
        console.log(err);
    }

}

scrapeCraigslist();