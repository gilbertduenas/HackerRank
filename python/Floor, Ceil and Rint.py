# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
        
    if pontoon_distance/you_speed < shark_distance/shark_speed:
        return 'Alive!'
    else:
        return 'Shark Bait!'