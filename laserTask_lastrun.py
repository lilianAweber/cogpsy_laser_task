#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on Mon 12 Jun 2023 23:42:11 
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'SaveTheWorld'  # from the Builder filename that created this script
expInfo = {'participant': '000', 'session': '00', 'order': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/lil/projects/ccn/ContinuousValue/rotation/COGPSY/megTask/laserTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.sr_research.eyelink.EyeTracker'] = {
    'name': 'tracker',
    'model_name': 'EYELINK 1000 DESKTOP',
    'simulation_mode': False,
    'network_settings': '100.1.1.1',
    'default_native_data_file_name': 'EXPFILE',
    'runtime_settings': {
        'sampling_rate': 1000.0,
        'track_eyes': 'RIGHT_EYE',
        'sample_filtering': {
            'sample_filtering': 'FILTER_LEVEL_2',
            'elLiveFiltering': 'FILTER_LEVEL_OFF',
        },
        'vog_settings': {
            'pupil_measure_types': 'PUPIL_AREA',
            'tracking_mode': 'PUPIL_CR_TRACKING',
            'pupil_center_algorithm': 'ELLIPSE_FIT',
        }
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='SaveTheWorld', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "instructions_game"
instructions_gameClock = core.Clock()
# counters/setup
phaseN = 0
send_triggers = False

# import modules
import numpy as np
import os

# paths and filenames
# where sequences are stored
sequenceRoot = 'sequences/'
dataRoot = 'data/'
imageRoot = 'images/'
# retrieve the current session csv file
sessionFileName = (sequenceRoot + "cogpsy_main_v1_order" 
    + str(expInfo['order']) + "/session_s1_main_v1.csv")
practiceBlockFile = "practice_v1_block1.csv"
    
# initialise list containing data to be saved
saveData = [["phase","blockID","currentFrame","laserRotation",
    "shieldRotation","shieldDegrees","currentHit","totalReward",
    "sendTrigger","triggerValue","trueMean","trueVariance",
    "volatility","toneTrigger","toneVolatility","toneIndex","toneEndFrame"]];
saveFilename = (dataRoot + "sub-" + str(expInfo['participant']) + 
    "ses-" + str(expInfo['session']) + "_task-laser.csv")
    
# hide the mouse
win.mouseVisible = False

# keyboard constants
kb = keyboard.Keyboard()
keys_move = ['2', '1']
key_right = '2'
key_left = '1'

# set constants for the experiment
screen_refreshRate = win.getActualFrameRate()
ROTATION_SPEED = 1
CIRCLE_RADIUS = 3

# initialise variables that will be updated as experiment progresses
# shield variables
shieldDegrees = 40 #because it needs to be predefined
shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5
shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5

#calculate the screen X and Y locations that correspond to the shield centre
shieldX = np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1
shieldY = np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1
shieldX = np.concatenate(([0],shieldX))
shieldY = np.concatenate(([0],shieldY))
shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))

shieldRotation = 360; #begin at top

#reward variables
totalReward_tot = 0
lossFactor = 0.003
totalReward_text = ''

# reward bar variables
red_bar_length = 0
red_bar_length = 0
bar_length = 0.5
reward_change_colour = [1, -1, -1]
top_amount_text = ''
bottom_amount_text = ''
#lossFactor = 0.003

#progress circle variables
pc_orientation = 0;
pc_degrees = 0;
pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
pc_X = np.concatenate(([0],pc_X));
pc_Y = np.concatenate(([0],pc_Y));
pc_coords = np.transpose(np.vstack((pc_X,pc_Y)))

hgf = 0;

# triggers
triggers = dict(
    exp_start=100,
    exp_end=101,
    block_start=80,
    block_end=90,
    last_frame=99,
    laser_hit=10,
    laser_miss=20,
    key_right=30,
    key_left=40,
    key_release=50,
    tone_1=1,
    tone_2=2,
    begin_pract=60,
    begin_main=70
)

# Define function for sending triggers during the main trial loop
if send_triggers:
    def send_trigger(triggerValue):
        """
        code: expects an integer code (up to a maximum of 127, because of the serial port being weird)to send to the EEG)
        """
        # actual sending of trigger looks like this
        win.callOnFlip(trialTrigger.setData, int(triggerValue))
else:
    def send_trigger(code):
        print('sending trigger: ' + str(code))
        
# exp_start and _end triggers as well as block_start and _end
# triggers will be sent via their trigger components
expStartTrig = triggers['exp_start']
expEndTrig = triggers['exp_end']
blockStartTrig = triggers['block_start']
blockEndTrig = triggers['block_end']

