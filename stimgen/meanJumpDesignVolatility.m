function design = meanJumpDesignVolatility
%MEANJUMPDESIGNVOLATILITY A task design with a manipulation of mean
%jump probability ("volatility").

design.blockTypes = {'stable', 'volatile'};

% What varies across blocks: change probability
% Block type 1: slow changes
design.blocks(1).durMeanStdMinMax = [15 1.5 8 18];

% Block type 2: fast changes 
design.blocks(2).durMeanStdMinMax = [5 1.5 2 8];

% What stays constant over blocks
for blockType = 1:2
    % Mean of the noise (standard deviation)
    design.blocks(blockType).noiseMean = 20;
    % Jump sizes (in mean SD of noise) that can occur (change magnitude)
    design.blocks(blockType).jumpValueSet = [-3 -2 -1.5 -1 -0.5 0.5 1 1.5 2 3]; % in SD of stimulus
end

end