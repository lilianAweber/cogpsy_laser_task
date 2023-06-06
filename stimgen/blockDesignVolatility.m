function design = blockDesignVolatility
%BLOCKDESIGNVOLATILITY A rotation task design with a manipulation of mean
%jump probability ("volatility").

design.blockTypes = {'stable', 'volatile'};

% What varies across blocks
% Block type 1: slow changes
design.blocks(1).durMeanStdMinMax = [15 1.5 8 18]; % MORE STABLE

% Block type 2: fast changes 
design.blocks(2).durMeanStdMinMax = [5 1.5 2 8];

% What stays constant over blocks
for blockType = 1:2
    % Mean of the noise (standard deviation)
    design.blocks(blockType).noiseMean = 20;
    % Noise jump values & durations
    design.blocks(blockType).noiseValueSet = [10 10 20 30];
    %design.blocks(blockType).noiseDurMeanStdMinMax = design.blocks(blockType).durMeanStdMinMax;
    design.blocks(blockType).noiseDurMeanStdMinMax = [15 3 5 20]; % in s
    % Value: proportion (rew/pun)
    design.blocks(blockType).jumpValueSet = [-3 -2 -1.5 -1 -0.5 0.5 1 1.5 2 3]; % in SD of stimulus
end

end