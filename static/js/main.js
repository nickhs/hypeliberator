$(function() {
  tracks = new Tracks();
  infoWindow = new InfoWindow();
  searchBox = new SearchBox();
});

var InfoWindow = Backbone.View.extend({
  el: ".info",
  template: "#track-template",

  initialize: function() {
    tracks.on("change reset add remove", this.drawSongs, this);
    tracks.on("request", this.setStatusFetching, this);
  },

  drawSongs: function() {
    this.$el.empty();

    if (tracks.length === 0) {
      this.setStatus("Nothing there?");
      searchBox.clear();
      return;
    }

    tracks.each(function(item, idx) {
      var html = _.template($(this.template).html(), item.toJSON());
      this.$el.append(html);
    }.bind(this));
  },

  setStatusFetching: function() {
    this.setStatus("Fetching...");
  },

  setStatus: function(message) {
    this.$el.empty();
    this.$el.append("<p>" + message + "</p>");
  },

  reset: function() {
    var str = "Download all the songs you've hearted</p><p>Enter your Hype Machine username above</p>";
    this.setStatus(str);
  }
});

var SearchBox = Backbone.View.extend({
  el: "#username",

  events: {
    "keypress": "handleKeypress"
  },

  handleKeypress: function(e) {
    if (e.target.value === '')
      infoWindow.reset();

    else if (e.keyCode == 13)
      this.search(this.$el.val());
  },

  search: function(username) {
    var data = {username: username};
    tracks.fetch({data: data});
  },

  clear: function() {
    this.$el.val('');
  }
});

var Tracks = Backbone.Collection.extend({
  url: '/api/grab',

  parse: function(response) {
    return response.results;
  }
});
