const e = require('express')
const express = require('express')
const app = express()
const port = 5000
const mongoose = require('mongoose')


mongoose.connect('mongodb+srv://wonjong:retopia-486@cluster0.nhs9f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', {
    useNewUrlParser: true, useUnifiedTopology: true
}).then(() => console.log('MongoDB connected...'))
  .catch(err => console.log(err))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})