title = visual.TextBox2(
     win, text='Save-the-world task', font='Open Sans',
     pos=(0, 0.35),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='title',
     autoLog=True,
)
text_instructions_1 = visual.TextStim(win=win, name='text_instructions_1',
    text='Welcome to the Save-the-world game!\n\nMysterious radioactive sources have just landed on Earth and are emitting radiation that is harmful to our planet.\n\nYour task is to catch the radiation beams with an absorbing shield. You will have to navigate the shield and position it wisely to minimise the damage caused by these sources. Help us save the world!\n\nPress any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_i1 = keyboard.Keyboard()

# Initialize components for Routine "practice_move"
practice_moveClock = core.Clock()
shield_move = visual.ShapeStim(
    win=win, name='shield_move', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, -0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
shield_centre_move = visual.ShapeStim(
    win=win, name='shield_centre_move', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
shield_bg_short_move = visual.ShapeStim(
    win=win, name='shield_bg_short_move', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, -0.5), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
radioactive_move = visual.ImageStim(
    win=win,
    name='radioactive_move', units='cm', 
    image='images/radioactive1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.5), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
text_move_s1 = visual.TextStim(win=win, name='text_move_s1',
    text='Your shield can be positioned anywhere on a circle around the harmful radiation source. To navigate the shield, use the "1" and "2" buttons on your response box. Try moving the shield now!',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_advance_move_s1 = visual.TextStim(win=win, name='text_advance_move_s1',
    text='If you have understood how to move the shield, \npress button "3" to advance to the next screen.',
    font='Open Sans',
    pos=(0, -0.25), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_move_s1 = keyboard.Keyboard()

# Initialize components for Routine "reward"
rewardClock = core.Clock()
text_reward = visual.TextStim(win=win, name='text_reward',
    text='In every block of this game, your reward for saving the world from this radiation starts off at £1. The more radiation you let through, the more reward you lose.\n\nTry to keep as much of that £1 as you can by catching as many beams as you can. After every block, you will receive feedback about how much reward you have earned in the previous block.\n\nEach block will last 3 minutes. A green circle will grow around the radioactive source, indicating how much time has passed. When the green circle is complete, the block is over.\n\nPress any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_reward = keyboard.Keyboard()

# Initialize components for Routine "instructions_practiceBlock"
instructions_practiceBlockClock = core.Clock()
text_practiceBlock = visual.TextStim(win=win, name='text_practiceBlock',
    text="You will now do a short practice block of the task. This block will only last 1 minute.\n\nAs in the real game, the source will emit radiation, but the main angle of attack might change over time, so that you have to keep monitoring the beams and decide when to re-position your shield.\n\nYou will see a reward bar on the right of the screen, which shows you how you lose money whenever a beam remains uncaught, but you will not actually earn any money during this practice. Remember to use the '1' and '2' buttons to navigate your shield.\n\nPress any key to start the practice block.",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_practiceBlock = keyboard.Keyboard()

# Initialize components for Routine "practiceBlock"
practiceBlockClock = core.Clock()
harmless_area_practice = visual.ShapeStim(
    win=win, name='harmless_area_practice',units='cm', 
    size=(6.6, 6.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-1.0, interpolate=True)
shield_practice = visual.ShapeStim(
    win=win, name='shield_practice', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
shield_centre_practice = visual.ShapeStim(
    win=win, name='shield_centre_practice', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
shield_bg_short_practice = visual.ShapeStim(
    win=win, name='shield_bg_short_practice', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
laser_practice = visual.ShapeStim(
    win=win, name='laser_practice', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-5.0, interpolate=True)
laser_long_practice = visual.ShapeStim(
    win=win, name='laser_long_practice', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.4]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-6.0, interpolate=True)
progress_bar_practice = visual.ShapeStim(
    win=win, name='progress_bar_practice', vertices=pc_coords,units='cm', 
    size=(0.3, 0.3),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='green', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
reward_bar_red = visual.Rect(
    win=win, name='reward_bar_red',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=[0,0], anchor='bottom-center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
reward_bar = visual.Rect(
    win=win, name='reward_bar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(0.6, -0.3), anchor='bottom-center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-9.0, interpolate=True)
radioactive_practice = visual.ImageStim(
    win=win,
    name='radioactive_practice', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
reward_text_top = visual.TextStim(win=win, name='reward_text_top',
    text='',
    font='Open Sans',
    pos=(0.6, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
reward_text_bottom = visual.TextStim(win=win, name='reward_text_bottom',
    text='',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "afterPractice"
afterPracticeClock = core.Clock()
after_practice_explanation = visual.TextStim(win=win, name='after_practice_explanation',
    text='Well done - this was the practice block!\n\nAs you have seen, the direction of the beams can jump around quickly, and you cannot catch all beams with your shield. That\'s ok - just try to catch as many as possible. The source will have a main direction of attack at any point - if you place your shield in that direction, you will catch most beams. \n\nMoving your shield also costs energy, which will be subtracted from your reward. It is thus important that you only move your shield when you think that the main direction of attack has changed. \n\nPress button "3" to continue.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_afterPractice = keyboard.Keyboard()

# Initialize components for Routine "instructions_mainTask"
instructions_mainTaskClock = core.Clock()
text_mainTask = visual.TextStim(win=win, name='text_mainTask',
    text="Are you ready to start the game?\n\nIn the actual game:\n\n1. You will not see the reward bar - but the rules for earning money remain the same, and you will receive feedback about your reward after every block.\n\n2. We ask you to please focus your eyes on the centre of the radioactive source and don't follow the beams with your eyes. This is to minimise eye-movement artefacts in the MEG data.\n\n3. You will hear tones through your headphones while you play the game. These tones are completely unrelated to the task - you can ignore them and focus on catching the beams.\n\nPress button 3 to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_mainTask = keyboard.Keyboard()

# Initialize components for Routine "radio_colours"
radio_coloursClock = core.Clock()
radioactive_colour1 = visual.ImageStim(
    win=win,
    name='radioactive_colour1', 
    image='images/radioactive3.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.2, 0.11), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
radioactive_colour2 = visual.ImageStim(
    win=win,
    name='radioactive_colour2', 
    image='images/radioactive2.png', mask=None, anchor='center',
    ori=0.0, pos=(0.2, 0.11), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_colours = visual.TextStim(win=win, name='text_colours',
    text="You will encounter two different radioactive sources:\nA red and a blue source.\n\n\n\n\n\n\n\nThe difference between these sources is how often they change their emission angle over time, and therefore how often you will have to adjust your shield position. One of the sources will change its main angle of attack more often, whereas the other will remain stable for longer.\n\nThis game has 4 blocks. You will encounter each of the two sources twice. \nPress button '3' to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_colours = keyboard.Keyboard()

# Initialize components for Routine "blockStartText"
blockStartTextClock = core.Clock()
radioactive_block_source = visual.ImageStim(
    win=win,
    name='radioactive_block_source', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_sourceImage = visual.TextStim(win=win, name='text_sourceImage',
    text="Please try to keep you eyes as fixed as possible on the centre of the screen.\n\nNew source ahead:\n\n\n\n\n\n\n\nPress any key if you're ready to start.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_blockStart = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
harmless_area = visual.ShapeStim(
    win=win, name='harmless_area',units='cm', 
    size=(6.6, 6.6), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0, 0, 0], fillColor=[0, 0, 0],
    opacity=None, depth=-1.0, interpolate=True)
shield = visual.ShapeStim(
    win=win, name='shield', vertices=shieldCoords,units='cm', 
    size=(1.1, 1.1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
shield_centre = visual.ShapeStim(
    win=win, name='shield_centre', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.2]],units='cm', 
    size=(1, 1),
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=3.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
shield_bg_short = visual.ShapeStim(
    win=win, name='shield_bg_short', vertices=shieldCoords,units='cm', 
    size=(1, 1),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
laser = visual.ShapeStim(
    win=win, name='laser', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.1]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-5.0, interpolate=True)
laser_long = visual.ShapeStim(
    win=win, name='laser_long', vertices=[[0, 0], [0, CIRCLE_RADIUS*1.4]],units='cm', 
    size=[1.0, 1.0],
    ori=1.0, pos=[0,0], anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=1.0, depth=-6.0, interpolate=True)
progress_bar = visual.ShapeStim(
    win=win, name='progress_bar', vertices=pc_coords,units='cm', 
    size=(0.3, 0.3),
    ori=1.0, pos=(0, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='green', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
radioactive = visual.ImageStim(
    win=win,
    name='radioactive', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "blockEndText"
blockEndTextClock = core.Clock()
textPause = visual.TextStim(win=win, name='textPause',
    text='Well done. In this block, you earned:\n\n\n\n\n\n\nTake a short break.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
textReward = visual.TextStim(win=win, name='textReward',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textContinue = visual.TextStim(win=win, name='textContinue',
    text='Press any key to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_blockEnd = keyboard.Keyboard()

# Initialize components for Routine "sessionEndText"
sessionEndTextClock = core.Clock()
textEndSession = visual.TextStim(win=win, name='textEndSession',
    text='Well done. You completed one session.\nIn this session, you made:\n\n\n\n\nTake a break. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
finalReward_text = visual.TextStim(win=win, name='finalReward_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions_game"-------
continueRoutine = True
# update component parameters for each repeat
title.reset()
key_resp_i1.keys = []
key_resp_i1.rt = []
_key_resp_i1_allKeys = []
# keep track of which components have finished
instructions_gameComponents = [title, text_instructions_1, key_resp_i1]
for thisComponent in instructions_gameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_gameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_game"-------
while continueRoutine:
    # get current time
    t = instructions_gameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_gameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *title* updates
    if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title.frameNStart = frameN  # exact frame index
        title.tStart = t  # local t and not account for scr refresh
        title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
        title.setAutoDraw(True)
    
    # *text_instructions_1* updates
    if text_instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions_1.frameNStart = frameN  # exact frame index
        text_instructions_1.tStart = t  # local t and not account for scr refresh
        text_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions_1, 'tStartRefresh')  # time at next scr refresh
        text_instructions_1.setAutoDraw(True)
    
    # *key_resp_i1* updates
    waitOnFlip = False
    if key_resp_i1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_i1.frameNStart = frameN  # exact frame index
        key_resp_i1.tStart = t  # local t and not account for scr refresh
        key_resp_i1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_i1, 'tStartRefresh')  # time at next scr refresh
        key_resp_i1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_i1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_i1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_i1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_i1.getKeys(keyList=None, waitRelease=False)
        _key_resp_i1_allKeys.extend(theseKeys)
        if len(_key_resp_i1_allKeys):
            key_resp_i1.keys = _key_resp_i1_allKeys[-1].name  # just the last key pressed
            key_resp_i1.rt = _key_resp_i1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_gameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_game"-------
for thisComponent in instructions_gameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('title.started', title.tStartRefresh)
thisExp.addData('title.stopped', title.tStopRefresh)
thisExp.addData('text_instructions_1.started', text_instructions_1.tStartRefresh)
thisExp.addData('text_instructions_1.stopped', text_instructions_1.tStopRefresh)
# check responses
if key_resp_i1.keys in ['', [], None]:  # No response was made
    key_resp_i1.keys = None
thisExp.addData('key_resp_i1.keys',key_resp_i1.keys)
if key_resp_i1.keys != None:  # we had a response
    thisExp.addData('key_resp_i1.rt', key_resp_i1.rt)
thisExp.addData('key_resp_i1.started', key_resp_i1.tStartRefresh)
thisExp.addData('key_resp_i1.stopped', key_resp_i1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_game" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_move"-------
continueRoutine = True
# update component parameters for each repeat
shieldRotation = 0; #begin at top
key_resp_move_s1.keys = []
key_resp_move_s1.rt = []
_key_resp_move_s1_allKeys = []
# keep track of which components have finished
practice_moveComponents = [shield_move, shield_centre_move, shield_bg_short_move, radioactive_move, text_move_s1, text_advance_move_s1, key_resp_move_s1]
for thisComponent in practice_moveComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_moveClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_move"-------
while continueRoutine:
    # get current time
    t = practice_moveClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_moveClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    #first, find out if L/R keys have been *released*
    LRkeys_released = kb.getKeys(keyList=keys_move,clear=True,waitRelease=True)
    if len(LRkeys_released)>0: #if so, then flush out the keys one final time
        LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=True,waitRelease=False)
    else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
        LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=False,waitRelease=False)
    
    #if key is pressed, rotate cursor
    #using most recently pressed key
    if len(LRkeys_pressed)>0:
        if LRkeys_pressed[-1]==key_right:
            shieldRotation += ROTATION_SPEED;
        if LRkeys_pressed[-1]==key_left:
            shieldRotation -= ROTATION_SPEED;
    
    # *shield_move* updates
    if shield_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_move.frameNStart = frameN  # exact frame index
        shield_move.tStart = t  # local t and not account for scr refresh
        shield_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_move, 'tStartRefresh')  # time at next scr refresh
        shield_move.setAutoDraw(True)
    if shield_move.status == STARTED:  # only update if drawing
        shield_move.setOri(shieldRotation, log=False)
    
    # *shield_centre_move* updates
    if shield_centre_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_centre_move.frameNStart = frameN  # exact frame index
        shield_centre_move.tStart = t  # local t and not account for scr refresh
        shield_centre_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_centre_move, 'tStartRefresh')  # time at next scr refresh
        shield_centre_move.setAutoDraw(True)
    if shield_centre_move.status == STARTED:  # only update if drawing
        shield_centre_move.setPos((0, -0.5), log=False)
        shield_centre_move.setOri(shieldRotation, log=False)
    
    # *shield_bg_short_move* updates
    if shield_bg_short_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        shield_bg_short_move.frameNStart = frameN  # exact frame index
        shield_bg_short_move.tStart = t  # local t and not account for scr refresh
        shield_bg_short_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_bg_short_move, 'tStartRefresh')  # time at next scr refresh
        shield_bg_short_move.setAutoDraw(True)
    if shield_bg_short_move.status == STARTED:  # only update if drawing
        shield_bg_short_move.setFillColor([0, 0, 0], log=False)
        shield_bg_short_move.setOri(shieldRotation, log=False)
        shield_bg_short_move.setVertices(shieldCoords, log=False)
        shield_bg_short_move.setLineColor([0, 0, 0], log=False)
    
    # *radioactive_move* updates
    if radioactive_move.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        radioactive_move.frameNStart = frameN  # exact frame index
        radioactive_move.tStart = t  # local t and not account for scr refresh
        radioactive_move.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radioactive_move, 'tStartRefresh')  # time at next scr refresh
        radioactive_move.setAutoDraw(True)
    
    # *text_move_s1* updates
    if text_move_s1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_move_s1.frameNStart = frameN  # exact frame index
        text_move_s1.tStart = t  # local t and not account for scr refresh
        text_move_s1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_move_s1, 'tStartRefresh')  # time at next scr refresh
        text_move_s1.setAutoDraw(True)
    
    # *text_advance_move_s1* updates
    if text_advance_move_s1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_advance_move_s1.frameNStart = frameN  # exact frame index
        text_advance_move_s1.tStart = t  # local t and not account for scr refresh
        text_advance_move_s1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_advance_move_s1, 'tStartRefresh')  # time at next scr refresh
        text_advance_move_s1.setAutoDraw(True)
    
    # *key_resp_move_s1* updates
    waitOnFlip = False
    if key_resp_move_s1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_move_s1.frameNStart = frameN  # exact frame index
        key_resp_move_s1.tStart = t  # local t and not account for scr refresh
        key_resp_move_s1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_move_s1, 'tStartRefresh')  # time at next scr refresh
        key_resp_move_s1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_move_s1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_move_s1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_move_s1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_move_s1.getKeys(keyList=['3'], waitRelease=False)
        _key_resp_move_s1_allKeys.extend(theseKeys)
        if len(_key_resp_move_s1_allKeys):
            key_resp_move_s1.keys = _key_resp_move_s1_allKeys[-1].name  # just the last key pressed
            key_resp_move_s1.rt = _key_resp_move_s1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_moveComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_move"-------
for thisComponent in practice_moveComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('shield_move.started', shield_move.tStartRefresh)
thisExp.addData('shield_move.stopped', shield_move.tStopRefresh)
thisExp.addData('shield_centre_move.started', shield_centre_move.tStartRefresh)
thisExp.addData('shield_centre_move.stopped', shield_centre_move.tStopRefresh)
thisExp.addData('shield_bg_short_move.started', shield_bg_short_move.tStartRefresh)
thisExp.addData('shield_bg_short_move.stopped', shield_bg_short_move.tStopRefresh)
thisExp.addData('radioactive_move.started', radioactive_move.tStartRefresh)
thisExp.addData('radioactive_move.stopped', radioactive_move.tStopRefresh)
thisExp.addData('text_move_s1.started', text_move_s1.tStartRefresh)
thisExp.addData('text_move_s1.stopped', text_move_s1.tStopRefresh)
thisExp.addData('text_advance_move_s1.started', text_advance_move_s1.tStartRefresh)
thisExp.addData('text_advance_move_s1.stopped', text_advance_move_s1.tStopRefresh)
# check responses
if key_resp_move_s1.keys in ['', [], None]:  # No response was made
    key_resp_move_s1.keys = None
thisExp.addData('key_resp_move_s1.keys',key_resp_move_s1.keys)
if key_resp_move_s1.keys != None:  # we had a response
    thisExp.addData('key_resp_move_s1.rt', key_resp_move_s1.rt)
thisExp.addData('key_resp_move_s1.started', key_resp_move_s1.tStartRefresh)
thisExp.addData('key_resp_move_s1.stopped', key_resp_move_s1.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_move" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "reward"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_reward.keys = []
key_resp_reward.rt = []
_key_resp_reward_allKeys = []
# keep track of which components have finished
rewardComponents = [text_reward, key_resp_reward]
for thisComponent in rewardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rewardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "reward"-------
while continueRoutine:
    # get current time
    t = rewardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rewardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_reward* updates
    if text_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_reward.frameNStart = frameN  # exact frame index
        text_reward.tStart = t  # local t and not account for scr refresh
        text_reward.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_reward, 'tStartRefresh')  # time at next scr refresh
        text_reward.setAutoDraw(True)
    
    # *key_resp_reward* updates
    waitOnFlip = False
    if key_resp_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_reward.frameNStart = frameN  # exact frame index
        key_resp_reward.tStart = t  # local t and not account for scr refresh
        key_resp_reward.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_reward, 'tStartRefresh')  # time at next scr refresh
        key_resp_reward.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_reward.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_reward.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_reward.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_reward.getKeys(keyList=None, waitRelease=False)
        _key_resp_reward_allKeys.extend(theseKeys)
        if len(_key_resp_reward_allKeys):
            key_resp_reward.keys = _key_resp_reward_allKeys[-1].name  # just the last key pressed
            key_resp_reward.rt = _key_resp_reward_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rewardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reward"-------
for thisComponent in rewardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_reward.started', text_reward.tStartRefresh)
thisExp.addData('text_reward.stopped', text_reward.tStopRefresh)
# check responses
if key_resp_reward.keys in ['', [], None]:  # No response was made
    key_resp_reward.keys = None
thisExp.addData('key_resp_reward.keys',key_resp_reward.keys)
if key_resp_reward.keys != None:  # we had a response
    thisExp.addData('key_resp_reward.rt', key_resp_reward.rt)
thisExp.addData('key_resp_reward.started', key_resp_reward.tStartRefresh)
thisExp.addData('key_resp_reward.stopped', key_resp_reward.tStopRefresh)
thisExp.nextEntry()
# the Routine "reward" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_practiceBlock"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_practiceBlock.keys = []
key_resp_practiceBlock.rt = []
_key_resp_practiceBlock_allKeys = []
# keep track of which components have finished
instructions_practiceBlockComponents = [text_practiceBlock, key_resp_practiceBlock]
for thisComponent in instructions_practiceBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_practiceBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_practiceBlock"-------
while continueRoutine:
    # get current time
    t = instructions_practiceBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_practiceBlockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_practiceBlock* updates
    if text_practiceBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_practiceBlock.frameNStart = frameN  # exact frame index
        text_practiceBlock.tStart = t  # local t and not account for scr refresh
        text_practiceBlock.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_practiceBlock, 'tStartRefresh')  # time at next scr refresh
        text_practiceBlock.setAutoDraw(True)
    
    # *key_resp_practiceBlock* updates
    waitOnFlip = False
    if key_resp_practiceBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_practiceBlock.frameNStart = frameN  # exact frame index
        key_resp_practiceBlock.tStart = t  # local t and not account for scr refresh
        key_resp_practiceBlock.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_practiceBlock, 'tStartRefresh')  # time at next scr refresh
        key_resp_practiceBlock.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_practiceBlock.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_practiceBlock.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_practiceBlock.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_practiceBlock.getKeys(keyList=None, waitRelease=False)
        _key_resp_practiceBlock_allKeys.extend(theseKeys)
        if len(_key_resp_practiceBlock_allKeys):
            key_resp_practiceBlock.keys = _key_resp_practiceBlock_allKeys[-1].name  # just the last key pressed
            key_resp_practiceBlock.rt = _key_resp_practiceBlock_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_practiceBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_practiceBlock"-------
for thisComponent in instructions_practiceBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_practiceBlock.started', text_practiceBlock.tStartRefresh)
thisExp.addData('text_practiceBlock.stopped', text_practiceBlock.tStopRefresh)
# check responses
if key_resp_practiceBlock.keys in ['', [], None]:  # No response was made
    key_resp_practiceBlock.keys = None
thisExp.addData('key_resp_practiceBlock.keys',key_resp_practiceBlock.keys)
if key_resp_practiceBlock.keys != None:  # we had a response
    thisExp.addData('key_resp_practiceBlock.rt', key_resp_practiceBlock.rt)
thisExp.addData('key_resp_practiceBlock.started', key_resp_practiceBlock.tStartRefresh)
thisExp.addData('key_resp_practiceBlock.stopped', key_resp_practiceBlock.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_practiceBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceBlock"-------
continueRoutine = True
# update component parameters for each repeat
# this is phase 0 (practice)
phaseN = 0
blockID = 0

# radioactive source image: yellow
sourceImageFile = os.path.join(imageRoot,"radioactive1.png")
volatility = 2

# we do not present any tones in this block
toneTrigger = 0
toneVolatility = 0
toneIndex = 0
toneEndFrame = 0

#load stimulusStream into NumPy array
block_path = sequenceRoot + practiceBlockFile
f = open(block_path, 'r')
storedStream_np = []
for line in f:
    words = line.split(',')
    storedStream_np.append((words[0], words[1], words[2]))
    
# calculate the total number of frames in this block
nFrames = len(storedStream_np) - 2
currentFrame = 0

#the ValueError: could not convert string to float error originates here
#need to start reading from the 2nd row rather than the 1st row (with header text)
#let's get rid of the first row since it's giving us headaches
storedStream_np.pop(0)

trueMean = float(storedStream_np[0][0])
laserRotation = float(storedStream_np[0][1])
trueVariance = float(storedStream_np[0][2])

#initialise variables that will be updated as experiment progresses

# send a trigger to mark the start of a main block
triggerValue = triggers['begin_pract']
sendTrigger = True
send_trigger(triggerValue)
#start by sending a trigger when subject presses a button
sendResponseTriggers = True
totalReward = 1
hit_i = 0
first_hit = 0

# reward bar variables
#bar_length = 0.5
top_amount = 1
bottom_amount = 0.8
#reward_change_colour = [1, -1, -1]
top_amount_text = "£%.2f" %(top_amount)
bottom_amount_text = "£%.2f" %(bottom_amount)

# shield position
shieldRotation = 360 #begin at top
shieldDegrees = 20
shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5
shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5

#calculate the screen X and Y locations that correspond to the shield centre
shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1
shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1
shieldX = np.concatenate(([0],shieldX))
shieldY = np.concatenate(([0],shieldY))
shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))

#update variables to draw polygon
laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation))
laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation))

# laser variables
unique, counts = np.unique(storedStream_np, return_counts=True)
laser_on = min(counts)
laser_frame_ct = 0

laser_practice.setAutoDraw(False)
laser_long_practice.setAutoDraw(False)

#progress circle variables
pc_orientation = 0
pc_degrees = 0
pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1
pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1
pc_X = np.concatenate(([0],pc_X))
pc_Y = np.concatenate(([0],pc_Y))
pc_coords = np.transpose(np.vstack((pc_X,pc_Y)))
laser_practice.setPos((0, 0))
laser_practice.setSize((1, 1))
laser_long_practice.setPos((0, 0))
laser_long_practice.setSize((1, 1))
radioactive_practice.setImage(sourceImageFile)
# keep track of which components have finished
practiceBlockComponents = [harmless_area_practice, shield_practice, shield_centre_practice, shield_bg_short_practice, laser_practice, laser_long_practice, progress_bar_practice, reward_bar_red, reward_bar, radioactive_practice, reward_text_top, reward_text_bottom]
for thisComponent in practiceBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceBlock"-------
while continueRoutine:
    # get current time
    t = practiceBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceBlockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    #determine whether laser is crossing the shield
    if hit_i:
        hit_i = 0
    else:
        if first_hit:
            laser_long_practice.setAutoDraw(True)
            
    # never go to negative reward
    if totalReward <= 0:
        totalReward = 0.1
        top_amount = 0.1
        bottom_amount = 0.0
        top_amount_text = "£%.2f" %(top_amount)
        bottom_amount_text = "£%.2f" %(bottom_amount)
    
    # update reward bar if loss was above 0.2
    if bar_length <= 0:
        bar_length = 0.5;
        top_amount = top_amount - 0.2;
        bottom_amount = bottom_amount - 0.2;
        top_amount_text = "£%.2f" %(top_amount);
        bottom_amount_text = "£%.2f" %(bottom_amount);
    
    #do not send a trigger on every frame, only if laser position changes or subject presses a button
    sendTrigger = False
    keyReleaseThisFrame = False
    triggerValue = 0
    send_trigger(triggerValue)
    #win.callOnFlip(trialTrigger.setData, int(0))
    
    #first, find out if L/R keys have been *released*
    LRkeys_released = kb.getKeys(keyList=keys_move,clear=True,waitRelease=True)
    if len(LRkeys_released)>0: #if so, then flush out the keys one final time
        LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=True,waitRelease=False)
        triggerValue = triggers['key_release']
        sendTrigger = True
        send_trigger(triggerValue)
        #win.callOnFlip(trialTrigger.setData, int(triggerValue))
        keyReleaseThisFrame = True
    else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
        LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=False,waitRelease=False)
    
    #if key is pressed, rotate cursor
    #using most recently pressed key
    if len(LRkeys_pressed)>0:
        if LRkeys_pressed[-1]==key_right:
            shieldRotation += ROTATION_SPEED;
            newTriggerValue = triggers['key_right']
        if LRkeys_pressed[-1]==key_left:
            shieldRotation -= ROTATION_SPEED;
            newTriggerValue = triggers['key_left']
        if sendResponseTriggers:
            triggerValue = newTriggerValue
            sendTrigger = True
            send_trigger(triggerValue)
            #win.callOnFlip(trialTrigger.setData, int(triggerValue))
            #stop triggering responses until key has been released again
            sendResponseTriggers = False
    
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    shieldX = np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY = np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    
    if currentFrame<nFrames:
        laserRotation = float(storedStream_np[currentFrame][1])#storedStream_np[currentFrame,1];
        trueMean = float(storedStream_np[currentFrame][0])#storedStream_np[currentFrame,0];
        trueVariance = float(storedStream_np[currentFrame][2])#storedStream_np[currentFrame,2];
        if currentFrame > 0:
            if float(storedStream_np[currentFrame][1]) != float(storedStream_np[currentFrame-1][1]):#storedStream_np[currentFrame - 1, 1]:
            #if currentFrame > 1:
                laser_frame_ct = 0;
            else:
                laser_frame_ct = laser_frame_ct + 1;
    
            if laser_frame_ct <= laser_on:
                laser_practice.setAutoDraw(True);
                laser_long_practice.setAutoDraw(True);
            else:
                laser_practice.setAutoDraw(False);
                laser_long_practice.setAutoDraw(False);
    
    #calculate whether shield is currently hit by laser
    currentHit = (shieldRotation - laserRotation + shieldDegrees)%360 <= (2*shieldDegrees);
    
    #determine whether laser position has changed
    if currentFrame == 0:
        if not sendTrigger:
            #we'll send different stim change triggers depending on hit/no-hit
            if currentHit:
                triggerValue = triggers['laser_hit']
            else:
                triggerValue = triggers['laser_miss']
    
            sendTrigger = True
            send_trigger(triggerValue)
            #win.callOnFlip(trialTrigger.setData, int(triggerValue))
    
        if currentHit:
            totalReward = totalReward
            red_bar_length = 0
            hit_i = 1
            first_hit = 1
        else:
            if totalReward > 0:
                totalReward = totalReward - lossFactor
                bar_length = bar_length - 2.5*lossFactor
                red_bar_length = 2.5*lossFactor
            else:
                totalReward = 0
                bar_length = 0.00001
                red_bar_length = 0
            
    if currentFrame > 0:
        if float(storedStream_np[currentFrame][1]) != float(storedStream_np[currentFrame-1][1]):
            #we only send a stimulus trigger if we don't already have a response to send
            if not sendTrigger:
                #we'll send different stim change triggers depending on hit/no-hit
                if currentHit:
                    triggerValue = triggers['laser_hit']
                else:
                    triggerValue = triggers['laser_miss']
    
                sendTrigger = True
                send_trigger(triggerValue)
                #win.callOnFlip(trialTrigger.setData, int(triggerValue))
    
            if currentHit:
                totalReward = totalReward
                red_bar_length = 0
                hit_i = 1
                first_hit = 1
            else:
                if totalReward > 0:
                    totalReward = totalReward - lossFactor
                    bar_length = bar_length - 2.5*lossFactor
                    red_bar_length = 2.5*lossFactor
                else:
                    totalReward = 0
                    bar_length = 0.00001
                    red_bar_length = 0
    
    #update the shieldRedness according to whether we are currently hitting/missing the shield
    if currentHit:
        laser_long_opacity = 0;    
        shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
    else:
        laser_long_opacity = 1
        shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
    
    if keyReleaseThisFrame:
        sendResponseTriggers = True
        
    if currentFrame<nFrames:
        saveData.append([phaseN,blockID,currentFrame,laserRotation,
            shieldRotation,shieldDegrees,currentHit,totalReward,
            sendTrigger,triggerValue,trueMean,trueVariance,volatility,
            toneTrigger,toneVolatility,toneIndex,toneEndFrame])
        currentFrame = currentFrame + 1;
    else:
        triggerValue = triggers['last_frame']
        sendTrigger = True
        send_trigger(triggerValue)
        #win.callOnFlip(trialTrigger.setData, int(triggerValue))
    
    pc_orientation = pc_orientation + (360/nFrames)/2;
    pc_degrees = pc_degrees + (360/nFrames)/2;
    pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
    pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
    pc_X = np.concatenate(([0],pc_X));
    pc_Y = np.concatenate(([0],pc_Y));
    pc_coords = np.transpose(np.vstack((pc_X,pc_Y)));
    
    # *harmless_area_practice* updates
    if harmless_area_practice.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        harmless_area_practice.frameNStart = frameN  # exact frame index
        harmless_area_practice.tStart = t  # local t and not account for scr refresh
        harmless_area_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(harmless_area_practice, 'tStartRefresh')  # time at next scr refresh
        harmless_area_practice.setAutoDraw(True)
    if harmless_area_practice.status == STARTED:
        if frameN >= (harmless_area_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            harmless_area_practice.tStop = t  # not accounting for scr refresh
            harmless_area_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(harmless_area_practice, 'tStopRefresh')  # time at next scr refresh
            harmless_area_practice.setAutoDraw(False)
    
    # *shield_practice* updates
    if shield_practice.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        shield_practice.frameNStart = frameN  # exact frame index
        shield_practice.tStart = t  # local t and not account for scr refresh
        shield_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_practice, 'tStartRefresh')  # time at next scr refresh
        shield_practice.setAutoDraw(True)
    if shield_practice.status == STARTED:
        if frameN >= (shield_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            shield_practice.tStop = t  # not accounting for scr refresh
            shield_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shield_practice, 'tStopRefresh')  # time at next scr refresh
            shield_practice.setAutoDraw(False)
    if shield_practice.status == STARTED:  # only update if drawing
        shield_practice.setFillColor(shieldColour, log=False)
        shield_practice.setOri(shieldRotation, log=False)
        shield_practice.setVertices(shieldCoords, log=False)
        shield_practice.setLineColor([0, 0, 0], log=False)
    
    # *shield_centre_practice* updates
    if shield_centre_practice.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        shield_centre_practice.frameNStart = frameN  # exact frame index
        shield_centre_practice.tStart = t  # local t and not account for scr refresh
        shield_centre_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_centre_practice, 'tStartRefresh')  # time at next scr refresh
        shield_centre_practice.setAutoDraw(True)
    if shield_centre_practice.status == STARTED:
        if frameN >= (shield_centre_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            shield_centre_practice.tStop = t  # not accounting for scr refresh
            shield_centre_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shield_centre_practice, 'tStopRefresh')  # time at next scr refresh
            shield_centre_practice.setAutoDraw(False)
    if shield_centre_practice.status == STARTED:  # only update if drawing
        shield_centre_practice.setPos((0, 0), log=False)
        shield_centre_practice.setOri(shieldRotation, log=False)
    
    # *shield_bg_short_practice* updates
    if shield_bg_short_practice.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        shield_bg_short_practice.frameNStart = frameN  # exact frame index
        shield_bg_short_practice.tStart = t  # local t and not account for scr refresh
        shield_bg_short_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shield_bg_short_practice, 'tStartRefresh')  # time at next scr refresh
        shield_bg_short_practice.setAutoDraw(True)
    if shield_bg_short_practice.status == STARTED:
        if frameN >= (shield_bg_short_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            shield_bg_short_practice.tStop = t  # not accounting for scr refresh
            shield_bg_short_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shield_bg_short_practice, 'tStopRefresh')  # time at next scr refresh
            shield_bg_short_practice.setAutoDraw(False)
    if shield_bg_short_practice.status == STARTED:  # only update if drawing
        shield_bg_short_practice.setFillColor([0, 0, 0], log=False)
        shield_bg_short_practice.setOri(shieldRotation, log=False)
        shield_bg_short_practice.setVertices(shieldCoords, log=False)
        shield_bg_short_practice.setLineColor([0, 0, 0], log=False)
    
    # *laser_practice* updates
    if laser_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        laser_practice.frameNStart = frameN  # exact frame index
        laser_practice.tStart = t  # local t and not account for scr refresh
        laser_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(laser_practice, 'tStartRefresh')  # time at next scr refresh
        laser_practice.setAutoDraw(True)
    if laser_practice.status == STARTED:
        if frameN >= (laser_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            laser_practice.tStop = t  # not accounting for scr refresh
            laser_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(laser_practice, 'tStopRefresh')  # time at next scr refresh
            laser_practice.setAutoDraw(False)
    if laser_practice.status == STARTED:  # only update if drawing
        laser_practice.setOri(laserRotation, log=False)
        laser_practice.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.1]], log=False)
    
    # *laser_long_practice* updates
    if laser_long_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        laser_long_practice.frameNStart = frameN  # exact frame index
        laser_long_practice.tStart = t  # local t and not account for scr refresh
        laser_long_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(laser_long_practice, 'tStartRefresh')  # time at next scr refresh
        laser_long_practice.setAutoDraw(True)
    if laser_long_practice.status == STARTED:
        if frameN >= (laser_long_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            laser_long_practice.tStop = t  # not accounting for scr refresh
            laser_long_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(laser_long_practice, 'tStopRefresh')  # time at next scr refresh
            laser_long_practice.setAutoDraw(False)
    if laser_long_practice.status == STARTED:  # only update if drawing
        laser_long_practice.setOpacity(laser_long_opacity, log=False)
        laser_long_practice.setOri(laserRotation, log=False)
        laser_long_practice.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.4]], log=False)
    
    # *progress_bar_practice* updates
    if progress_bar_practice.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        progress_bar_practice.frameNStart = frameN  # exact frame index
        progress_bar_practice.tStart = t  # local t and not account for scr refresh
        progress_bar_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(progress_bar_practice, 'tStartRefresh')  # time at next scr refresh
        progress_bar_practice.setAutoDraw(True)
    if progress_bar_practice.status == STARTED:
        if frameN >= (progress_bar_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            progress_bar_practice.tStop = t  # not accounting for scr refresh
            progress_bar_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(progress_bar_practice, 'tStopRefresh')  # time at next scr refresh
            progress_bar_practice.setAutoDraw(False)
    if progress_bar_practice.status == STARTED:  # only update if drawing
        progress_bar_practice.setOri(pc_orientation, log=False)
        progress_bar_practice.setVertices(pc_coords, log=False)
    
    # *reward_bar_red* updates
    if reward_bar_red.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        reward_bar_red.frameNStart = frameN  # exact frame index
        reward_bar_red.tStart = t  # local t and not account for scr refresh
        reward_bar_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reward_bar_red, 'tStartRefresh')  # time at next scr refresh
        reward_bar_red.setAutoDraw(True)
    if reward_bar_red.status == STARTED:
        if frameN >= (reward_bar_red.frameNStart + nFrames):
            # keep track of stop time/frame for later
            reward_bar_red.tStop = t  # not accounting for scr refresh
            reward_bar_red.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reward_bar_red, 'tStopRefresh')  # time at next scr refresh
            reward_bar_red.setAutoDraw(False)
    if reward_bar_red.status == STARTED:  # only update if drawing
        reward_bar_red.setFillColor(reward_change_colour, log=False)
        reward_bar_red.setPos((0.6, -0.3+bar_length), log=False)
        reward_bar_red.setSize((0.05, red_bar_length), log=False)
        reward_bar_red.setLineColor(reward_change_colour, log=False)
    
    # *reward_bar* updates
    if reward_bar.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        reward_bar.frameNStart = frameN  # exact frame index
        reward_bar.tStart = t  # local t and not account for scr refresh
        reward_bar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reward_bar, 'tStartRefresh')  # time at next scr refresh
        reward_bar.setAutoDraw(True)
    if reward_bar.status == STARTED:
        if frameN >= (reward_bar.frameNStart + nFrames):
            # keep track of stop time/frame for later
            reward_bar.tStop = t  # not accounting for scr refresh
            reward_bar.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reward_bar, 'tStopRefresh')  # time at next scr refresh
            reward_bar.setAutoDraw(False)
    if reward_bar.status == STARTED:  # only update if drawing
        reward_bar.setSize((0.05, bar_length), log=False)
    
    # *radioactive_practice* updates
    if radioactive_practice.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        radioactive_practice.frameNStart = frameN  # exact frame index
        radioactive_practice.tStart = t  # local t and not account for scr refresh
        radioactive_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radioactive_practice, 'tStartRefresh')  # time at next scr refresh
        radioactive_practice.setAutoDraw(True)
    if radioactive_practice.status == STARTED:
        if frameN >= (radioactive_practice.frameNStart + nFrames):
            # keep track of stop time/frame for later
            radioactive_practice.tStop = t  # not accounting for scr refresh
            radioactive_practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(radioactive_practice, 'tStopRefresh')  # time at next scr refresh
            radioactive_practice.setAutoDraw(False)
    
    # *reward_text_top* updates
    if reward_text_top.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        reward_text_top.frameNStart = frameN  # exact frame index
        reward_text_top.tStart = t  # local t and not account for scr refresh
        reward_text_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reward_text_top, 'tStartRefresh')  # time at next scr refresh
        reward_text_top.setAutoDraw(True)
    if reward_text_top.status == STARTED:
        if frameN >= (reward_text_top.frameNStart + nFrames):
            # keep track of stop time/frame for later
            reward_text_top.tStop = t  # not accounting for scr refresh
            reward_text_top.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reward_text_top, 'tStopRefresh')  # time at next scr refresh
            reward_text_top.setAutoDraw(False)
    if reward_text_top.status == STARTED:  # only update if drawing
        reward_text_top.setText(top_amount_text, log=False)
    
    # *reward_text_bottom* updates
    if reward_text_bottom.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        reward_text_bottom.frameNStart = frameN  # exact frame index
        reward_text_bottom.tStart = t  # local t and not account for scr refresh
        reward_text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(reward_text_bottom, 'tStartRefresh')  # time at next scr refresh
        reward_text_bottom.setAutoDraw(True)
    if reward_text_bottom.status == STARTED:
        if frameN >= (reward_text_bottom.frameNStart + nFrames):
            # keep track of stop time/frame for later
            reward_text_bottom.tStop = t  # not accounting for scr refresh
            reward_text_bottom.frameNStop = frameN  # exact frame index
            win.timeOnFlip(reward_text_bottom, 'tStopRefresh')  # time at next scr refresh
            reward_text_bottom.setAutoDraw(False)
    if reward_text_bottom.status == STARTED:  # only update if drawing
        reward_text_bottom.setText(bottom_amount_text, log=False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceBlock"-------
for thisComponent in practiceBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# this block will not count towards the total reward
#totalReward_tot = totalReward_tot + totalReward
totalReward_text = "£%.2f" %(totalReward)

# save the output data for this block
np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
#win.callOnFlip(trialTrigger.setData, int(0))
triggerValue = 0
send_trigger(triggerValue)
sendTrigger = False
thisExp.addData('harmless_area_practice.started', harmless_area_practice.tStartRefresh)
thisExp.addData('harmless_area_practice.stopped', harmless_area_practice.tStopRefresh)
thisExp.addData('shield_practice.started', shield_practice.tStartRefresh)
thisExp.addData('shield_practice.stopped', shield_practice.tStopRefresh)
thisExp.addData('shield_centre_practice.started', shield_centre_practice.tStartRefresh)
thisExp.addData('shield_centre_practice.stopped', shield_centre_practice.tStopRefresh)
thisExp.addData('shield_bg_short_practice.started', shield_bg_short_practice.tStartRefresh)
thisExp.addData('shield_bg_short_practice.stopped', shield_bg_short_practice.tStopRefresh)
thisExp.addData('laser_practice.started', laser_practice.tStartRefresh)
thisExp.addData('laser_practice.stopped', laser_practice.tStopRefresh)
thisExp.addData('laser_long_practice.started', laser_long_practice.tStartRefresh)
thisExp.addData('laser_long_practice.stopped', laser_long_practice.tStopRefresh)
thisExp.addData('progress_bar_practice.started', progress_bar_practice.tStartRefresh)
thisExp.addData('progress_bar_practice.stopped', progress_bar_practice.tStopRefresh)
thisExp.addData('reward_bar_red.started', reward_bar_red.tStartRefresh)
thisExp.addData('reward_bar_red.stopped', reward_bar_red.tStopRefresh)
thisExp.addData('reward_bar.started', reward_bar.tStartRefresh)
thisExp.addData('reward_bar.stopped', reward_bar.tStopRefresh)
thisExp.addData('radioactive_practice.started', radioactive_practice.tStartRefresh)
thisExp.addData('radioactive_practice.stopped', radioactive_practice.tStopRefresh)
thisExp.addData('reward_text_top.started', reward_text_top.tStartRefresh)
thisExp.addData('reward_text_top.stopped', reward_text_top.tStopRefresh)
thisExp.addData('reward_text_bottom.started', reward_text_bottom.tStartRefresh)
thisExp.addData('reward_text_bottom.stopped', reward_text_bottom.tStopRefresh)
# the Routine "practiceBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "afterPractice"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_afterPractice.keys = []
key_resp_afterPractice.rt = []
_key_resp_afterPractice_allKeys = []
# keep track of which components have finished
afterPracticeComponents = [after_practice_explanation, key_resp_afterPractice]
for thisComponent in afterPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
afterPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "afterPractice"-------
while continueRoutine:
    # get current time
    t = afterPracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=afterPracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *after_practice_explanation* updates
    if after_practice_explanation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        after_practice_explanation.frameNStart = frameN  # exact frame index
        after_practice_explanation.tStart = t  # local t and not account for scr refresh
        after_practice_explanation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(after_practice_explanation, 'tStartRefresh')  # time at next scr refresh
        after_practice_explanation.setAutoDraw(True)
    
    # *key_resp_afterPractice* updates
    waitOnFlip = False
    if key_resp_afterPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_afterPractice.frameNStart = frameN  # exact frame index
        key_resp_afterPractice.tStart = t  # local t and not account for scr refresh
        key_resp_afterPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_afterPractice, 'tStartRefresh')  # time at next scr refresh
        key_resp_afterPractice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_afterPractice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_afterPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_afterPractice.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_afterPractice.getKeys(keyList=['3'], waitRelease=False)
        _key_resp_afterPractice_allKeys.extend(theseKeys)
        if len(_key_resp_afterPractice_allKeys):
            key_resp_afterPractice.keys = _key_resp_afterPractice_allKeys[-1].name  # just the last key pressed
            key_resp_afterPractice.rt = _key_resp_afterPractice_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in afterPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "afterPractice"-------
