import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Counter from './Counter.js'
import Summary from './Summary.js'

class App extends Component {
    render() {
        return (
            <div>
                <Counter caption='First' />
                <Counter caption='Second' />
                <Counter caption='Third' />

                <Summary />
            </div>
        )
    }
}

export default App;
