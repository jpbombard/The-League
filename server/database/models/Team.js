import db from '../database.js'
const { STRING, INTEGER } = db.Sequelize

const Team = db.define('teams', {
    name: {
        type: STRING,
        allowNull: false
    },
    imageUrl: {
        type: STRING,
        defaultValue: ''
    },
    seasons: {
        type: INTEGER,
        validate: {
            min: 1,
            max: 12
        }
    }
})

export default Team 