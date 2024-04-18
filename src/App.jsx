import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://fantasy.espn.com/football/league?leagueId=48346" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/en/3/3b/TheLeagueintertitle.png" className="logo" alt="Vite logo" />
        </a>
      </div>
      <h1>The League</h1>
      <p>Data Visualizaiton</p>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the League logo to check out our league!
      </p>
    </>
  )
}

export default App
