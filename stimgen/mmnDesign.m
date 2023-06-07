function design = mmnDesign( condition, deviantProbability )
%MMNDESIGN Defines a duration mismatch paradigm with switching
%standard/deviant roles and 3 possible deviant probabilities

design.tonePitch = 500; % in Hz
design.toneDuration1 = 50; % in ms
design.toneDuration2 = 125; % in ms
design.soaDuration = 450; % in ms
design.isiDuration1 = design.soaDuration - design.toneDuration1; % in ms
design.isiDuration2 = design.soaDuration - design.toneDuration2; % in ms

design.condition = condition;
design.devProb = deviantProbability;

switch design.devProb
    case 0.2
        design.distances = [3 4 4 5 5 6 6 7]; % possible train lengths of standards
        design.maxDevDiff = 5; % how many more or less deviants we accept per block
        design.blockDurations = 6:10; % how many deviants before a role switch
    case 0.1
        design.distances = [8 9 9 10 10 11 11 12];
        design.maxDevDiff = 3;
        design.blockDurations = 3:5;
    case 0.15
        design.distances = [4 5 6 6 7 7 8 9];%[8 9 9 10 10 11 11 12];
        design.maxDevDiff = 3;
        design.blockDurations = 5:8;
end

end