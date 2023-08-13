#!/usr/bin/env node

const request = require('request');

function printCharacters (charactersArray, index) {
  request(charactersArray[index], (res, err, body) => {
    console.log(JSON.parse(body).name);
    if (index === charactersArray.length - 1) { return (0); } else { printCharacters(charactersArray, index + 1); }
  });
}

function requestStarWarsAPI () {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (res, err, body) => {
    if (!err) { console.log(Error(err)); }

    printCharacters(JSON.parse(body).characters, 0);
  });
}

requestStarWarsAPI();
