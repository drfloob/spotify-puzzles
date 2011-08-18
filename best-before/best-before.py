import sys

leapYears = [x for x in xrange(2000,2999) if (x % 4 == 0) or (x % 100 == 0 and x % 400 != 0)]
days30 = [4, 6, 9, 11]
days31 = [1, 3, 5, 7, 8, 10, 12]

def padYear(year):
    if year < 2000:
        year += 2000
    return str(year)

def padMD(md):
    if md < 10:
        return '0'+str(md)
    return str(md)

# returns int list of [y,m,d]
def bestDate(input):
    partsStr = input.strip().split('/')
    pts= sorted(map(int, partsStr), reverse=True)

    if pts[0] > 31:
        # pts[0] must be year
        year = pts[0]
        if pts[1] > 12:
            # pts[1] must be day
            date = [year, pts[2], pts[1]]
            if dateCheck(date):
                return date

        
        date = [year, pts[1], pts[2]]
        if dateCheck(date):
            return date
    
    if pts[1] > 12:
        # month must be the last entry
        date = [pts[1], pts[2], pts[0]]
        if dateCheck(date):
            return date
        date = [pts[0], pts[2], pts[1]]
        if dateCheck(date):
            return date

    return input
    

def dateCheck(arr):
    if arr[2] > 31:
        return False

    if arr[2] == 0:
        return False

    if arr[1] in days30:
        return arr[2] <= 30

    if arr[1] == 2:
        if arr[2] > 29:
            return False
        if arr[2] == 29:
            return arr[0] in leapYears
        return True

    return True


def formatDate(arr):
    if isinstance(arr, str):
        return arr+' is illegal'
    return '-'.join([padYear(arr[0]), padMD(arr[1]), padMD(arr[2])])


if __name__ == '__main__':
    for line in sys.stdin:
        print formatDate(bestDate(line))
