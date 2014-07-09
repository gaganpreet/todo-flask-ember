App = Ember.Application.create();

App.Router.map(function() {
  this.resource('todos', {'path': '/'});
});

App.Todo = DS.Model.extend({
  description: DS.attr('string'),
  isCompleted: DS.attr('boolean'),
  lastUpdate: DS.attr()
});

App.ApplicationAdapter = DS.RESTAdapter.extend({
  namespace: 'api'
});

App.TodosRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('todo');
  }
});

App.TodosController = Ember.ArrayController.extend({
  // Properties
  sortProperties: ['lastUpdate'],
  sortAscending: false,
  todosLeft: Ember.computed.filterBy('content', 'isCompleted', false),
  todosCompleted: Ember.computed.filterBy('content', 'isCompleted', true),

  // Actions
  actions: {
    addTodo: function() {
      var description = this.get('description');

      var o = {description: description, isCompleted: false, lastUpdate: new Date().getTime()/1000};
      var todo = this.store.createRecord('todo', o);

      this.set('description', '');

      todo.save();
    },

    markAllTodosComplete: function() {
      var todosLeft = this.get('todosLeft');
      for (var i = todosLeft.length - 1; i >= 0; --i) {
        var todo = todosLeft[todosLeft.length - 1];
        todo.set('isCompleted', true);
      }
    }
  }
});


App.TodoController = Ember.ObjectController.extend({
  isEditing: false,
  actions: {
    editTodo: function() {
      this.set('isEditing', true);
    },
    cancelEditing: function() {
      this.set('isEditing', false);
    },
    finishedEditing: function() {
      this.get('model').save();
      this.set('isEditing', false);
    },
    deleteTodo: function() {
      this.get('model').deleteRecord();
      this.get('model').save();
    }
  },
  previousIsCompleted: undefined,
  saveTodo: function() {
    /*
     * The previousIsCompleted is needed because of a bug I encouncted in Ember.js
     * handling of observes which happens when calling the this.get().save() function 
     * from this function, which in turn triggers the observe signal again,
     * in an infinite loop
     *
     * The previous variable doesn't allow the save method to be called again if the
     * value hasn't changed, stopping the possible infinite loop at the first
     * iteration itself
     *
     * Meta TODO: File a bug
     */
    var previousIsCompleted = this.get('previousIsCompleted');
    var currentState = this.get('isCompleted');
    this.set('previousIsCompleted', currentState);

    if (previousIsCompleted !== currentState) {
      this.get('model').save();
    }
  }.observes('isCompleted')
});
