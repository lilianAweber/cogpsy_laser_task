function session = generateLaserSessionPractice( blockSequence )
%GENERATELASERSESSIONPRACTICE Generates a practice session for the 
%continuous laser task with block-wise volatility manipulation.
%Task version: COGPSY study

if nargin < 1
    blockSequence = 3;
end

% Design choices
session.nBlocks = numel(blockSequence);
session.blockDuration = 1; % in min
session.design = designVolatility; % generating stimulus stats
session.blockSequence = blockSequence;
session.blockTypes = session.design.blockTypes;

% Settings
session.sampleRate = 60;
session.jumpDuration.mean = 0.3*session.sampleRate; % frames or samples (s*1/s)
session.jumpDuration.min = 0.1*session.sampleRate;
session.jumpDuration.max = 1*session.sampleRate;

for iBlock = 1: session.nBlocks
    % Generate block stimulus with noise
    blockID = session.blockSequence(iBlock);
    stim = generateMeanJumps(session.blockDuration*60, session.design.blocks(blockID), session.sampleRate);
    stim = generateBlockStimulus(stim, session, session.design.blocks(blockID).noiseStd);
    % Fill the block with stimulus and info
    session.blocks(iBlock).blockID = blockID;
    session.blocks(iBlock).blockType = session.blockTypes{blockID};
    session.blocks(iBlock).duration = session.blockDuration*60;
    session.blocks(iBlock).stim = stim;
end

end
