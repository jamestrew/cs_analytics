import { BrowserRouter, Route } from 'react-router-dom'
import { User } from './components/User'

const Home = () => (
    <h1>WElcome to cS ANalYTics</h1>
)

export const App = () => (
    <BrowserRouter>
        <Route exact path="/" component={Home} />
        <Route path="/user/:xuid" component={User} />
    </BrowserRouter>
)

