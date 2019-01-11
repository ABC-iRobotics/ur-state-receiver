'use strict'

const EventEmitter = require('events')
const ieee754 = require('ieee754')
const net = require('net')
const urStateDef = require('./urStateDef.js')

var currentState = {}
var retrying = false
const timeOut = 5000

class URState extends EventEmitter {
  constructor (PORT, HOST) {
    super()
    this.client = new net.Socket()
    this.client.connect(
      PORT,
      HOST,
      () => {
        retrying = false
        this.emit('connect')
      }
    )

    this.client.on('data', function (data) {
      for (var key in urStateDef) {
        currentState[key] = ieee754.read(
          data,
          urStateDef[key].start,
          false,
          52,
          urStateDef[key].length
        )
      }
    })

    this.client.on('data', () => {
      this.emit('data', currentState)
    })
    this.client.on('connec', () => {
      console.log('oneconnection')
      this.emit('connect')
    })
    this.client.on('error', exception => {
      console.log('exception: ', exception)
      this.emit('exception', exception)
    })
    this.client.on('drain', () => {
      this.emit('drain')
    })
    this.client.on('timeout', () => {
      this.emit('timeout')
    })
    this.client.on('close', () => {
      if (!retrying) {
        retrying = true
        console.log('Reconnecting...')
      }
      setTimeout(() => {
        this.client.connect(
          PORT,
          HOST
        )
      }, timeOut)
      this.emit('close')
    })
  }
}

module.exports = URState
