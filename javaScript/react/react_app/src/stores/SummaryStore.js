import AppDispatcher from '../AppDispatcher.js';
import * as ActionTypes from '../ActionTypes.js';
import CounterStore from './CounterStore.js';
import { EventEmitter } from 'events';

const CHANGE_EVENT = 'changed';

function computeSummary(counterValues) {
    let summary = 0;
    for (const key in counterValues) {
        if (counterValues.hasOwnProperty(key)) {
            summary += counterValues[key];
        }
    }

    return summary;
}

const SummaryStore = Object.assign({}, EventEmitter.prototype, {
    getSummaryValues () {
        return computeSummary(CounterStore.getCounterValues());
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

SummaryStore.dispatchToken = AppDispatcher.register((action) => {
    if (action.type === ActionTypes.INCREMENT || action.type === ActionTypes.DECREMENT) {
        AppDispatcher.waitFor([CounterStore.dispatchToken]);

        SummaryStore.emitChange();
    }
})


export default SummaryStore;
