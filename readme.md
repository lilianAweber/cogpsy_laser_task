# Save the world game

This task is written in PsychoPy. It has been developed in PsychoPy Builder v2022.1.2 to run on the stimulus PC in the MEG laboratory at OHBA.

The subject aims to manoeuvre a "shield" around a circle to catch as many 'radiation beams' emitted from a radioactice source as possible. This requires the subject to estimate the current mean of the generative distribution of the beams, and place their shield as close as possible to this mean. They can adjust the shield location using the '1' and '2' keys on the button box. In this task version, they width of their shield is fixed, and the noise around the mean angle of emission is constant. They encounter two different sources which only differ in their volatility (i.e., how often the generative mean of their beam distributions changes over time).

# Stimulus sequences and counterbalancing

This task has one short practice block (1min) and 4 main task blocks (3min each). For every block, the sequence of beam positions is read from a block-specific .csv file. The order of these blocks is determined by a session .csv file. All of these files are pre-generated and located in the folder 'sequences'. The code for generating these sequences is in the subfolder 'stimgen' (written in Matlab). 

There are 4 different sessions available: orders 1 and 2 start with a stable block, orders 3 and 4 start with a volatile block. In orders 1 and 3, the volatile blocks correspond to the red source image; in orders 2 and 4, they correspond to the blue source image (and vice versa). At the beginning of the experiment, the experimenter will be prompted for the participant ID, the session number and the order. This can be used to counterbalance the order of volatile/stable and the assignment of colours to stability levels across participants.

# MEG triggers

Per default, the triggers are activated. If the task is to run on a laptop or without connection to the trigger port in the OHBA MEG lab, the triggers can be deactivated. Two steps are required for this: 1. The variable "send_trigger" in the code needs to be set to False. This is in one of the first lines of code. In PsychoPy builder view, select the first routine ('instructions_game') and within that the "code_start" component. 2. The trigger components in the 'instructions_game', 'practiceBlock', 'blockStartText', 'trial', 'blockEndText', and 'sessionEndText' need to be deactivated. For that, select the component and in the tab 'Testing' choose 'Disable component'. 

# Background MMN

During the 4 main blocks of the experiment, participants will hear tones that implement a duration MMN. There are two tones, both with pitch 440 Hz: one long tone (100ms) and one short tone (50ms). In stable blocks, one of the two will be the deviant (will occur with probability 0.15). In volatile blocks, the roles of standard and deviant will occasionally switch. Volatility of tone sequences will correspond to the condition in the main task. 

# Changing the code

Most changes (like file naming & paths, trigger values, general settings) can be implemented by changing the code in the "code_start" component of the "instructions_game" routine. For questions or further changes contact lilian.weber@psych.ox.ac.uk.

