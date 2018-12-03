import sys


def sol():

    hevents = list()
    vevents = list()

    claims = sys.stdin.readlines()

    for claim in claims:
        
        formatted_claim = [x for x in claim.split(' ')]

        coords = formatted_claim[2].split(',')
        size = formatted_claim[3].split('x')

        claim_id = int(formatted_claim[0].replace('#', ''))

        x = int(coords[0])
        y = int(coords[1].replace(':', ''))
        width = int(size[0])
        height = int(size[1].replace('\n', ''))

        hevents.append((x, claim_id, -1))
        hevents.append((x + width, claim_id, 1))
        vevents.append((y, claim_id, -1))
        vevents.append((y + height, claim_id, 1))

    hevents.sort(key=lambda event : event[0])
    vevents.sort(key=lambda event : event[0])

    vactive = set()
    hactive = set()
    active = set()

    overlaps = 0

    h = 0

    for x in range(1000): 
        
        while h < len(hevents) and hevents[h][0] == x:

            if hevents[h][2] == -1:

                hactive.add(hevents[h][1])

            else:
 
                hactive.remove(hevents[h][1])

            h += 1

        v = 0

        for y in range(1000):
            
            while v < len(vevents) and vevents[v][0] == y:

                if vevents[v][2] == -1:

                    vactive.add(vevents[v][1])

                    if vevents[v][1] in hactive:

                        active.add(vevents[v][1])

                else:

                    vactive.remove(vevents[v][1])
                    
                    if vevents[v][1] in active:

                        active.remove(vevents[v][1])

                v+=1

            if len(active) > 1:

                overlaps += 1

    return overlaps


print(sol())
