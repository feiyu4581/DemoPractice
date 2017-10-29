import {createStore, combineReduces} from 'react-redux'

import {reducer as todoReducer} from './todos'

export default createStore(reducer, {})
