import AppDispatcher from '../AppDispatcher.js';
import * as ActionTypes from '../ActionTypes.js';
import { EventEmitter } from 'events';

const counterValues = {
    'First': 0,
    'Second': 10,
    'Third': 20
}

const CHANGE_EVENT = 'changed';

const CounterStore = Object.assign({}, EventEmitter.prototype, {
    getCounterValues () {
        return counterValues;
    },

    emitChange () {
        this.emit(CHANGE_EVENT);
    },

    addChangedListener (callback) {
        this.on(CHANGE_EVENT, callback);
    },

    removeChangedListener (callback) {
        this.removeListener(CHANGE_EVENT, callback)
    }

});

CounterStore.dispatchToken = AppDispatcher.register((action) => {
    if (action.type === ActionTypes.INCREMENT) {
        counterValues[action.counterCaption] ++;
        CounterStore.emitChange();
    } else if (action.type === ActionTypes.DECREMENT) {
        counterValues[action.counterCaption] --;
        CounterStore.emitChange();
    }
})


export default CounterStore;
