class hotelprice:
    __hotelPriceUrl = None
    __hotelPriceDetailUrl = None
    __hotelPrice = None
    __hotelPriceCurrency = None
    __hotelPriceSource = None
    __reateTime = None
    
    def __init__(self,hotelPriceUrl,hotelPriceDetailUrl,hotelPrice,hotelPriceCurrency,hotelPriceSource,reateTime):
        self.__hotelPriceUrl = hotelPriceUrl
        self.__hotelPriceDetailUrl = hotelPriceDetailUrl
        self.__hotelPrice = hotelPrice
        self.__hotelPriceCurrency = hotelPriceCurrency
        self.__hotelPriceSource = hotelPriceSource
        self.__reateTime=reateTime