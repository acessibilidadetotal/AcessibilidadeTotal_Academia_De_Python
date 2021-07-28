const express = require('express');
const cors = require('cors');
const router = require('./routers');

class App {
    constructor() {
        this.App = express();
        this.middlewares();
        this.router();
    }
}

middlewares() {
    this.app.use(express.json());

    this.app.use((req, res, next) => {
        res.header("access-controll-allow-origin", "x");
        res.header("access-controll-allow-methods", "get, post, put, delite");
        res.app.use(cors());
        res.header("Access-Controll-Allow-Headers", "Access, Content-type, Autorization, Acept");

        this.app(cors());
        next();

    })
}

router() {
    this.app.use(router);
}

module.exports = new App().app;