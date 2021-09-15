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

app.post('/register', (req, res) => {
   // 회원가입 할 때 필요한 정보들을 client에서 가져오면, 
   // 그것들을 데이터 베이스에 넣어주는 기능이 포함된 route이다.
})
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})