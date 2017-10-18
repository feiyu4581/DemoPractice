import React, { Component } from 'react';
import SummaryStore from './stores/SummaryStore.js'


class Summary extends Component {
    constructor (props) {
        super(props);

        this.onUpdate = this.onUpdate.bind(this);

        this.state = {
            summary: SummaryStore.getSummaryValues()
        }
    }

    componentDidMount () {
        SummaryStore.addChangedListener(this.onUpdate);
    }

    componentWillUnmount () {
        SummaryStore.removeChangedListener(this.onUpdate);
    }

    onUpdate () {
        this.setState({
            summary: SummaryStore.getSummaryValues()
        })
    }

    render () {
        return (
            <div>
                <span> All: {this.state.summary} </span>
            </div>
        )
    }
}

export default Summary;