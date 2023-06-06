function design = varJumpDesign
%VARJUMPDESIGN A rotation task design for generating jumps in stimulus
%standard deviation.

design.blockTypes = {'lowNoise', 'highNoise'};

% What varies across blocks
% Block type 1: more low noise
design.blocks(1).noiseValueSet = [10 10 20 30];

% Block type 2: more middle noise
design.blocks(2).noiseValueSet = [10 20 20 30];

% What stays constant over blocks
for blockType = 1:2
    design.blocks(blockType).noiseDurMeanStdMinMax = [10 3 5 15]; % in s
end

end