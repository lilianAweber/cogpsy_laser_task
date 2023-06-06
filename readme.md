# Save the world game

This task is written in PsychoPy. It has been developed in PsychoPy Builder v2022.1.2 to run on the stimulus PC in the MEG laboratory at OHBA.

The subject aims to manoeuvre a "shield" around a circle to catch as many 'radiation beams' emitted from a radioactice source as possible. This requires the subject to estimate the current mean of the generative distribution of the beams, and place their shield as close as possible to this mean. They can adjust the shield location using the '1' and '2' keys on the button box. In this task version, they width of their shield is fixed, and the noise around the mean angle of emission is constant. They encounter two different sources which only differ in their volatility (i.e., how often the generative mean of their beam distributions changes over time).

# Stimulus sequences and counterbalancing

This task has one short practice block (1min) and 4 main task blocks (3min each). For every block, the sequence of beam positions is read from a block-specific .csv file. The order of these blocks is determined by a session .csv file. All of these files are pre-generated and located in the folder 'sequences'. There are 4 different sessions available: orders 1 and 2 start with a stable block, orders 3 and 4 start with a volatile block. In orders 1 and 3, the volatile blocks correspond to the red source image; in orders 2 and 4, they correspond to the blue source image (and vice versa). At the beginning of the experiment, the experimenter will be prompted for the participant ID and the order. This can be used to counterbalance the order of volatile/stable and the assignment of colours to stability levels across participants.


