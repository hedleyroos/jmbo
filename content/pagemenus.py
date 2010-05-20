from pagemenu.pagemenus import PageMenu
from pagemenu.items import MostLikedItem, MostRecentItem, ThisWeekItem, ThisMonthItem

class ContentPageMenu(PageMenu):
    def __init__(self, queryset, request):
        self.items = [
            MostRecentItem(
                request=request,
                title="Most Recent",
                get={'name': 'by', 'value': 'most-recent'},
                default=True,
            ),
            MostLikedItem(
                request=request,
                title="Most Liked",
                get={'name': 'by', 'value': 'most-liked'},
                default=False,
            ),
            ThisWeekItem(
                request=request,
                title="This Week",
                get={'name': 'for', 'value': 'this-week'},
                default=False,
            ),
            ThisMonthItem(
                request=request,
                title="This Month",
                get={'name': 'for', 'value': 'this-month'},
                default=False,
            )
        ]
        super(ContentPageMenu, self).__init__(queryset, request)
