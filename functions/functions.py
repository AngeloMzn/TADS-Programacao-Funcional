#Filter main data in array without a condition
def getMainData(data):
    return list(map(_grabMainData, data))

def _grabMainData(data):
    starred_at = data.get('starred_at')
    hireable = data.get('hireable')
    email = data.get('email')
    twitter_username = data.get('twitter_username')
    return [starred_at, hireable, email, twitter_username]


#Sort main data by date
def (mainData):
    sortedMainData = list(map())

def sortByDate(mainData):
