#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  const promises = characters.map((url) => new Promise((resolve, reject) => {
    request(url, (err, res, charBody) => {
      if (err) reject(err);
      else resolve(JSON.parse(charBody).name);
    });
  }));

  Promise.all(promises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((err) => console.error('Error fetching character names:', err));
});