for thisComponent in afterPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('after_practice_explanation.started', after_practice_explanation.tStartRefresh)
thisExp.addData('after_practice_explanation.stopped', after_practice_explanation.tStopRefresh)
# check responses
if key_resp_afterPractice.keys in ['', [], None]:  # No response was made
    key_resp_afterPractice.keys = None
thisExp.addData('key_resp_afterPractice.keys',key_resp_afterPractice.keys)
if key_resp_afterPractice.keys != None:  # we had a response
    thisExp.addData('key_resp_afterPractice.rt', key_resp_afterPractice.rt)
thisExp.addData('key_resp_afterPractice.started', key_resp_afterPractice.tStartRefresh)
thisExp.addData('key_resp_afterPractice.stopped', key_resp_afterPractice.tStopRefresh)
thisExp.nextEntry()
# the Routine "afterPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_mainTask"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_mainTask.keys = []
key_resp_mainTask.rt = []
_key_resp_mainTask_allKeys = []
# keep track of which components have finished
instructions_mainTaskComponents = [text_mainTask, key_resp_mainTask]
for thisComponent in instructions_mainTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_mainTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_mainTask"-------
while continueRoutine:
    # get current time
    t = instructions_mainTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_mainTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_mainTask* updates
    if text_mainTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_mainTask.frameNStart = frameN  # exact frame index
        text_mainTask.tStart = t  # local t and not account for scr refresh
        text_mainTask.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_mainTask, 'tStartRefresh')  # time at next scr refresh
        text_mainTask.setAutoDraw(True)
    
    # *key_resp_mainTask* updates
    waitOnFlip = False
    if key_resp_mainTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_mainTask.frameNStart = frameN  # exact frame index
        key_resp_mainTask.tStart = t  # local t and not account for scr refresh
        key_resp_mainTask.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_mainTask, 'tStartRefresh')  # time at next scr refresh
        key_resp_mainTask.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_mainTask.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_mainTask.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_mainTask.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_mainTask.getKeys(keyList=['3'], waitRelease=False)
        _key_resp_mainTask_allKeys.extend(theseKeys)
        if len(_key_resp_mainTask_allKeys):
            key_resp_mainTask.keys = _key_resp_mainTask_allKeys[-1].name  # just the last key pressed
            key_resp_mainTask.rt = _key_resp_mainTask_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_mainTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_mainTask"-------
