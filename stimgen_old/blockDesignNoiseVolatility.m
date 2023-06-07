function design = blockDesignNoiseVolatility
%BLOCKDESIGNNOISEVOLATILITY A rotation task design with a 2x2 manipulation of 
%mean jump probability ("volatility") and noise around the mean ("stochasticity").

design.blockTypes = {'lowNoiseStable', 'lowNoiseVolatile', 'highNoiseStable', 'highNoiseVolatile'};

% What varies across blocks
% Block type 1: low noise, slow changes
design.blocks(1).noise = 15;
design.blocks(1).durMeanStdMinMax = [10 1.5 7 15]; % in s

% Block type 2: low noise, fast changes 
design.blocks(2).noise = 15;
design.blocks(2).durMeanStdMinMax = [5 1.5 2 10];

% Block type 2: high noise, slow changes
design.blocks(3).noise = 30;
design.blocks(3).durMeanStdMinMax = [10 1.5 7 15];

% Block type 4: high noise, fast changes
design.blocks(4).noise = 30;
design.blocks(4).durMeanStdMinMax = [5 1.5 2 10];

% What stays constant over blocks
for blockType = 1:4
    % Value: proportion (rew/pun)
    design.blocks(blockType).jumpValueSet = [-5 -2.5 -2 -1 1 2 2.5 5]; % in SD of stimulus
end

end