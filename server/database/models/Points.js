const db = require('../database')
const { INTEGER } = db.Sequelize

const Points = db.define('points', {
    seasonOne: {
        type: INTEGER,
        allowNull: true
    }
})