for thisComponent in instructions_mainTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_mainTask.started', text_mainTask.tStartRefresh)
thisExp.addData('text_mainTask.stopped', text_mainTask.tStopRefresh)
# check responses
if key_resp_mainTask.keys in ['', [], None]:  # No response was made
    key_resp_mainTask.keys = None
thisExp.addData('key_resp_mainTask.keys',key_resp_mainTask.keys)
if key_resp_mainTask.keys != None:  # we had a response
    thisExp.addData('key_resp_mainTask.rt', key_resp_mainTask.rt)
thisExp.addData('key_resp_mainTask.started', key_resp_mainTask.tStartRefresh)
thisExp.addData('key_resp_mainTask.stopped', key_resp_mainTask.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_mainTask" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "radio_colours"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_colours.keys = []
key_resp_colours.rt = []
_key_resp_colours_allKeys = []
# keep track of which components have finished
radio_coloursComponents = [radioactive_colour1, radioactive_colour2, text_colours, key_resp_colours]
for thisComponent in radio_coloursComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
radio_coloursClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "radio_colours"-------
while continueRoutine:
    # get current time
    t = radio_coloursClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=radio_coloursClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *radioactive_colour1* updates
    if radioactive_colour1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        radioactive_colour1.frameNStart = frameN  # exact frame index
        radioactive_colour1.tStart = t  # local t and not account for scr refresh
        radioactive_colour1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radioactive_colour1, 'tStartRefresh')  # time at next scr refresh
        radioactive_colour1.setAutoDraw(True)
    
    # *radioactive_colour2* updates
    if radioactive_colour2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        radioactive_colour2.frameNStart = frameN  # exact frame index
        radioactive_colour2.tStart = t  # local t and not account for scr refresh
        radioactive_colour2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(radioactive_colour2, 'tStartRefresh')  # time at next scr refresh
        radioactive_colour2.setAutoDraw(True)
    
    # *text_colours* updates
    if text_colours.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_colours.frameNStart = frameN  # exact frame index
        text_colours.tStart = t  # local t and not account for scr refresh
        text_colours.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_colours, 'tStartRefresh')  # time at next scr refresh
        text_colours.setAutoDraw(True)
    
    # *key_resp_colours* updates
    waitOnFlip = False
    if key_resp_colours.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_colours.frameNStart = frameN  # exact frame index
        key_resp_colours.tStart = t  # local t and not account for scr refresh
        key_resp_colours.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_colours, 'tStartRefresh')  # time at next scr refresh
        key_resp_colours.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_colours.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_colours.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_colours.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_colours.getKeys(keyList=['3'], waitRelease=False)
        _key_resp_colours_allKeys.extend(theseKeys)
        if len(_key_resp_colours_allKeys):
            key_resp_colours.keys = _key_resp_colours_allKeys[-1].name  # just the last key pressed
            key_resp_colours.rt = _key_resp_colours_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in radio_coloursComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "radio_colours"-------
