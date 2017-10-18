import React, { Component } from 'react';
import CounterStore from './stores/CounterStore.js';
import * as Actions from './Actions.js';


class Counter extends Component {
    constructor (props) {
        super(props);

        this.onChange = this.onChange.bind(this);
        this.onClickMinus = this.onClickMinus.bind(this);
        this.onClickPlus = this.onClickPlus.bind(this);

        this.state = {
            count: CounterStore.getCounterValues()[props.caption]
        }
    }

    onChange () {
        this.setState({
            count: CounterStore.getCounterValues()[this.props.caption]
        })
    }

    componentDidMount () {
        CounterStore.addChangedListener(this.onChange);
    }

    componentWillUnmount () {
        CounterStore.removeChangedListener(this.onChange);
    }

    onClickPlus () {
        Actions.increment(this.props.caption);
    }

    onClickMinus () {
        Actions.decrement(this.props.caption);
    }

    render () {
        return (
            <div>
                <button onClick={this.onClickPlus}>Plus</button>
                <button onClick={this.onClickMinus}>Minus</button>
                <span> {this.state.count} </span>
            </div>
        )
    }
}

export default Counter;
