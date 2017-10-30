import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {toggleTodo, removeTodo} from '../actions.js'

const TodoItem = ({onToggle, onRemove, completed, text}) => {
    return (
        <li className='todo-item'>
            <input className='toggle' type='checkbox' checked={completed? "checked": ""} readOnly onClick={onToggle} />
            <label className="text">{text}</label>
            <button className="remove" onClick={onRemove}>x</button>
        </li>
    )
}

TodoItem.PropTypes = {
    onToggle: PropTypes.func.isRequred,
    onRemove: PropTypes.func.isRequred,
    completed: PropTypes.bool.isRequred,
    text: PropTypes.string.isRequred
}

const mapDispatchToProps = (dispatch, {id}) => {
    return {
        onToggle: () => dispatch(toggleTodo(id)),
        onRemove: () => dispatch(removeTodo(id))
    }
}

export default connect(null, mapDispatchToProps)(TodoItem);