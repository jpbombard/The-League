const db = require('./database')
const { Team } = require('./models/Team')

const teams = [{
    name: "Bosh",
    imageUrl: "https://s.yimg.com/cv/apiv2/default/nfl/20190724/500x500/2019_NYG.png",
    seasons: 12,
}, {
    name: 'Kellen and Tal',
    imageUrl: 'https://a.espncdn.com/i/headshots/nfl/players/full/14874.png',
    seasons: 12
}, {
    name: 'Nate and Jake',
    imageUrl: '',
    seasons: 12
}, {
    name: 'Sam',
    imageUrl: '',
    seasons: 12
}, {
    name: 'Sam',
    imageUrl: '',
    seasons: 12
}]

const seed = async () => {
    try {
        await db.sync({ force: true })

        const createdTeams = await Promise.all(teams.map(team => {
            return Team.create(team)
        }))

        console.log("Success!")
        db.close()
    } catch (error) {
        console.error("DID NOT WORk")
        console.error(error)
        db.close()
    }
}

module.exports = {
    seed,
    db,
    Team
}