for thisComponent in radio_coloursComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('radioactive_colour1.started', radioactive_colour1.tStartRefresh)
thisExp.addData('radioactive_colour1.stopped', radioactive_colour1.tStopRefresh)
thisExp.addData('radioactive_colour2.started', radioactive_colour2.tStartRefresh)
thisExp.addData('radioactive_colour2.stopped', radioactive_colour2.tStopRefresh)
thisExp.addData('text_colours.started', text_colours.tStartRefresh)
thisExp.addData('text_colours.stopped', text_colours.tStopRefresh)
# check responses
if key_resp_colours.keys in ['', [], None]:  # No response was made
    key_resp_colours.keys = None
thisExp.addData('key_resp_colours.keys',key_resp_colours.keys)
if key_resp_colours.keys != None:  # we had a response
    thisExp.addData('key_resp_colours.rt', key_resp_colours.rt)
thisExp.addData('key_resp_colours.started', key_resp_colours.tStartRefresh)
thisExp.addData('key_resp_colours.stopped', key_resp_colours.tStopRefresh)
thisExp.nextEntry()
# the Routine "radio_colours" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(sessionFileName),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blockStartText"-------
    continueRoutine = True
    # update component parameters for each repeat
    #determine radioactive source image
    sourceImageFile = os.path.join(imageRoot,sourceImage)
    radioactive_block_source.setImage(sourceImageFile)
    key_resp_blockStart.keys = []
    key_resp_blockStart.rt = []
    _key_resp_blockStart_allKeys = []
    # keep track of which components have finished
    blockStartTextComponents = [radioactive_block_source, text_sourceImage, key_resp_blockStart]
    for thisComponent in blockStartTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockStartTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blockStartText"-------
    while continueRoutine:
        # get current time
        t = blockStartTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockStartTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *radioactive_block_source* updates
        if radioactive_block_source.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            radioactive_block_source.frameNStart = frameN  # exact frame index
            radioactive_block_source.tStart = t  # local t and not account for scr refresh
            radioactive_block_source.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(radioactive_block_source, 'tStartRefresh')  # time at next scr refresh
            radioactive_block_source.setAutoDraw(True)
        
        # *text_sourceImage* updates
        if text_sourceImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sourceImage.frameNStart = frameN  # exact frame index
            text_sourceImage.tStart = t  # local t and not account for scr refresh
            text_sourceImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sourceImage, 'tStartRefresh')  # time at next scr refresh
            text_sourceImage.setAutoDraw(True)
        
        # *key_resp_blockStart* updates
        waitOnFlip = False
        if key_resp_blockStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_blockStart.frameNStart = frameN  # exact frame index
            key_resp_blockStart.tStart = t  # local t and not account for scr refresh
            key_resp_blockStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_blockStart, 'tStartRefresh')  # time at next scr refresh
            key_resp_blockStart.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_blockStart.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_blockStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_blockStart.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_blockStart.getKeys(keyList=None, waitRelease=False)
            _key_resp_blockStart_allKeys.extend(theseKeys)
            if len(_key_resp_blockStart_allKeys):
                key_resp_blockStart.keys = _key_resp_blockStart_allKeys[-1].name  # just the last key pressed
                key_resp_blockStart.rt = _key_resp_blockStart_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockStartTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockStartText"-------
    for thisComponent in blockStartTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('radioactive_block_source.started', radioactive_block_source.tStartRefresh)
    blocks.addData('radioactive_block_source.stopped', radioactive_block_source.tStopRefresh)
    blocks.addData('text_sourceImage.started', text_sourceImage.tStartRefresh)
    blocks.addData('text_sourceImage.stopped', text_sourceImage.tStopRefresh)
    # check responses
    if key_resp_blockStart.keys in ['', [], None]:  # No response was made
        key_resp_blockStart.keys = None
    blocks.addData('key_resp_blockStart.keys',key_resp_blockStart.keys)
    if key_resp_blockStart.keys != None:  # we had a response
        blocks.addData('key_resp_blockStart.rt', key_resp_blockStart.rt)
    blocks.addData('key_resp_blockStart.started', key_resp_blockStart.tStartRefresh)
    blocks.addData('key_resp_blockStart.stopped', key_resp_blockStart.tStopRefresh)
    # the Routine "blockStartText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # this is the actual experiment
    phaseN = 1
    
    #load stimulusStream into NumPy array
    block_path = sequenceRoot + blockFileName
    f = open(block_path, 'r')
    storedStream_np = []
    for line in f:
        words = line.split(',')
        storedStream_np.append((words[0], words[1], words[2]))
        
    #calculate the total number of frames in this block
    nFrames = len(storedStream_np) - 2 # try debug IndexError:list index out of range
    currentFrame = 0
    
    #the ValueError: could not convert string to float error originates here
    #need to start reading from the 2nd row rather than the 1st row (with header text)
    #let's get rid of the first row since it's giving us headaches
    storedStream_np.pop(0)
    
    trueMean = float(storedStream_np[0][0])
    laserRotation = float(storedStream_np[0][1])
    trueVariance = float(storedStream_np[0][2])
    
    #initialise variables that will be updated as experiment progresses
    hit_i = 0
    first_hit = 0
    
    # send a trigger to mark the start of a main block
    triggerValue = triggers['begin_main']
    sendTrigger = True
    send_trigger(triggerValue)
    #start by sending a trigger when subject presses a button
    sendResponseTriggers = True
    totalReward = 1;
    
    shieldDegrees = 20; #because it needs to be predefined
    shieldRotation = 360 #begin at top
    
    shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
    
    #calculate the screen X and Y locations that correspond to the shield centre
    shieldX=np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldY=np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
    shieldX = np.concatenate(([0],shieldX));
    shieldY = np.concatenate(([0],shieldY));
    shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
    
    #update variables to draw polygon
    laserXcoord = CIRCLE_RADIUS*cos(deg2rad(laserRotation));
    laserYcoord = CIRCLE_RADIUS*sin(deg2rad(laserRotation));
    
    unique, counts = np.unique(storedStream_np, return_counts=True);
    laser_on = min(counts);
    laser_frame_ct = 0;
    
    laser.setAutoDraw(False);
    laser_long.setAutoDraw(False);
    
    #progress circle variables
    pc_orientation = 0;
    pc_degrees = 0;
    pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
    pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
    pc_X = np.concatenate(([0],pc_X));
    pc_Y = np.concatenate(([0],pc_Y));
    pc_coords = np.transpose(np.vstack((pc_X,pc_Y)))
    laser.setPos((0, 0))
    laser.setSize((1, 1))
    laser_long.setPos((0, 0))
    laser_long.setSize((1, 1))
    radioactive.setImage(sourceImageFile)
    #initialise some things
    toneOnsets=[]
    ISIs=[]
    
    # make tone sequence of S and Ds
    toneFilePath = "sequences/"+toneSeqFileName;
    
    #load tone stimuli stream into NumPy array
    f = open(toneFilePath, 'r');
    toneStream_np = [];
    for line in f:
        tones = line.split(',');
        toneStream_np.append(tones[0].strip());
    
    #  tone entry 0 is variable name, start at 1
    toneIndex = 1
    nTones = len(toneStream_np)-1
    toneEndFrame = 0
    
    # current tone 
    toneCurr = toneStream_np[toneIndex]
    if toneCurr == "1":
        lastTone = 1
    else:
        lastTone = 2
    
    # define the two tones
    global tone1
    global tone2
    tone1 = sound.Sound(440, secs=0.05, stereo=True, hamming=True,
            syncToWin=True,  name='sound_short')
    tone1.setVolume(1)
    tone2 = sound.Sound(440, secs=0.1, stereo=True, hamming=True,
           syncToWin=True, name='sound_long')
    tone2.setVolume(1)
    
    # ISIs corresponding to tones, in frames
    # isi = soa - toneDuration
    # isi1 = 450-100 *60/1000
    isi1 = 24
    # isi2 = 450-500 *60/1000
    isi2 = 21
     
    # start with no tone and no ISI
    toneIsPlaying = False
    toneIsWaiting = False
    toneTrig = 0
    
    # start with frame 0
    iFrame = 0
    # keep track of which components have finished
    trialComponents = [harmless_area, shield, shield_centre, shield_bg_short, laser, laser_long, progress_bar, radioactive]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #determine whether laser is crossing the shield
        if hit_i:
            hit_i = 0
        else:
            if first_hit:
                laser_long.setAutoDraw(True)
                
        if totalReward <= 0:
            totalReward = 0.1;
        
        #do not send a trigger on every frame, only if laser position changes or subject presses a button
        sendTrigger = False
        keyReleaseThisFrame = False
        triggerValue = 0
        send_trigger(triggerValue)
        #win.callOnFlip(trialTrigger.setData, int(0))
        
        #first, find out if L/R keys have been *released*
        LRkeys_released = kb.getKeys(keyList=keys_move,clear=True,waitRelease=True)
        if len(LRkeys_released)>0: #if so, then flush out the keys one final time
            LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=True,waitRelease=False)
            triggerValue = triggers['key_release']
            sendTrigger = True
            send_trigger(triggerValue)
            #win.callOnFlip(trialTrigger.setData, int(triggerValue))
            keyReleaseThisFrame = True
        else: #otherwise, put the currently pressed keys into a list, finishing with the most recently pressed
            LRkeys_pressed = kb.getKeys(keyList=keys_move,clear=False,waitRelease=False)
        
        #if key is pressed, rotate cursor
        #using most recently pressed key
        if len(LRkeys_pressed)>0:
            if LRkeys_pressed[-1]==key_right:
                shieldRotation += ROTATION_SPEED;
                newTriggerValue = triggers['key_right']
            if LRkeys_pressed[-1]==key_left:
                shieldRotation -= ROTATION_SPEED;
                newTriggerValue = triggers['key_left']
            if sendResponseTriggers:
                triggerValue = newTriggerValue
                sendTrigger = True
                send_trigger(triggerValue)
                #win.callOnFlip(trialTrigger.setData, int(triggerValue))
                #stop triggering responses until key has been released again
                sendResponseTriggers = False
        
        shieldWidth = np.sin(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        shieldHeight = np.cos(np.radians(shieldDegrees))*CIRCLE_RADIUS*1.5;
        
        shieldX = np.sin(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldY = np.cos(np.arange(np.radians(-shieldDegrees),np.radians(shieldDegrees),np.radians(shieldDegrees)/20))*CIRCLE_RADIUS*1.1;
        shieldX = np.concatenate(([0],shieldX));
        shieldY = np.concatenate(([0],shieldY));
        shieldCoords = np.transpose(np.vstack((shieldX,shieldY)))
        
        if currentFrame<nFrames:
            laserRotation = float(storedStream_np[currentFrame][1])#storedStream_np[currentFrame,1];
            trueMean = float(storedStream_np[currentFrame][0])#storedStream_np[currentFrame,0];
            trueVariance = float(storedStream_np[currentFrame][2])#storedStream_np[currentFrame,2];
            if currentFrame > 0:
                if float(storedStream_np[currentFrame][1]) != float(storedStream_np[currentFrame-1][1]):#storedStream_np[currentFrame - 1, 1]:
                #if currentFrame > 1:
                    laser_frame_ct = 0;
                else:
                    laser_frame_ct = laser_frame_ct + 1;
        
                if laser_frame_ct <= laser_on:
                    laser.setAutoDraw(True);
                    laser_long.setAutoDraw(True);
                else:
                    laser.setAutoDraw(False);
                    laser_long.setAutoDraw(False);
        
        #calculate whether shield is currently hit by laser
        currentHit = (shieldRotation - laserRotation + shieldDegrees)%360 <= (2*shieldDegrees);
        
        #determine whether laser position has changed
        if currentFrame == 0:
            if not sendTrigger:
                #we'll send different stim change triggers depending on hit/no-hit
                if currentHit:
                    triggerValue = triggers['laser_hit']
                else:
                    triggerValue = triggers['laser_miss']
        
                sendTrigger = True
                send_trigger(triggerValue)
                #win.callOnFlip(trialTrigger.setData, int(triggerValue))
        
            if currentHit:
                totalReward = totalReward;
                hit_i = 1;
                first_hit = 1;
            else:
                if totalReward > 0:
                    totalReward = totalReward - lossFactor;
                else:
                    totalReward = 0;
                
        if currentFrame > 0:
            if float(storedStream_np[currentFrame][1]) != float(storedStream_np[currentFrame-1][1]):
                #we only send a stimulus trigger if we don't already have a response to send
                if not sendTrigger:
                    #we'll send different stim change triggers depending on hit/no-hit
                    if currentHit:
                        triggerValue = triggers['laser_hit']
                    else:
                        triggerValue = triggers['laser_miss']
        
                    sendTrigger = True
                    send_trigger(triggerValue)
                    #win.callOnFlip(trialTrigger.setData, int(triggerValue))
        
                if currentHit:
                    totalReward = totalReward;
                    hit_i = 1;
                    first_hit = 1;
                else:
                    if totalReward > 0:
                        totalReward = totalReward - lossFactor;
                    else:
                        totalReward = 0;
        
        #update the shieldRedness according to whether we are currently hitting/missing the shield
        if currentHit:
            laser_long_opacity = 0;    
            shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
        else:
            laser_long_opacity = 1
            shieldColour = [1, 1-(1-laser_long_opacity), 1-(1-laser_long_opacity)];
        
        if keyReleaseThisFrame:
            sendResponseTriggers = True
            
        if currentFrame<nFrames:
            saveData.append([phaseN,blockID,currentFrame,laserRotation,
            shieldRotation,shieldDegrees,currentHit,totalReward,
            sendTrigger,triggerValue,trueMean,trueVariance,volatility,
            toneTrig,toneVolatility,toneIndex,toneEndFrame])
            currentFrame = currentFrame + 1;
        else:
            triggerValue = triggers['last_frame']
            sendTrigger = True
            send_trigger(triggerValue)
            #win.callOnFlip(trialTrigger.setData, int(triggerValue))
        
        pc_orientation = pc_orientation + (360/nFrames)/2;
        pc_degrees = pc_degrees + (360/nFrames)/2;
        pc_X=np.sin(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
        pc_Y=np.cos(np.arange(np.radians(-pc_degrees),np.radians(pc_degrees),np.radians(10)/20))*CIRCLE_RADIUS*1.1;
        pc_X = np.concatenate(([0],pc_X));
        pc_Y = np.concatenate(([0],pc_Y));
        pc_coords = np.transpose(np.vstack((pc_X,pc_Y)));
        
        # *harmless_area* updates
        if harmless_area.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            harmless_area.frameNStart = frameN  # exact frame index
            harmless_area.tStart = t  # local t and not account for scr refresh
            harmless_area.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(harmless_area, 'tStartRefresh')  # time at next scr refresh
            harmless_area.setAutoDraw(True)
        if harmless_area.status == STARTED:
            if frameN >= (harmless_area.frameNStart + nFrames):
                # keep track of stop time/frame for later
                harmless_area.tStop = t  # not accounting for scr refresh
                harmless_area.frameNStop = frameN  # exact frame index
                win.timeOnFlip(harmless_area, 'tStopRefresh')  # time at next scr refresh
                harmless_area.setAutoDraw(False)
        
        # *shield* updates
        if shield.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield.frameNStart = frameN  # exact frame index
            shield.tStart = t  # local t and not account for scr refresh
            shield.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield, 'tStartRefresh')  # time at next scr refresh
            shield.setAutoDraw(True)
        if shield.status == STARTED:
            if frameN >= (shield.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield.tStop = t  # not accounting for scr refresh
                shield.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield, 'tStopRefresh')  # time at next scr refresh
                shield.setAutoDraw(False)
        if shield.status == STARTED:  # only update if drawing
            shield.setFillColor(shieldColour, log=False)
            shield.setOri(shieldRotation, log=False)
            shield.setVertices(shieldCoords, log=False)
            shield.setLineColor([0, 0, 0], log=False)
        
        # *shield_centre* updates
        if shield_centre.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_centre.frameNStart = frameN  # exact frame index
            shield_centre.tStart = t  # local t and not account for scr refresh
            shield_centre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_centre, 'tStartRefresh')  # time at next scr refresh
            shield_centre.setAutoDraw(True)
        if shield_centre.status == STARTED:
            if frameN >= (shield_centre.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_centre.tStop = t  # not accounting for scr refresh
                shield_centre.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_centre, 'tStopRefresh')  # time at next scr refresh
                shield_centre.setAutoDraw(False)
        if shield_centre.status == STARTED:  # only update if drawing
            shield_centre.setPos((0, 0), log=False)
            shield_centre.setOri(shieldRotation, log=False)
        
        # *shield_bg_short* updates
        if shield_bg_short.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            shield_bg_short.frameNStart = frameN  # exact frame index
            shield_bg_short.tStart = t  # local t and not account for scr refresh
            shield_bg_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(shield_bg_short, 'tStartRefresh')  # time at next scr refresh
            shield_bg_short.setAutoDraw(True)
        if shield_bg_short.status == STARTED:
            if frameN >= (shield_bg_short.frameNStart + nFrames):
                # keep track of stop time/frame for later
                shield_bg_short.tStop = t  # not accounting for scr refresh
                shield_bg_short.frameNStop = frameN  # exact frame index
                win.timeOnFlip(shield_bg_short, 'tStopRefresh')  # time at next scr refresh
                shield_bg_short.setAutoDraw(False)
        if shield_bg_short.status == STARTED:  # only update if drawing
            shield_bg_short.setFillColor([0, 0, 0], log=False)
            shield_bg_short.setOri(shieldRotation, log=False)
            shield_bg_short.setVertices(shieldCoords, log=False)
            shield_bg_short.setLineColor([0, 0, 0], log=False)
        
        # *laser* updates
        if laser.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laser.frameNStart = frameN  # exact frame index
            laser.tStart = t  # local t and not account for scr refresh
            laser.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser, 'tStartRefresh')  # time at next scr refresh
            laser.setAutoDraw(True)
        if laser.status == STARTED:
            if frameN >= (laser.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser.tStop = t  # not accounting for scr refresh
                laser.frameNStop = frameN  # exact frame index
                win.timeOnFlip(laser, 'tStopRefresh')  # time at next scr refresh
                laser.setAutoDraw(False)
        if laser.status == STARTED:  # only update if drawing
            laser.setOri(laserRotation, log=False)
            laser.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.1]], log=False)
        
        # *laser_long* updates
        if laser_long.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            laser_long.frameNStart = frameN  # exact frame index
            laser_long.tStart = t  # local t and not account for scr refresh
            laser_long.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(laser_long, 'tStartRefresh')  # time at next scr refresh
            laser_long.setAutoDraw(True)
        if laser_long.status == STARTED:
            if frameN >= (laser_long.frameNStart + nFrames):
                # keep track of stop time/frame for later
                laser_long.tStop = t  # not accounting for scr refresh
                laser_long.frameNStop = frameN  # exact frame index
                win.timeOnFlip(laser_long, 'tStopRefresh')  # time at next scr refresh
                laser_long.setAutoDraw(False)
        if laser_long.status == STARTED:  # only update if drawing
            laser_long.setOpacity(laser_long_opacity, log=False)
            laser_long.setOri(laserRotation, log=False)
            laser_long.setVertices([[0, 0], [0, CIRCLE_RADIUS*1.4]], log=False)
        
        # *progress_bar* updates
        if progress_bar.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            progress_bar.frameNStart = frameN  # exact frame index
            progress_bar.tStart = t  # local t and not account for scr refresh
            progress_bar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress_bar, 'tStartRefresh')  # time at next scr refresh
            progress_bar.setAutoDraw(True)
        if progress_bar.status == STARTED:
            if frameN >= (progress_bar.frameNStart + nFrames):
                # keep track of stop time/frame for later
                progress_bar.tStop = t  # not accounting for scr refresh
                progress_bar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(progress_bar, 'tStopRefresh')  # time at next scr refresh
                progress_bar.setAutoDraw(False)
        if progress_bar.status == STARTED:  # only update if drawing
            progress_bar.setOri(pc_orientation, log=False)
            progress_bar.setVertices(pc_coords, log=False)
        
        # *radioactive* updates
        if radioactive.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            radioactive.frameNStart = frameN  # exact frame index
            radioactive.tStart = t  # local t and not account for scr refresh
            radioactive.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(radioactive, 'tStartRefresh')  # time at next scr refresh
            radioactive.setAutoDraw(True)
        if radioactive.status == STARTED:
            if frameN >= (radioactive.frameNStart + nFrames):
                # keep track of stop time/frame for later
                radioactive.tStop = t  # not accounting for scr refresh
                radioactive.frameNStop = frameN  # exact frame index
                win.timeOnFlip(radioactive, 'tStopRefresh')  # time at next scr refresh
                radioactive.setAutoDraw(False)
        # we want to present the tone every
        # X seconds for the duration of the trial
        # if the sound is not currently playing
        
        if phaseN > 0:
            iFrame = iFrame +1
            if not toneIsPlaying and not toneIsWaiting:
                # pick how long we will wait for
                if lastTone == 1:
                    thisISI = isi1-2 
                    # this is in frames
                    # we correct for 2 frames as wait a little longer
                    # before stopping the tone (see below)
                else:
                    thisISI = isi2-2
                #print('thisISI', thisISI)
                ISIs.append(thisISI)
                thisOnset = iFrame +thisISI
                #we are waiting for the sound to play
                toneIsWaiting = True
                toneTrig = 0
            elif not toneIsPlaying and toneIsWaiting:
                if iFrame >= thisOnset:
                    #getTone()
                    print('playing')
                    if toneCurr == "1":
                        tone1.play()
                        toneTrig = triggers['tone_1']
                        lastTone = 1
                    elif toneCurr == "2":
                        tone2.play()
                        toneTrig = triggers['tone_2']
                        lastTone = 2
                    toneOnsets.append(iFrame)
                    send_trigger(toneTrig)
                    toneIsPlaying = True
                    toneIsWaiting = False
            elif toneIsPlaying:
                toneTrig = 0
                if toneCurr == "1":
                    if iFrame >= thisOnset + tone1.secs*screen_refreshRate +1:
                        toneEndFrame = iFrame
                        if toneIndex < nTones:
                            toneIndex += 1
                            print('tone number:')
                            print(toneIndex)
                            toneCurr = toneStream_np[toneIndex]
                            tone1.stop()
                            toneIsPlaying = False
                        else:
                            # we have reached the end of the tone list
                            tone1.stop()
                            continueRoutine = False
                elif toneCurr == "2":
                    if iFrame >= thisOnset + tone2.secs*screen_refreshRate +1:
                        toneEndFrame = iFrame
                        if toneIndex < nTones:
                            toneIndex += 1
                            print('tone number:')
                            print(toneIndex)
                            toneCurr = toneStream_np[toneIndex]
                            tone2.stop()
                            toneIsPlaying = False
                        else:
                            tone2.stop()
                            continueRoutine = False
        
            # end the routine if the trial duration has been reached
            if currentFrame > nFrames:
                toneIsPlaying = False
                toneIsWaiting = False
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    totalReward_tot = totalReward_tot + totalReward;
    totalReward_text = "£%.2f" %(totalReward);
    
    # save the output data for this block
    np.savetxt(saveFilename,saveData,delimiter=",",fmt="%s")
    #win.callOnFlip(trialTrigger.setData, int(0))
    triggerValue = 0;
    send_trigger(triggerValue)
    sendTrigger = False;
    blocks.addData('harmless_area.started', harmless_area.tStartRefresh)
    blocks.addData('harmless_area.stopped', harmless_area.tStopRefresh)
    blocks.addData('shield.started', shield.tStartRefresh)
    blocks.addData('shield.stopped', shield.tStopRefresh)
    blocks.addData('shield_centre.started', shield_centre.tStartRefresh)
    blocks.addData('shield_centre.stopped', shield_centre.tStopRefresh)
    blocks.addData('shield_bg_short.started', shield_bg_short.tStartRefresh)
    blocks.addData('shield_bg_short.stopped', shield_bg_short.tStopRefresh)
    blocks.addData('laser.started', laser.tStartRefresh)
    blocks.addData('laser.stopped', laser.tStopRefresh)
    blocks.addData('laser_long.started', laser_long.tStartRefresh)
    blocks.addData('laser_long.stopped', laser_long.tStopRefresh)
    blocks.addData('progress_bar.started', progress_bar.tStartRefresh)
    blocks.addData('progress_bar.stopped', progress_bar.tStopRefresh)
    blocks.addData('radioactive.started', radioactive.tStartRefresh)
    blocks.addData('radioactive.stopped', radioactive.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blockEndText"-------
    continueRoutine = True
    # update component parameters for each repeat
    rewardFeedback = "£%.2f" %(totalReward)
    textReward.setText(rewardFeedback)
    key_resp_blockEnd.keys = []
    key_resp_blockEnd.rt = []
    _key_resp_blockEnd_allKeys = []
    # keep track of which components have finished
    blockEndTextComponents = [textPause, textReward, textContinue, key_resp_blockEnd]
    for thisComponent in blockEndTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockEndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blockEndText"-------
    while continueRoutine:
        # get current time
        t = blockEndTextClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockEndTextClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPause* updates
        if textPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textPause.frameNStart = frameN  # exact frame index
            textPause.tStart = t  # local t and not account for scr refresh
            textPause.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textPause, 'tStartRefresh')  # time at next scr refresh
            textPause.setAutoDraw(True)
        if textPause.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textPause.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textPause.tStop = t  # not accounting for scr refresh
                textPause.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textPause, 'tStopRefresh')  # time at next scr refresh
                textPause.setAutoDraw(False)
        
        # *textReward* updates
        if textReward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textReward.frameNStart = frameN  # exact frame index
            textReward.tStart = t  # local t and not account for scr refresh
            textReward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textReward, 'tStartRefresh')  # time at next scr refresh
            textReward.setAutoDraw(True)
        if textReward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textReward.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textReward.tStop = t  # not accounting for scr refresh
                textReward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textReward, 'tStopRefresh')  # time at next scr refresh
                textReward.setAutoDraw(False)
        
        # *textContinue* updates
        if textContinue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            textContinue.frameNStart = frameN  # exact frame index
            textContinue.tStart = t  # local t and not account for scr refresh
            textContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textContinue, 'tStartRefresh')  # time at next scr refresh
            textContinue.setAutoDraw(True)
        
        # *key_resp_blockEnd* updates
        waitOnFlip = False
        if key_resp_blockEnd.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_blockEnd.frameNStart = frameN  # exact frame index
            key_resp_blockEnd.tStart = t  # local t and not account for scr refresh
            key_resp_blockEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_blockEnd, 'tStartRefresh')  # time at next scr refresh
            key_resp_blockEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_blockEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_blockEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_blockEnd.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_blockEnd.getKeys(keyList=None, waitRelease=False)
            _key_resp_blockEnd_allKeys.extend(theseKeys)
            if len(_key_resp_blockEnd_allKeys):
                key_resp_blockEnd.keys = _key_resp_blockEnd_allKeys[-1].name  # just the last key pressed
                key_resp_blockEnd.rt = _key_resp_blockEnd_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockEndTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockEndText"-------
    for thisComponent in blockEndTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('textPause.started', textPause.tStartRefresh)
    blocks.addData('textPause.stopped', textPause.tStopRefresh)
    blocks.addData('textReward.started', textReward.tStartRefresh)
    blocks.addData('textReward.stopped', textReward.tStopRefresh)
    blocks.addData('textContinue.started', textContinue.tStartRefresh)
    blocks.addData('textContinue.stopped', textContinue.tStopRefresh)
    # check responses
    if key_resp_blockEnd.keys in ['', [], None]:  # No response was made
        key_resp_blockEnd.keys = None
    blocks.addData('key_resp_blockEnd.keys',key_resp_blockEnd.keys)
    if key_resp_blockEnd.keys != None:  # we had a response
        blocks.addData('key_resp_blockEnd.rt', key_resp_blockEnd.rt)
    blocks.addData('key_resp_blockEnd.started', key_resp_blockEnd.tStartRefresh)
    blocks.addData('key_resp_blockEnd.stopped', key_resp_blockEnd.tStopRefresh)
    # the Routine "blockEndText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


