$(function() {
    'use strict';

    var Todo = Backbone.Model.extend({
        defaults: function() {
            return {
                choosed: false,
                done: false,
                name: '空内容',
                folder: false,
                order: todos.nextOrder(),
            };
        },

        initialize: function() {
            if (!this.get('name')) {
                this.set({name: this.defaults().name});
            }
        },

        toggle: function(choosed) {
            choosed = _.isUndefined(choosed)? !this.get('choosed') : choosed;
            this.set({choosed: choosed});
        },

        done: function(done) {
            done = _.isUndefined(done)? !this.get('done') : done;
            console.log(this.get('name'), done);
            this.save({done: done});
        },
    });

    var Folder = Backbone.Model.extend({
        defaults: function() {
            return {
                choosed: false,
                name: "空文件夹",
                order: folders.nextOrder(),
            };
        },

        initialize: function() {
            if (!this.get('name')) {
                this.set({name: this.defaults().name});
            }
        },

        toggle: function(choosed) {
            choosed = _.isUndefined(choosed)? !this.get('choosed') : choosed;
            this.save({choosed: choosed});
        },
    });

    var TodoCollection = Backbone.Collection.extend({
        model: Todo,
        localStorage: new Backbone.LocalStorage("todos"),

        comparator: function(todo) {
            return todo.get('order');
        },

        nextOrder: function() {
            if (!this.length) return 1;
            return this.last().get('order') + 1;
        },

        choosed: function(filter) {
            var draftTodos = this.filter(function(todo) { return !todo.get('done'); });
            var currentTodos = _.isUndefined(filter)? draftTodos : _.filter(draftTodos, filter);
            return _.filter(currentTodos, function(model) { return model.get('choosed'); });
        },

        done: function() {
            return this.filter(function(todo) {return todo.get('done'); });
        },

        remaining: function(filter) {
            var self = this,
                choosed = self.choosed(filter),
                draftTodos = this.filter(function(todo) { return !todo.get('done'); }),
                currentTodos = _.isUndefined(filter)? draftTodos : _.filter(draftTodos, filter);

            return _.filter(currentTodos, function(todo) {
                return !_.contains(choosed, todo);
            });
        },

        toggle: function(choosed, filter) {
            var currentTodos = _.isUndefined(filter)? this : this.filter(filter);
            _.each(currentTodos, function(todo) {
                todo.set({choosed: choosed});
            });
        }
    });

    var FolderCollection = Backbone.Collection.extend({
        "model": Folder,
        "localStorage": new Backbone.LocalStorage("folders"),

        comparator: function(todo) {
            return todo.get('order');
        },

        nextOrder: function() {
            if (!this.length) return 1;
            return this.last().get('order') + 1;
        },
        get_current: function() {
            if (!this.length) {
                folders.create({name: '收件箱', choosed: true});
            }

            return this.find(function(folder) { return folder.get('choosed');});
        },
        chooseFolder: function(model) {
            this.each(function(folder) { folder.toggle(false); });
            model.toggle(true);
        },
    });

    var todos = new TodoCollection(),
        folders = new FolderCollection();

    var TodoView = Backbone.View.extend({
        tagName: 'li',
        template: _.template($("#TodoList").html()),
        events: {
            "click .destroy": "destroyTodo",
            "click .toggle": "toggleChoose",
            "dblclick .todo-display > label": "toggleEdit",
            "blur .todo-edit": "blurEdit",
        },

        initialize: function() {
            this.listenTo(folders, 'change:choosed', this.choosedFolder);
            this.model.on('change:name', this.refreshName, this);
            this.model.on('change:choosed', this.refreshChoose, this);
            this.model.on('change:done', this.refreshDone, this);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            this.$display = this.$el.find('.todo-display');
            this.$edit = this.$el.find('.todo-edit');
            return this;
        },

        choosedFolder: function(model, value, options) {
            if (value) {
                if (!this.model.get('done') && this.model.get('folder') === model.id) {
                    this.$el.show();
                } else {
                    this.$el.hide();
                }
            }
        },

        destroyTodo: function() {
            this.model.destroy();
            this.$el.hide('fast');
        },

        toggleEdit: function() {
            this.$el.addClass('editable');
            this.$el.find('.todo-edit').focus().select();
        },

        blurEdit: function() {
            var val = this.$el.find('.todo-edit').val();
            if (val) {
                this.model.save({'name': val});
            }
            this.$el.removeClass('editable');
        },

        refreshName: function(model, value, options) {
            this.$el.find('.todo-display > label').text(value);
        },

        refreshChoose: function(model, value, options) {
            this.$el.find('.toggle').prop('checked', value);
        },

        toggleChoose: function() {
            this.model.toggle();
        },

        refreshDone: function(model, value, options) {
            if (!model.get('done') && !this.$el.parent().hasClass('todos-lists-done')) {
                this.$el.show('slow');
            }

            if (!model.get('done') && this.$el.parent().hasClass('todos-lists-done')) {
                this.$el.hide('slow');
            }

            if (model.get('done') && !this.$el.parent().hasClass('todos-lists-done')) {
                this.$el.hide('slow');
            }
        },
    });

    var FolderView = Backbone.View.extend({
        tagName: 'li',
        template: _.template($("#TodoFolder").html()),

        events: {
            "click": "toggleFolder",
        },

        initialize: function() {
            this.listenTo(this.model, 'change:choosed', this.render);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            if (this.model.get('choosed')) {
                this.$el.addClass('active');
            } else {
                this.$el.removeClass('active');
            }

            return this;
        },

        toggleFolder: function() {
            folders.chooseFolder(this.model);
        },

    });

    var AppView = Backbone.View.extend({
        el: '.todos-container',
        events: {
            "keypress .todos-input": "createTodo",
            "click .new-folder": "createNewFolder",
            "click .toggle-all": "toggleAll",
            "click .todo-confirm": "confirmChoose",
            "click .todo-done": "displayDone",
        },

        initialize: function() {
            this.$input = $('.todos-input');
            this.$lists = $('.todos-lists-container:first');
            this.$doneLists = $('.todos-lists-container:last');

            this.$folders = $('.todos-folds-container');
            this.$toggleAll = $('.toggle-all');
            this.$todoConfirm = $('.todo-confirm');
            this.$todoDone = $('.todo-done');

            this.listenTo(folders, 'add', this.addFolder);
            this.listenTo(todos, 'add', this.addTodo);
            this.listenTo(todos, 'change:choosed', this.refreshChoose);
            folders.fetch();
            todos.fetch();

            folders.chooseFolder(folders.get_current());

            this.displayDoneFlag = false;
        },

        createTodo: function(event) {
            if (event.keyCode != 13) return;
            if (!this.$input.val()) return;

            todos.create({'name': this.$input.val(), 'folder': folders.get_current().id});
            this.$input.val('');
        },

        createNewFolder: function(event) {
            var name = prompt("输入文件夹的名称");
            folders.create({'name': name});
        },

        addFolder: function(model, collection, options) {
            var folderView = new FolderView({model: model});
            this.$folders.append(folderView.render().el);
        },

        addTodo: function(model, collection, options) {
            var listView = new TodoView({model: model});
            this.$lists.prepend(listView.render().el);
        },

        displayDone: function() {
            var self = this;

            if (!this.displayDoneFlag) {
                this.displayDoneFlag = true;
                _.each(todos.done(), function(todo) {
                    var listView = new TodoView({model: todo});
                    self.$doneLists.append(listView.render().el);
                });
            } else {
                this.displayDoneFlag = false;
                self.$doneLists.empty();
            }
        },

        refreshChoose: function(model, value, options) {
            if (model.get('done')) {
                return model.done();
            }

            var choosed = todos.choosed(function(todo) {
                return todo.get('folder') === folders.get_current().id;
            });
            var remaining = todos.remaining(function(todo) {
                return todo.get('folder') === folders.get_current().id;
            });

            this.$toggleAll.prop('checked', remaining.length === 0? true : false);
            if (choosed.length > 0) {
                this.$todoConfirm.fadeIn('slow');
            } else {
                this.$todoConfirm.fadeOut('slow');
            }
        },

        toggleAll: function() {
            todos.toggle(this.$toggleAll.prop('checked'), function(todo) {
                return !todo.get('done') && todo.get('folder') === folders.get_current().id;
            });
        },

        confirmChoose: function() {
            var choosed = todos.choosed(function(todo) {
                return todo.get('folder') === folders.get_current().id;
            });

            _.each(choosed, function(todo) {
                todo.done();
            });
        },
    });

    var app = new AppView();
});
