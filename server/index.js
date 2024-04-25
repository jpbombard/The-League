import app from './app.js'
import obj from './database/index.js'
const { seed } = obj

const init = async () => {
    try {
        await seed()
        const port = process.env.PORT || 3000
        app.listen(port, () => console.log(`Listening on port ${port}`))
    } catch (error) {
        console.log(error)
    }
}

init()