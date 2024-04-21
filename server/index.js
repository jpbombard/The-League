const app = require('./app');
const { seed } = require('./database')

const init = async () => {
    try {
        await seed()
        const port = provess.env.PORT || 3000
        app.listen(port, () => console.log(`Listening on port ${port}`))
    } catch (error) {
        console.log(error)
    }
}

init()