from rx import Observable, Observer

source1 = Observable.interval(1000).map(lambda i: "Source 1: {}".format(i))
source2 = Observable.interval(1000).map(lambda i: "Source 2: {}".format(i))
source3 = Observable.interval(1000).map(lambda i: "Source 3: {}".format(i))


list = [source1, source2, source3]

Observable.from_(list)\
    .merge_all()\
    .subscribe(lambda s:print(s))

input("Press ctrl+c to stop.\n")
