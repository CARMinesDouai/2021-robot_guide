const hostname = "localhost";
const port = 8081;  

var fs = require('fs');
const files = fs.readFileSync("index.html");

const express = require('express')
const app = express()
var publicDir = require('path').join(__dirname,'public'); 
app.use(express.static(publicDir)); 

app.get('/', (req, res) => {
  res.end(files);
})

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`)
})
