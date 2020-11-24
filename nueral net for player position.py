# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:46:15 2020

@author: Charlie
"""
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

def load_dataset(tournament):
    matches, events = {}, {}
    matches = json.load(open('./epldata/matches/matches_{}.json'.format(tournament)))
    events = json.load(open('./epldata/events/events_{}.json'.format(tournament)))
    players = json.load(open('./epldata/players.json'))
    competitions = json.load(open('./epldata/competitions.json'))
    teams = json.load(open('./epldata/teams.json'))
    return matches, events, players, competitions, teams

def get_match(matches, events):
    match_id2events = defaultdict(list)
    match_id2match = defaultdict(dict)
    for event in events:
        match_id = event['matchId']
        match_id2events[match_id].append(event)
                                         
    for match in matches:
        match_id = match['wyId']
        match_id2match[match_id] = match

def get_player(players):
    player_id2player = defaultdict(dict)
    for player in players:
        player_id = player['wyId']
        player_id2player[player_id] = player
    return player_id2player

def get_competitions(competitions):
    competition_id2competition = defaultdict(dict)
    for competition in competitions:
        competition_id = competition['wyId']
        competition_id2competition[competition_id] = competition
    return competition_id2competition

def get_teams(teams):
    team_id2team = defaultdict(dict)
    for team in teams:
        team_id = team['wyId']
        team_id2team[team_id] = team
    return team_id2team

matches, events, players, competitions, teams = load_dataset('England')


def id_finder(lastname, players):
    players=(pd.DataFrame(players))
    for i in range(len(players)):
        if players['lastName'][i] == lastname:
            return players['wyId'][i]
        
def event_assigner(iden,events):
    subevents=[]
    for j in range(len(events)):
        if events[j]['playerId'] == iden:
            subevents.append(events[j]['subEventName'])
            
    subevents = sorted(subevents)
    return subevents

def y_axis_position_events(iden,events):
    y_events=[]
    for j in range(len(events)):
        if events[j]['playerId'] == iden:
            y_events.append(events[j]['positions'][0]['y'])
            
    return y_events

def x_axis_position_events(iden,events):
    x_events=[]
    for j in range(len(events)):
        if events[j]['playerId'] == iden:
            x_events.append(events[j]['positions'][0]['x'])
            
    return x_events

'''attempt to do a one layer neural net, breaking a football pitch into
a 3x3 grid'''

#take in all players events, store each event position

'''iden = id_finder('Ryan', players)
y_axis_position_events = y_axis_position_events(iden, events)
x_axis_position_events = x_axis_position_events(iden, events)
print(x_axis_position_events)
'''
def x_axis_neural_net(lastname, players, events):
    iden = id_finder(lastname, players)
    x_events = x_axis_position_events(iden,events)
    feature1_1_10 = np.empty(len(x_events))
    feature2_11_20 = np.empty(len(x_events))
    feature3_21_30 = np.empty(len(x_events))
    feature4_31_40 = np.empty(len(x_events))
    feature5_41_50 = np.empty(len(x_events))
    feature6_51_60 = np.empty(len(x_events))
    feature7_61_70 = np.empty(len(x_events))
    feature8_71_80 = np.empty(len(x_events))
    feature9_81_90 = np.empty(len(x_events))
    feature10_91_100 = np.empty(len(x_events))
    #will need 10 independant for loops
    #firstly for x values between 0 n ten
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature1_1_10[i] = x_events[i]+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature1_1_10[i] = (x_events[i]*0.67)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature1_1_10[i] = (x_events[i]*0.33)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature1_1_10[i] = (x_events[i]*0.17)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature1_1_10[i] = (x_events[i]*0.08)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature1_1_10[i] = (x_events[i]*0.04)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature1_1_10[i] = (x_events[i]*0.02)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature1_1_10[i] = (x_events[i]*0.01)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature1_1_10[i] = (x_events[i]*0.005)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature1_1_10[i] = (x_events[i]*0.0025)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature2_11_20[i] = (x_events[i]*0.67)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature2_11_20[i] = (x_events[i])+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature2_11_20[i] = (x_events[i]*0.67)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature2_11_20[i] = (x_events[i]*0.33)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature2_11_20[i] = (x_events[i]*0.17)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature2_11_20[i] = (x_events[i]*0.08)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature2_11_20[i] = (x_events[i]*0.04)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature2_11_20[i] = (x_events[i]*0.02)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature2_11_20[i] = (x_events[i]*0.01)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature2_11_20[i] = (x_events[i]*0.005)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature3_21_30[i] = (x_events[i]*0.33)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature3_21_30[i] = (x_events[i]*0.67)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature3_21_30[i] = (x_events[i])+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature3_21_30[i] = (x_events[i]*0.67)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature3_21_30[i] = (x_events[i]*0.33)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature3_21_30[i] = (x_events[i]*0.17)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature3_21_30[i] = (x_events[i]*0.08)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature3_21_30[i] = (x_events[i]*0.04)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature3_21_30[i] = (x_events[i]*0.02)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature3_21_30[i] = (x_events[i]*0.01)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature4_31_40[i] = (x_events[i]*0.17)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature4_31_40[i] = (x_events[i]*0.33)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature4_31_40[i] = (x_events[i]*0.67)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature4_31_40[i] = (x_events[i])+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature4_31_40[i] = (x_events[i]*0.67)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature4_31_40[i] = (x_events[i]*0.33)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature4_31_40[i] = (x_events[i]*0.17)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature4_31_40[i] = (x_events[i]*0.08)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature4_31_40[i] = (x_events[i]*0.04)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature4_31_40[i] = (x_events[i]*0.02)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature5_41_50[i] = (x_events[i]*0.08)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature5_41_50[i] = (x_events[i]*0.17)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature5_41_50[i] = (x_events[i]*0.33)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature5_41_50[i] = (x_events[i]*0.67)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature5_41_50[i] = (x_events[i])+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature5_41_50[i] = (x_events[i]*0.67)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature5_41_50[i] = (x_events[i]*0.33)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature5_41_50[i] = (x_events[i]*0.17)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature5_41_50[i] = (x_events[i]*0.08)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature5_41_50[i] = (x_events[i]*0.04)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature6_51_60[i] = (x_events[i]*0.04)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature6_51_60[i] = (x_events[i]*0.08)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature6_51_60[i] = (x_events[i]*0.17)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature6_51_60[i] = (x_events[i]*0.33)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature6_51_60[i] = (x_events[i]*0.67)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature6_51_60[i] = (x_events[i])+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature6_51_60[i] = (x_events[i]*0.67)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature6_51_60[i] = (x_events[i]*0.33)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature6_51_60[i] = (x_events[i]*0.17)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature6_51_60[i] = (x_events[i]*0.08)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature7_61_70[i] = (x_events[i]*0.02)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature7_61_70[i] = (x_events[i]*0.04)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature7_61_70[i] = (x_events[i]*0.08)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature7_61_70[i] = (x_events[i]*0.17)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature7_61_70[i] = (x_events[i]*0.33)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature7_61_70[i] = (x_events[i]*0.67)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature7_61_70[i] = (x_events[i])+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature7_61_70[i] = (x_events[i]*0.67)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature7_61_70[i] = (x_events[i]*0.33)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature7_61_70[i] = (x_events[i]*0.17)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature8_71_80[i] = (x_events[i]*0.01)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature8_71_80[i] = (x_events[i]*0.02)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature8_71_80[i] = (x_events[i]*0.04)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature8_71_80[i] = (x_events[i]*0.08)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature8_71_80[i] = (x_events[i]*0.17)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature8_71_80[i] = (x_events[i]*0.33)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature8_71_80[i] = (x_events[i]*0.67)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature8_71_80[i] = (x_events[i])+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature8_71_80[i] = (x_events[i]*0.67)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature8_71_80[i] = (x_events[i]*0.33)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature9_81_90[i] = (x_events[i]*0.005)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature9_81_90[i] = (x_events[i]*0.01)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature9_81_90[i] = (x_events[i]*0.02)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature9_81_90[i] = (x_events[i]*0.04)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature9_81_90[i] = (x_events[i]*0.08)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature9_81_90[i] = (x_events[i]*0.17)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature9_81_90[i] = (x_events[i]*0.33)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature9_81_90[i] = (x_events[i]*0.67)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature9_81_90[i] = (x_events[i])+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature9_81_90[i] = (x_events[i]*0.67)
            
    for i in range(len(x_events)):
        if x_events[i] < 11:
            feature10_91_100[i] = (x_events[i]*0.0025)+90 
        if x_events[i] < 21 and  x_events[i] >= 11:
            feature10_91_100[i] = (x_events[i]*0.005)+80 
        if x_events[i] < 31 and  x_events[i] >= 21:
            feature10_91_100[i] = (x_events[i]*0.01)+70
        if x_events[i] < 41 and  x_events[i] >= 31:
            feature10_91_100[i] = (x_events[i]*0.02)+60
        if x_events[i] < 51 and  x_events[i] >= 41:
            feature10_91_100[i] = (x_events[i]*0.04)+50
        if x_events[i] < 61 and  x_events[i] >= 51:
            feature10_91_100[i] = (x_events[i]*0.08)+40
        if x_events[i] < 71 and  x_events[i] >= 61:
            feature10_91_100[i] = (x_events[i]*0.17)+30
        if x_events[i] < 81 and  x_events[i] >= 71:
            feature10_91_100[i] = (x_events[i]*0.33)+20
        if x_events[i] < 91 and  x_events[i] >= 81:
            feature10_91_100[i] = (x_events[i]*0.67)+10
        if x_events[i] < 101 and  x_events[i] >= 91:
            feature10_91_100[i] = (x_events[i])
            
    A = sum(feature1_1_10)/(100*len(x_events))
    B = sum(feature2_11_20)/(100*len(x_events))
    C = sum(feature3_21_30)/(100*len(x_events))
    D = sum(feature4_31_40)/(100*len(x_events))
    E = sum(feature5_41_50)/(100*len(x_events))
    F = sum(feature6_51_60)/(100*len(x_events))
    G = sum(feature7_61_70)/(100*len(x_events))
    H = sum(feature8_71_80)/(100*len(x_events))
    I = sum(feature9_81_90)/(100*len(x_events))
    J = sum(feature10_91_100)/(100*len(x_events))
    
    mat = [A, B, C, D, E, F, G, H, I, J]
    
    defender_mat = np.empty(10)
    midfielder_mat = np.empty(10)
    forward_mat = np.empty(10)
    goalkeeper_mat = np.empty(10)
    
    if A > 0.9:
        goalkeeper_mat[0] = A
    if J > 0.9:
        goalkeeper_mat[1] = J
   
    
    if C > 0.57:
        midfielder_mat[2] = C
    if D > 0.57:
        midfielder_mat[3] = D
    if E > 0.57:
        midfielder_mat[4] = E
    if F > 0.57:
        midfielder_mat[5] = F
    if G > 0.57:
        midfielder_mat[6] = G
    if H > 0.57:
        midfielder_mat[7] = H
        
    if A > 0.23:
        defender_mat[0] = A*0.33
    if J > 0.23:
        defender_mat[9] = J*0.33
    if B > 0.9:
        defender_mat[1] = B
    if I > 0.9:
        defender_mat[8] = I
    if C > 0.9:
        defender_mat[2] = C
    if H > 0.9:
        defender_mat[7] = H
    if D > 0.57:
        defender_mat[3] = D*0.57
    if G > 0.57:
        defender_mat[6] = G*0.57
        
    if A > 0.23:
        forward_mat[0] = A*0.33
    if J > 0.23:
        forward_mat[9] = J*0.33
    if B > 0.9:
        forward_mat[1] = B
    if I > 0.9:
        forward_mat[8] = I
    if C > 0.9:
        forward_mat[2] = C
    if H > 0.9:
        forward_mat[7] = H
    if D > 0.57:
        forward_mat[3] = D*0.57
    if G > 0.57:
        forward_mat[6] = G*0.57
    if E > 0.57:
        forward_mat[4] = E*0.57
    if F > 0.57:
        forward_mat[5] = F*0.57
        
    defender = sum(defender_mat)/10
    midfielder = sum(midfielder_mat)/10
    goalkeeper = sum(goalkeeper_mat)/10
    forward = sum(forward_mat)/10
    
    return goalkeeper, defender, midfielder, forward, mat

print(x_axis_neural_net('Rice', players, events))
    
    
    
    
            
    
            
    
    
