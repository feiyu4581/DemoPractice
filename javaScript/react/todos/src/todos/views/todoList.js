import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import TodoItem from '/todoItem.js';

const TodoList = ({todos}) => {
    return (
        <ul>
        {
            todos.map(item => (
                <TodoItem 
                  key={item.id}
                  id={item.id}
                  text={item.text}
                  completed={item.completed}
                />
            ))
        }
        </ul>
    )
}

TodoList.PropTypes = {
    todos: PropTypes.array.isRequired
}

const mapStateToProps = (state) => {
    return {
        todos: state.todos
    }
}

export default connect(mapStateToProps)(TodoList);
