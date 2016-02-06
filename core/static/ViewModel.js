;
function ViewModel() {
    var self = this;
    var dateObject = new Date(1900, 12, 1);
    var date = dateObject.toISOString().split("T")[0];
    self.date = ko.observable(date);
    self.books = ko.observableArray();

    self.getBooks = function () {
        var year = self.date().split("-")[0];
        self.books.removeAll();
        $.get("/core/books_year/"+encodeURIComponent(year)).then(function (resp) {
            resp = JSON.parse(resp)
            console.log(resp);
            var book;
            for (var i = 0; i < resp.length; i++) {
                book = new Book(resp[i].pk, resp[i].fields.title);
                self.books.push(book);
            }
        }).always();
    }
}