function session = generateTrainingSessionVaJump( sessionFileName )
%GENERATEMAINSESSION Generates a main experimental session for the continuous
%laser task with block-wise volatility and jumps in variance/noise.

if nargin < 1
    sessionFileName = 'test_session_training';
end

% Design choices
session.nBlocks = 4;
session.blockDuration = 2; % in min
session.blockSequence = {'lo', 'hi', 'lo', 'hi'};

% Settings
session.sampleRate = 60;
session.jumpDuration.mean = 0.3*session.sampleRate; % frames or samples (s*1/s)
session.jumpDuration.min = 0.1*session.sampleRate;
session.jumpDuration.max = 1*session.sampleRate;

% Generating stimulus stats
design = blockDesignVolatility;

%% Two variance-controlled blocks
session.blocks(1).blockType = 'lo';
session.blocks(1).volatility = 0;
session.blocks(1).duration = session.blockDuration*60;
% Generate a stimulus for blockType 1 (stable) - high precision
stdValues = 10;
noiseDurations = 120;
session.blocks(1).stim = generateMeanStimulusVaJumpTraining(session.blocks(1).duration, design.blocks(1), stdValues, noiseDurations, session.sampleRate);
session.blocks(1).stim = generateBlockStimulusVaJump(session.blocks(1).stim, session);

session.blocks(2).blockType = 'hi';
session.blocks(2).volatility = 1;
session.blocks(2).duration = session.blockDuration*60;
% Generate a stimulus for blockType 2 (volatile) - high precision
stdValues = 10;
noiseDurations = 120;
session.blocks(2).stim = generateMeanStimulusVaJumpTraining(session.blocks(2).duration, design.blocks(2), stdValues, noiseDurations, session.sampleRate);
session.blocks(2).stim = generateBlockStimulusVaJump(session.blocks(2).stim, session);

%% Two normal blocks
session.blocks(3).blockType = 'lo';
session.blocks(3).volatility = 0;
session.blocks(3).duration = session.blockDuration*60;
% Generate a stimulus for blockType 1 (stable) - changing precision
stdValues = [10 20 10 30 10 20];
noiseDurations = [20 20 20 20 20 20];
session.blocks(3).stim = generateMeanStimulusVaJumpTraining(session.blocks(3).duration, design.blocks(1), stdValues, noiseDurations, session.sampleRate);
session.blocks(3).stim = generateBlockStimulusVaJump(session.blocks(3).stim, session);

session.blocks(4).blockType = 'hi';
session.blocks(4).volatility = 1;
session.blocks(4).duration = session.blockDuration*60;
% Generate a stimulus for blockType 2 (volatile) - changing precision
stdValues = [10 20 10 30 10 20];
noiseDurations = [20 20 20 20 20 20];
session.blocks(4).stim = generateMeanStimulusVaJumpTraining(session.blocks(4).duration, design.blocks(2), stdValues, noiseDurations, session.sampleRate);
session.blocks(4).stim = generateBlockStimulusVaJump(session.blocks(4).stim, session);

%% Generate csv file for psychopy task
writeSessionToCsvFile(session, sessionFileName);
save([sessionFileName '.mat'], 'session');


end
