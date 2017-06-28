# =======================================================================
# Program Name: python_player_piano.py
#        Title: Python Player Piano
#       Author: Mark Stramaglia (markstramaglia@gmail.com)
#         Date: June 27, 2017
#      Purpose: Having some fun with the Python winsound module,
#               creating music with beeps!
# =======================================================================

# The winsound module is part of the standard Python library,
# and provides Python access to sound-playing functionality in Windows OS.
# Reference: https://docs.python.org/2/library/winsound.html
import winsound

# winsound.Beep(frequency, duration)
# winsound function that plays a beep sound on the PC's speakers.
# frequency specifies the frequency in hertz for the beep sound (range 37 through 32767).
# duration specifies the duration in milliseconds that the sound should last.

# BEGIN FUNCTION playNote ----------------------------------------------
# The playNote function accepts a note, octave, and noteValue as an input parameters, and makes
# a beep sound at the appropriate frequency for that note for the appropriate duration.
# 
def playNote(note, octave, noteValue):

    # Set duration of beep based on noteValue
    duration = 0
    if noteValue == '1/8':
        duration = 250
    elif noteValue == '1/4':
        duration = 500
    elif noteValue == '1/2':
        duration = 1000
    elif noteValue == '1':
        duration = 2000

    # Play sound at appropriate frequency based on note and octave
    if note == 'A':
        if octave == 3:
            winsound.Beep(220, duration)
        elif octave == 4:
            winsound.Beep(440, duration)
        elif octave == 5:
            winsound.Beep(880, duration)
    elif note == 'B':
        if octave == 3:
            winsound.Beep(246, duration)
        elif octave == 4:
            winsound.Beep(493, duration)
        elif octave == 5:
            winsound.Beep(987, duration)
    elif note == 'C':
        if octave == 3:
            winsound.Beep(130, duration)
        elif octave == 4:
            winsound.Beep(261, duration)
        elif octave == 5:
            winsound.Beep(523, duration)
    elif note == 'D':
        if octave == 3:
            winsound.Beep(146, duration)
        elif octave == 4:
            winsound.Beep(293, duration)
        elif octave == 5:
            winsound.Beep(587, duration)
    elif note == 'E':
        if octave == 3:
            winsound.Beep(164, duration)
        elif octave == 4:
            winsound.Beep(329, duration)
        elif octave == 5:
            winsound.Beep(659, duration)
    elif note == 'F':
        if octave == 3:
            winsound.Beep(174, duration)
        elif octave == 4:
            winsound.Beep(349, duration)
        elif octave == 5:
            winsound.Beep(698, duration)
    elif note == 'G':
        if octave == 3:
            winsound.Beep(195, duration)
        elif octave == 4:
            winsound.Beep(391, duration)
        elif octave == 5:
            winsound.Beep(783, duration)
# END FUNCTION playNote ------------------------------------------------

# BEGIN PROGRAM --------------------------------------------------------
# Play Twinkle Twinkle Little Star
playNote('C',4,'1/4')
playNote('C',4,'1/4')
playNote('G',4,'1/4')
playNote('G',4,'1/4')
playNote('A',4,'1/4')
playNote('A',4,'1/4')
playNote('G',4,'1/2')
playNote('F',4,'1/4')
playNote('F',4,'1/4')
playNote('E',4,'1/4')
playNote('E',4,'1/4')
playNote('D',4,'1/4')
playNote('D',4,'1/4')
playNote('C',4,'1/2')
# END PROGRAM ----------------------------------------------------------
