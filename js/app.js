const express = require('express');

const app = express()

app.get('/', (req, res) => {console.log('Ive been hit by root!');
                            res.send('[node]Hello, World!\n')});

app.get('/wait', (req, res) => {
    setTimeout(function() {
        console.log("Ive been hit by wait!");
        res.send('[node]Hello World, 5 seconds later!\n');
    }, 5000);
});

app.listen(8111, () => console.log('I am listening on port 8111!'))
