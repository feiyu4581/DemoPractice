import React, {Component, PropTypes} from 'react';
import {connect} from 'react-redux';
import {addTodo} from '../actions.js';


class AddTodo extends Component {
    constructor (props, context) {
        super(props, context);

        this.value = {
            value: ''
        };
    }

    onSbumit(ev) {
        ev.preventDefault();

        const inputValue = this.state.value;
        if (!inputValue.trim()) {
            return;
        }

        this.props.onAdd(inputValue);
        this.setState({'value': ''});
    }

    onInputChange(ev) {
        this.setState({
            value: ev.target.value
        })
    }

    render() {
        return (
            <div className='add-todo'>
                <form onSubmit={this.onSbumit}>
                    <input className='new-todo' onChange={this.onInputChange} value={this.state.value} />
                    <button className='add-btn' type='submit' >
                        Add
                    </button>
                </form>
            </div>
        )
    }
}

AddTodo.propTypes = {
    onAdd: PropTypes.func.isRequired
}

const mapDispatchToProps = (dispatch) => {
    return {
        onAdd: (text) => {
            dispatch(addTodo(text));
        }
    }
}

export default connect(null, mapDispatchToProps)(AddTodo);
