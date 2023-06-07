function design = designVolatility
%DESIGNVOLATILITY A task design with a manipulation of mean
%jump probability ("volatility").

design.blockTypes = {'stable', 'volatile', 'medium'};

% What varies across blocks: change probability
% Block type 1: slow changes
design.blocks(1).durMeanStdMinMax = [10 1.5 8 15];
% Mean of the noise (standard deviation)
design.blocks(1).noiseStd = 15;

% Block type 2: fast changes
design.blocks(2).durMeanStdMinMax = [3 1.5 2 6];
% Mean of the noise (standard deviation)
design.blocks(2).noiseStd = 15;

% Block type 3: intermediate
design.blocks(3).durMeanStdMinMax = [5 1.5 3 12];
% Mean of the noise (standard deviation)
design.blocks(3).noiseStd = 10;

% What stays constant over blocks
for blockType = 1:numel(design.blocks)
    % Jump sizes (in mean SD of noise) that can occur (change magnitude)
    %design.blocks(blockType).jumpValueSet = [-3 -2 -1 1 2 3]; % in SD
    design.blocks(blockType).jumpValueSet = [-45 -30 -15 15 30 45]; % in deg
end

end