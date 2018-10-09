const express = require('express');
const pg = require('pg-promise')();
const tableify = require('tableify');

const db = pg('postgres://roy:fielding@postgres:5432/arqsoft');

const app = express()
const noop = () => {};

app.get('/', (req, res) => {console.log('Ive been hit by root!');
                            res.send('[node]Hello, World!\n')});

app.get('/wait', (req, res) => {
    setTimeout(function() {
        console.log("Ive been hit by wait!");
        res.send('[node]Hello World, 5 seconds later!\n');
    }, 5000);
});

app.get('/intensive', (req, res) => {console.log('Ive been hit by intensive!');
    var startTime = Date.now();
    while ((Date.now() - startTime) < 5000) {
        noop();
    }
    res.send('[node]Intensive processing done!\n')});

app.use('/static', express.static('static'));

app.get('/db/movies/top', (req, res) => {
    db.any("select m.name as Movie, avg(r.rating) as Avg_Rating, count(*) as Reviews from movies m join ratings r on r.movie_id = m.id group by 1 having count(*) > 800 order by 2 desc limit 10")
        .then(function (data) {
            console.log("DATA:", data);
            res.send(tableify({t : data}));
        })
        .catch(function (error) {
            console.log("ERROR:", error);
            res.send(error);
        });
});

app.listen(8111, () => console.log('I am listening on port 8111!'))
