import random

class Hat():
    def __init__(self, **coller):
        self.contents = []
        inhat = dict(coller)
        lval = list(inhat.values())
        lkey = list(inhat.keys())
        i = 0
        for x in lval:
            i1 = 0
            while i1 < lval[i]:
                self.contents.append(lkey[i])
                i1+=+1
            i+=+1
        
    def draw(self, draw):
        i = 0
        self.new_list = []
        if draw > len(self.contents):
            draw = len(self.contents)
        # out of balls
        while i < draw:
            drawNumber = int(round(random.random()*len(self.contents),0))
            if drawNumber >= len(self.contents):
                drawNumber = (len(self.contents) - 1)
            self.new_list.append(self.contents[drawNumber])
            #self.contents.pop(drawNumber)
            i += +1 
        return self.new_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_right = 0
    i = 0
    expected_balls = dict(expected_balls)
    eval = list(expected_balls.values())
    ekey = list(expected_balls.keys())
    while i < num_experiments:
        balls_drawn = []
        i1 = 0
        #///// makes expected bals list /////
        for x in eval:
            i2 = 0
            while i2 < eval[i1]:
                balls_drawn.append(ekey[i1])
                i2+=+1
            i1+=+1
        i+=+1
        #//// check if all bals can be picked /////
        count = 0
        new_list = Hat.draw(hat, num_balls_drawn)
        
        for c in balls_drawn: 
            try:
                isin = (new_list.index(c))
                new_list.pop(isin)
                count+=+1
                
            except ValueError as v:
                new_list = []
                break
        if count == len(balls_drawn):
            times_right+=+1
    percentage_right = times_right / num_experiments
    return times_right , percentage_right
                
                
hat = Hat(blue=4, red=2, green=6)
hat3 = Hat(red=5, orange=4, black=1, blue=4, pink=2, striped=9, green=5)
x = experiment(
    hat=hat3,
    expected_balls={"blue": 2,
                    "green": 1},
    num_balls_drawn=6,
    num_experiments=20000)
print(x)