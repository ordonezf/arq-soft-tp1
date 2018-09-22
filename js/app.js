const express = require('express');

const app = express()

app.get('/', (req, res) => {console.log('Ive been hit by root!');
                            res.send('Hello, World!')});

app.get('/wait', (req, res) => {
    setTimeout(function() {
        console.log("Ive been hit by wait!");
        res.send('Hello World, 5 seconds later!');
    }, 5000);
});

app.listen(8111, () => console.log('I am listening on port 8111!'))
