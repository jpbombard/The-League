const Sequelize = require('sequelize')
const db = require('../database')

const Team = db.define('teams', {
    name: {
        type: Sequelize.STRING,
        allowNull: false
    },
    imageUrl: {
        type: Sequelize.STRING,
        defaultValue: ''
    },
    seasons: {
        type: Sequelize.INTEGER,
        validate: {
            min: 1,
            max: 12
        }
    }
})

module.exports = { Team }