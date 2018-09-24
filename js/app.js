const express = require('express');

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

app.listen(8111, () => console.log('I am listening on port 8111!'))
