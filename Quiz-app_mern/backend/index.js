// import { createRequire } from 'module';
// const require = createRequire(import.meta.url);

const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const userRoutes = require('./routes/users');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 9000;
let server;

// middleware config

app.use(cors());
app.use(bodyParser.urlencoded({extended: true, limit: '20mb'}));
app.use(bodyParser.json({limit: '20mb' }));

app.use('/api/users/', userRoutes);

mongoose.connect(process.env.DB_URL, {
    useUnifiedTopology: true,
    useNewUrlParser: true
}).then(()=>console.log('database connection established')).catch(er=>console.log('Error connecting to mongodb instance: ',er));

app.listen(PORT, ()=>{
    console.log('Node server running on port: ${PORT}');
});