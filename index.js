const EventEmitter = require('events')
const ieee754 = require('ieee754')
const net = require('net')
const urStateDef = require('./urStateDef.js')
const client = new net.Socket()

var currentState = {}

client.on('data', function (data) {
  for (var key in urStateDef) {
    currentState[key] = ieee754.read(data, urStateDef[key].start, false, 52, urStateDef[key].length)
  }
})

class URState extends EventEmitter {
  constructor (PORT, HOST) {
    super()
    client.connect(PORT, HOST, () => { this.emit('connect') })
    client.on('data', () => { this.emit('data', currentState) })
    client.on('error', (exception) => { this.emit('exception', exception) })
    client.on('drain', () => { this.emit('drain') })
    client.on('timeout', () => { this.emit('timeout') })
    client.on('close', () => { this.emit('close') })
  }
}

module.exports = URState
