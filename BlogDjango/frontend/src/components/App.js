import React, { Component } from 'react';
import ReactDOM from 'react-dom';
class App extends Component{
    render()
    {
        return <h1>React App</h1>
    }
}
ReactDOM.render(<App />,document.getElementById('app'));//First half is for what are we trying to render, Second half looks for app id in index.html