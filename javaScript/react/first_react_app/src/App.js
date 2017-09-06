import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = { count: 0 };
        this.onClickButton = this.onClickButton.bind(this);
    }

    onClickButton() {
        this.setState({ count: this.state.count + 1 });
    }


    render() {
        const counterStyle = {margin: '16px'};
        return (
            <div style={counterStyle}>
                <button onClick={this.onClickButton}>Click Me</button>
                <div>Click Me: {this.state.count}</div>
            </div>
        )
    }
}

export default App;