import datetime;
class date:
    __FLAG_BOOKING_YEAR_MONTH = "YEAR-MONTH";
    __FLAG_BOOKING_DAY = "DAY";

    # def getMMTStartDate(self):
    #     now = datetime.date.today().timedelta(days=2).strftime("%m-%d-%Y")
    #     return now

    # def getMMTEndDate(self):
    #     now = datetime.date.today().timedelta(days=4).strftime("%m-%d-%Y")
    #     return now

    # def getGoibiboEndDate(self):
    #     now = datetime.date.today().timedelta(days=8).strftime("%m-%d-%Y")
    #     return now

    # def getGoibiboStartDate(self):
    #     now = datetime.date.today().timedelta(days=7).strftime("%m-%d-%Y")
    #     return now
    
    def getExpediaStartDate(self):
        now = (datetime.date.today().strftime("%d/%m/%Y"))
        return now

    def getExpediaEndDate(self):
        now = (date.today() + timedelta(days=1)).strftime("%m-%d-%Y")
        return now