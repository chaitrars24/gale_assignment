from pageObjects.SearchScreen import SearchScreen
from utilities.ReadConfig import ReadConfig


class Test_001_SearchFlights:
    travel_type = ReadConfig.getType()
    from_loc = ReadConfig.getFromLoc()
    to_loc = ReadConfig.getToLoc()
    depart_date = ReadConfig.getDepartDate()
    return_date = ReadConfig.getReturnDate()

    def test_searchFlight(self, setup):
        self.driver = setup
        # self.wait = setup
        self.search = SearchScreen(self.driver)
        self.search.click_roundTrip(self.travel_type)
        self.search.select_from_loc(self.from_loc)
        self.search.select_to_loc(self.to_loc)
        self.search.select_depart_date(self.depart_date)
        self.search.select_return_date(self.return_date)
        self.search.click_search_btn()
        self.search.verify_inputs(self.from_loc, self.to_loc)
        self.search.select_oneStop()
        self.search.select_flights()
        # self.search.click_book()

