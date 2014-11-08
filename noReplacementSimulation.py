#!/usr/local/bin/python2.7
    
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    matches = 0
    i = 0
    for i in range(numTrials):
        colors = ['R','R','R','G','G','G']
        ballsSet = set()
        for x in range(3):
            ball = random.choice(colors)
            colors.pop(colors.index(ball))
            ballsSet.add(ball)
        if len(ballsSet) == 1:
            matches += 1
    return matches/float(numTrials)
    
    
print "Number of Trials = {0} Percentage = {1}".format(10000,noReplacementSimulation(10000))