(function($) {
    $(function() {
        $.widget("zpd.paging", {
            options: {
                limit: 5,
                rowDisplayStyle: 'block',
                activePage: 0,
                rows: []
            },
            _create: function() {
                let rows = $("tbody", this.element).children();
                this.options.rows = rows;
                this.options.rowDisplayStyle = rows.css('display');
                let nav = this._getNavBar();
                this.element.after(nav);
                this.showPage(0);
            },
            _getNavBar: function() {
                let rows = this.options.rows;
                let nav = $('<div>', {class: 'paging-nav'});
                for (let i = 0; i < Math.ceil(rows.length / this.options.limit); i++) {
                    this._on($('<a>', {
                        href: '#',
                        text: (i + 1),
                        "data-page": (i)
                    }).appendTo(nav),
                            {click: "pageClickHandler"});
                }
                //create previous link
                this._on($('<a>', {
                    href: '#',
                    text: '<<',
                    "data-direction": -1
                }).prependTo(nav),
                        {click: "pageStepHandler"});
                //create next link
                this._on($('<a>', {
                    href: '#',
                    text: '>>',
                    "data-direction": +1
                }).appendTo(nav),
                        {click: "pageStepHandler"});
                return nav;
            },
            showPage: function(pageNum) {
                let num = pageNum * 1; //it has to be numeric
                this.options.activePage = num;
                let rows = this.options.rows;
                let limit = this.options.limit;
                for (let i = 0; i < rows.length; i++) {
                    if (i >= limit * num && i < limit * (num + 1)) {
                        $(rows[i]).css('display', this.options.rowDisplayStyle);
                    } else {
                        $(rows[i]).css('display', 'none');
                    }
                }
            },
            pageClickHandler: function(event) {
                event.preventDefault();
                $(event.target).siblings().attr('class', "");
                $(event.target).attr('class', "selected-page");
                let pageNum = $(event.target).attr('data-page');
                this.showPage(pageNum);
            },
            pageStepHandler: function(event) {
                event.preventDefault();
                //get the direction and ensure it's numeric
                let dir = $(event.target).attr('data-direction') * 1;
                let pageNum = this.options.activePage + dir;
                //if we're in limit, trigger the requested pages link
                if (pageNum >= 0 && pageNum < this.options.rows.length) {
                    $("a[data-page=" + pageNum + "]", $(event.target).parent()).click();
                }
            }
        });
    });
})(jQuery);



