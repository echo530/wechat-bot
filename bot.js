const { WechatyBuilder } = require('wechaty')
const axios = require('axios')

const bot = WechatyBuilder.build()

bot.on('scan', (qrcode, status) => {
  console.log('扫码登录👇')
  require('qrcode-terminal').generate(qrcode)
})

bot.on('login', user => {
  console.log(`登录成功: ${user}`)
})

bot.on('message', async message => {
  const text = message.text()
  const room = message.room()

  if (room && text.includes('@AI')) {
    const cleanText = text.replace('@AI', '')

    try {
      const res = await axios.post('http://localhost:5000/chat', {
        msg: cleanText
      })

      await room.say(res.data.reply)
    } catch (e) {
      console.log(e)
    }
  }
})

bot.start()