# ------Prepare to start Routine "sessionEndText"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
totRew_text = "£%.2f" %(totalReward_tot);
finalReward_text.setText(totRew_text)
# keep track of which components have finished
sessionEndTextComponents = [textEndSession, finalReward_text]
for thisComponent in sessionEndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sessionEndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sessionEndText"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sessionEndTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sessionEndTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndSession* updates
    if textEndSession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndSession.frameNStart = frameN  # exact frame index
        textEndSession.tStart = t  # local t and not account for scr refresh
        textEndSession.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndSession, 'tStartRefresh')  # time at next scr refresh
        textEndSession.setAutoDraw(True)
    if textEndSession.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndSession.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            textEndSession.tStop = t  # not accounting for scr refresh
            textEndSession.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEndSession, 'tStopRefresh')  # time at next scr refresh
            textEndSession.setAutoDraw(False)
    
    # *finalReward_text* updates
    if finalReward_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalReward_text.frameNStart = frameN  # exact frame index
        finalReward_text.tStart = t  # local t and not account for scr refresh
        finalReward_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalReward_text, 'tStartRefresh')  # time at next scr refresh
        finalReward_text.setAutoDraw(True)
    if finalReward_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finalReward_text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            finalReward_text.tStop = t  # not accounting for scr refresh
            finalReward_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finalReward_text, 'tStopRefresh')  # time at next scr refresh
            finalReward_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sessionEndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sessionEndText"-------
for thisComponent in sessionEndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEndSession.started', textEndSession.tStartRefresh)
thisExp.addData('textEndSession.stopped', textEndSession.tStopRefresh)
thisExp.addData('finalReward_text.started', finalReward_text.tStartRefresh)
thisExp.addData('finalReward_text.stopped', finalReward_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
