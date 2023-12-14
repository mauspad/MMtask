#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on November 07, 2023, at 21:10
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'MM_scan'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'run': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Silver\\Box\\psychopy_git_masters\\MM_task\\MM_scan.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color='0.3255, 0.3255, 0.3255', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = '0.3255, 0.3255, 0.3255'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "wait" ---
    trigger = keyboard.Keyboard()
    text = visual.TextStim(win=win, name='text',
        text="wait for 'o' trigger from scanner",
        font='Arial',
        pos=(0, 0), height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "run_in" ---
    runin_fix = visual.ShapeStim(
        win=win, name='runin_fix', vertices='cross',
        size=(50,50),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-1.0, interpolate=True)
    runin_testing_text = visual.TextStim(win=win, name='runin_testing_text',
        text='',
        font='Arial',
        pos=(0, -200), height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "visualcue" ---
    # Run 'Begin Experiment' code from code_startpump
    ##import stuff
    #import serial
    #import time
    
    ##open serial port
    #ser = serial.Serial(port='COM4', baudrate=19200, bytesize=8)
    
    ##pump order:
    ##0 - water1
    ##1 - water2
    ##2 - chocolate milk
    ##3 - strawberry milk
    visual_cue = visual.ImageStim(
        win=win,
        name='visual_cue', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(200, 200),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "postCueWait" ---
    postcuewait = visual.ShapeStim(
        win=win, name='postcuewait', vertices='cross',
        size=(50,50),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-1.0, interpolate=True)
    postcuewait_testing_text = visual.TextStim(win=win, name='postcuewait_testing_text',
        text='postcue wait 2s',
        font='Arial',
        pos=(0, -200), height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "taste_delivery" ---
    taste_delivery_fixation = visual.ShapeStim(
        win=win, name='taste_delivery_fixation', vertices='cross',
        size=(50,50),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-1.0, interpolate=True)
    taste_testing_delivery_text = visual.TextStim(win=win, name='taste_testing_delivery_text',
        text='',
        font='Arial',
        pos=(0, -200), height=40, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "pre_rinse_wait" ---
    rinsewait = visual.ShapeStim(
        win=win, name='rinsewait', vertices='cross',
        size=(50, 50),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-1.0, interpolate=True)
    rinse_testing_wait_text = visual.TextStim(win=win, name='rinse_testing_wait_text',
        text='pre-rinse wait 1s',
        font='Arial',
        pos=(0, -200), height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "rinse_delivery" ---
    rinse_delivery_fixation = visual.ShapeStim(
        win=win, name='rinse_delivery_fixation', vertices='cross',
        size=(50, 50),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-1.0, interpolate=True)
    rinse_testing_delivery_text = visual.TextStim(win=win, name='rinse_testing_delivery_text',
        text='',
        font='Arial',
        pos=(0, -200), height=40, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Jitter" ---
    jitter_fix = visual.ShapeStim(
        win=win, name='jitter_fix', vertices='cross',
        size=(50,50),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=1, depth=-1.0, interpolate=True)
    jitter_testing_text = visual.TextStim(win=win, name='jitter_testing_text',
        text='',
        font='Arial',
        pos=(0, -200), height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "end" ---
    end_task_trigger = keyboard.Keyboard()
    end_task = visual.TextStim(win=win, name='end_task',
        text='You have completed this scan :)',
        font='Arial',
        pos=(0, 0), height=30, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "wait" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from mouse_hide
    ##start and hide mouse
    mouse = event.Mouse(visible=False)
    trigger.keys = []
    trigger.rt = []
    _trigger_allKeys = []
    # keep track of which components have finished
    waitComponents = [trigger, text]
    for thisComponent in waitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wait" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trigger* updates
        waitOnFlip = False
        
        # if trigger is starting this frame...
        if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trigger.frameNStart = frameN  # exact frame index
            trigger.tStart = t  # local t and not account for scr refresh
            trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trigger.started')
            # update status
            trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trigger.status == STARTED and not waitOnFlip:
            theseKeys = trigger.getKeys(keyList=['o'], ignoreKeys=["escape"], waitRelease=False)
            _trigger_allKeys.extend(theseKeys)
            if len(_trigger_allKeys):
                trigger.keys = _trigger_allKeys[0].name  # just the first key pressed
                trigger.rt = _trigger_allKeys[0].rt
                trigger.duration = _trigger_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wait" ---
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trigger.keys in ['', [], None]:  # No response was made
        trigger.keys = None
    thisExp.addData('trigger.keys',trigger.keys)
    if trigger.keys != None:  # we had a response
        thisExp.addData('trigger.rt', trigger.rt)
        thisExp.addData('trigger.duration', trigger.duration)
    thisExp.nextEntry()
    # the Routine "wait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "run_in" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from runin_mouse
    ##hide mouse
    mouse = event.Mouse(visible=False)
    runin_testing_text.setText('run-in 8s')
    # keep track of which components have finished
    run_inComponents = [runin_fix, runin_testing_text]
    for thisComponent in run_inComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "run_in" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *runin_fix* updates
        
        # if runin_fix is starting this frame...
        if runin_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            runin_fix.frameNStart = frameN  # exact frame index
            runin_fix.tStart = t  # local t and not account for scr refresh
            runin_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(runin_fix, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'runin_fix.started')
            # update status
            runin_fix.status = STARTED
            runin_fix.setAutoDraw(True)
        
        # if runin_fix is active this frame...
        if runin_fix.status == STARTED:
            # update params
            pass
        
        # if runin_fix is stopping this frame...
        if runin_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > runin_fix.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                runin_fix.tStop = t  # not accounting for scr refresh
                runin_fix.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'runin_fix.stopped')
                # update status
                runin_fix.status = FINISHED
                runin_fix.setAutoDraw(False)
        
        # *runin_testing_text* updates
        
        # if runin_testing_text is starting this frame...
        if runin_testing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            runin_testing_text.frameNStart = frameN  # exact frame index
            runin_testing_text.tStart = t  # local t and not account for scr refresh
            runin_testing_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(runin_testing_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            runin_testing_text.status = STARTED
            runin_testing_text.setAutoDraw(True)
        
        # if runin_testing_text is active this frame...
        if runin_testing_text.status == STARTED:
            # update params
            pass
        
        # if runin_testing_text is stopping this frame...
        if runin_testing_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > runin_testing_text.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                runin_testing_text.tStop = t  # not accounting for scr refresh
                runin_testing_text.frameNStop = frameN  # exact frame index
                # update status
                runin_testing_text.status = FINISHED
                runin_testing_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_inComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "run_in" ---
    for thisComponent in run_inComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('eventtype.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "visualcue" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_startpump
        ##hide mouse
        mouse = event.Mouse(visible=False)
        visual_cue.setImage(imgpath)
        # keep track of which components have finished
        visualcueComponents = [visual_cue]
        for thisComponent in visualcueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "visualcue" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *visual_cue* updates
            
            # if visual_cue is starting this frame...
            if visual_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                visual_cue.frameNStart = frameN  # exact frame index
                visual_cue.tStart = t  # local t and not account for scr refresh
                visual_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(visual_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'visual_cue.started')
                # update status
                visual_cue.status = STARTED
                visual_cue.setAutoDraw(True)
            
            # if visual_cue is active this frame...
            if visual_cue.status == STARTED:
                # update params
                pass
            
            # if visual_cue is stopping this frame...
            if visual_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > visual_cue.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    visual_cue.tStop = t  # not accounting for scr refresh
                    visual_cue.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'visual_cue.stopped')
                    # update status
                    visual_cue.status = FINISHED
                    visual_cue.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in visualcueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "visualcue" ---
        for thisComponent in visualcueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "postCueWait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from postcue_mouse
        ##start and hide mouse
        mouse = event.Mouse(visible=False)
        # keep track of which components have finished
        postCueWaitComponents = [postcuewait, postcuewait_testing_text]
        for thisComponent in postCueWaitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "postCueWait" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *postcuewait* updates
            
            # if postcuewait is starting this frame...
            if postcuewait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                postcuewait.frameNStart = frameN  # exact frame index
                postcuewait.tStart = t  # local t and not account for scr refresh
                postcuewait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(postcuewait, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postcuewait.started')
                # update status
                postcuewait.status = STARTED
                postcuewait.setAutoDraw(True)
            
            # if postcuewait is active this frame...
            if postcuewait.status == STARTED:
                # update params
                pass
            
            # if postcuewait is stopping this frame...
            if postcuewait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > postcuewait.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    postcuewait.tStop = t  # not accounting for scr refresh
                    postcuewait.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'postcuewait.stopped')
                    # update status
                    postcuewait.status = FINISHED
                    postcuewait.setAutoDraw(False)
            
            # *postcuewait_testing_text* updates
            
            # if postcuewait_testing_text is starting this frame...
            if postcuewait_testing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                postcuewait_testing_text.frameNStart = frameN  # exact frame index
                postcuewait_testing_text.tStart = t  # local t and not account for scr refresh
                postcuewait_testing_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(postcuewait_testing_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                postcuewait_testing_text.status = STARTED
                postcuewait_testing_text.setAutoDraw(True)
            
            # if postcuewait_testing_text is active this frame...
            if postcuewait_testing_text.status == STARTED:
                # update params
                pass
            
            # if postcuewait_testing_text is stopping this frame...
            if postcuewait_testing_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > postcuewait_testing_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    postcuewait_testing_text.tStop = t  # not accounting for scr refresh
                    postcuewait_testing_text.frameNStop = frameN  # exact frame index
                    # update status
                    postcuewait_testing_text.status = FINISHED
                    postcuewait_testing_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in postCueWaitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "postCueWait" ---
        for thisComponent in postCueWaitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "taste_delivery" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from tastedelivery_code
        ##start and hide mouse
        mouse = event.Mouse(visible=False)
        
        #if eventtype == 'water1': #if water1
        #    ser.write(("0run\r").encode()) #trigger pump 1
        #elif eventtype == 'water2': #if water2
        #    ser.write(("1run\r").encode()) #trigger pump 2
        #elif eventtype == 'milkchoc': #if chocolate
        #    ser.write(("2run\r").encode()) #trigger pump 3
        #elif eventtype == 'milkstraw': #if strawberry
        #    ser.write(("3run\r").encode()) #trigger pump 4
        taste_testing_delivery_text.setText(eventtype + " delivery 11s")
        # keep track of which components have finished
        taste_deliveryComponents = [taste_delivery_fixation, taste_testing_delivery_text]
        for thisComponent in taste_deliveryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "taste_delivery" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 11.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *taste_delivery_fixation* updates
            
            # if taste_delivery_fixation is starting this frame...
            if taste_delivery_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taste_delivery_fixation.frameNStart = frameN  # exact frame index
                taste_delivery_fixation.tStart = t  # local t and not account for scr refresh
                taste_delivery_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taste_delivery_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'taste_delivery_fixation.started')
                # update status
                taste_delivery_fixation.status = STARTED
                taste_delivery_fixation.setAutoDraw(True)
            
            # if taste_delivery_fixation is active this frame...
            if taste_delivery_fixation.status == STARTED:
                # update params
                pass
            
            # if taste_delivery_fixation is stopping this frame...
            if taste_delivery_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taste_delivery_fixation.tStartRefresh + 11-frameTolerance:
                    # keep track of stop time/frame for later
                    taste_delivery_fixation.tStop = t  # not accounting for scr refresh
                    taste_delivery_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'taste_delivery_fixation.stopped')
                    # update status
                    taste_delivery_fixation.status = FINISHED
                    taste_delivery_fixation.setAutoDraw(False)
            
            # *taste_testing_delivery_text* updates
            
            # if taste_testing_delivery_text is starting this frame...
            if taste_testing_delivery_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                taste_testing_delivery_text.frameNStart = frameN  # exact frame index
                taste_testing_delivery_text.tStart = t  # local t and not account for scr refresh
                taste_testing_delivery_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(taste_testing_delivery_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                taste_testing_delivery_text.status = STARTED
                taste_testing_delivery_text.setAutoDraw(True)
            
            # if taste_testing_delivery_text is active this frame...
            if taste_testing_delivery_text.status == STARTED:
                # update params
                pass
            
            # if taste_testing_delivery_text is stopping this frame...
            if taste_testing_delivery_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > taste_testing_delivery_text.tStartRefresh + 11-frameTolerance:
                    # keep track of stop time/frame for later
                    taste_testing_delivery_text.tStop = t  # not accounting for scr refresh
                    taste_testing_delivery_text.frameNStop = frameN  # exact frame index
                    # update status
                    taste_testing_delivery_text.status = FINISHED
                    taste_testing_delivery_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in taste_deliveryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "taste_delivery" ---
        for thisComponent in taste_deliveryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-11.000000)
        
        # --- Prepare to start Routine "pre_rinse_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        ##hide mouse
        mouse = event.Mouse(visible=False)
        
        if rinse_deliver == 0: #if no rinse
            continueRoutine = False #skip routine
        # keep track of which components have finished
        pre_rinse_waitComponents = [rinsewait, rinse_testing_wait_text]
        for thisComponent in pre_rinse_waitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pre_rinse_wait" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rinsewait* updates
            
            # if rinsewait is starting this frame...
            if rinsewait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rinsewait.frameNStart = frameN  # exact frame index
                rinsewait.tStart = t  # local t and not account for scr refresh
                rinsewait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rinsewait, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rinsewait.started')
                # update status
                rinsewait.status = STARTED
                rinsewait.setAutoDraw(True)
            
            # if rinsewait is active this frame...
            if rinsewait.status == STARTED:
                # update params
                pass
            
            # if rinsewait is stopping this frame...
            if rinsewait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rinsewait.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rinsewait.tStop = t  # not accounting for scr refresh
                    rinsewait.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rinsewait.stopped')
                    # update status
                    rinsewait.status = FINISHED
                    rinsewait.setAutoDraw(False)
            
            # *rinse_testing_wait_text* updates
            
            # if rinse_testing_wait_text is starting this frame...
            if rinse_testing_wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rinse_testing_wait_text.frameNStart = frameN  # exact frame index
                rinse_testing_wait_text.tStart = t  # local t and not account for scr refresh
                rinse_testing_wait_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rinse_testing_wait_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                rinse_testing_wait_text.status = STARTED
                rinse_testing_wait_text.setAutoDraw(True)
            
            # if rinse_testing_wait_text is active this frame...
            if rinse_testing_wait_text.status == STARTED:
                # update params
                pass
            
            # if rinse_testing_wait_text is stopping this frame...
            if rinse_testing_wait_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rinse_testing_wait_text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rinse_testing_wait_text.tStop = t  # not accounting for scr refresh
                    rinse_testing_wait_text.frameNStop = frameN  # exact frame index
                    # update status
                    rinse_testing_wait_text.status = FINISHED
                    rinse_testing_wait_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pre_rinse_waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pre_rinse_wait" ---
        for thisComponent in pre_rinse_waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "rinse_delivery" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from rinsedelivery_code
        ##hide mouse
        mouse = event.Mouse(visible=False)
        
        if rinse_deliver == 0: #if no rinse
            continueRoutine = False #skip routine 
        #elif rinse_deliver == 1: #if there's a rinse
        #    ser.write(("1run\r").encode()) #trigger pump 2
        rinse_testing_delivery_text.setText('Rinse delivery')
        # keep track of which components have finished
        rinse_deliveryComponents = [rinse_delivery_fixation, rinse_testing_delivery_text]
        for thisComponent in rinse_deliveryComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "rinse_delivery" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rinse_delivery_fixation* updates
            
            # if rinse_delivery_fixation is starting this frame...
            if rinse_delivery_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rinse_delivery_fixation.frameNStart = frameN  # exact frame index
                rinse_delivery_fixation.tStart = t  # local t and not account for scr refresh
                rinse_delivery_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rinse_delivery_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rinse_delivery_fixation.started')
                # update status
                rinse_delivery_fixation.status = STARTED
                rinse_delivery_fixation.setAutoDraw(True)
            
            # if rinse_delivery_fixation is active this frame...
            if rinse_delivery_fixation.status == STARTED:
                # update params
                pass
            
            # if rinse_delivery_fixation is stopping this frame...
            if rinse_delivery_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rinse_delivery_fixation.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    rinse_delivery_fixation.tStop = t  # not accounting for scr refresh
                    rinse_delivery_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rinse_delivery_fixation.stopped')
                    # update status
                    rinse_delivery_fixation.status = FINISHED
                    rinse_delivery_fixation.setAutoDraw(False)
            
            # *rinse_testing_delivery_text* updates
            
            # if rinse_testing_delivery_text is starting this frame...
            if rinse_testing_delivery_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rinse_testing_delivery_text.frameNStart = frameN  # exact frame index
                rinse_testing_delivery_text.tStart = t  # local t and not account for scr refresh
                rinse_testing_delivery_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rinse_testing_delivery_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                rinse_testing_delivery_text.status = STARTED
                rinse_testing_delivery_text.setAutoDraw(True)
            
            # if rinse_testing_delivery_text is active this frame...
            if rinse_testing_delivery_text.status == STARTED:
                # update params
                pass
            
            # if rinse_testing_delivery_text is stopping this frame...
            if rinse_testing_delivery_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rinse_testing_delivery_text.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    rinse_testing_delivery_text.tStop = t  # not accounting for scr refresh
                    rinse_testing_delivery_text.frameNStop = frameN  # exact frame index
                    # update status
                    rinse_testing_delivery_text.status = FINISHED
                    rinse_testing_delivery_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rinse_deliveryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rinse_delivery" ---
        for thisComponent in rinse_deliveryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.500000)
        
        # --- Prepare to start Routine "Jitter" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from jitter_mouse
        ##hide mouse
        mouse = event.Mouse(visible=False)
        jitter_testing_text.setText('Jittered ISI')
        # keep track of which components have finished
        JitterComponents = [jitter_fix, jitter_testing_text]
        for thisComponent in JitterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Jitter" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *jitter_fix* updates
            
            # if jitter_fix is starting this frame...
            if jitter_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                jitter_fix.frameNStart = frameN  # exact frame index
                jitter_fix.tStart = t  # local t and not account for scr refresh
                jitter_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(jitter_fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jitter_fix.started')
                # update status
                jitter_fix.status = STARTED
                jitter_fix.setAutoDraw(True)
            
            # if jitter_fix is active this frame...
            if jitter_fix.status == STARTED:
                # update params
                pass
            
            # if jitter_fix is stopping this frame...
            if jitter_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > jitter_fix.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    jitter_fix.tStop = t  # not accounting for scr refresh
                    jitter_fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'jitter_fix.stopped')
                    # update status
                    jitter_fix.status = FINISHED
                    jitter_fix.setAutoDraw(False)
            
            # *jitter_testing_text* updates
            
            # if jitter_testing_text is starting this frame...
            if jitter_testing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                jitter_testing_text.frameNStart = frameN  # exact frame index
                jitter_testing_text.tStart = t  # local t and not account for scr refresh
                jitter_testing_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(jitter_testing_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                jitter_testing_text.status = STARTED
                jitter_testing_text.setAutoDraw(True)
            
            # if jitter_testing_text is active this frame...
            if jitter_testing_text.status == STARTED:
                # update params
                pass
            
            # if jitter_testing_text is stopping this frame...
            if jitter_testing_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > jitter_testing_text.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    jitter_testing_text.tStop = t  # not accounting for scr refresh
                    jitter_testing_text.frameNStop = frameN  # exact frame index
                    # update status
                    jitter_testing_text.status = FINISHED
                    jitter_testing_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in JitterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Jitter" ---
        for thisComponent in JitterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Jitter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trials'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    end_task_trigger.keys = []
    end_task_trigger.rt = []
    _end_task_trigger_allKeys = []
    # keep track of which components have finished
    endComponents = [end_task_trigger, end_task]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_task_trigger* updates
        waitOnFlip = False
        
        # if end_task_trigger is starting this frame...
        if end_task_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_task_trigger.frameNStart = frameN  # exact frame index
            end_task_trigger.tStart = t  # local t and not account for scr refresh
            end_task_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_task_trigger, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_task_trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_task_trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_task_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_task_trigger.status == STARTED and not waitOnFlip:
            theseKeys = end_task_trigger.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _end_task_trigger_allKeys.extend(theseKeys)
            if len(_end_task_trigger_allKeys):
                end_task_trigger.keys = _end_task_trigger_allKeys[-1].name  # just the last key pressed
                end_task_trigger.rt = _end_task_trigger_allKeys[-1].rt
                end_task_trigger.duration = _end_task_trigger_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *end_task* updates
        
        # if end_task is starting this frame...
        if end_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_task.frameNStart = frameN  # exact frame index
            end_task.tStart = t  # local t and not account for scr refresh
            end_task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_task, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_task.started')
            # update status
            end_task.status = STARTED
            end_task.setAutoDraw(True)
        
        # if end_task is active this frame...
        if end_task.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
