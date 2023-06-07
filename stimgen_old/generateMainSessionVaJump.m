function session = generateMainSessionVaJump( sessionFileName )
%GENERATEMAINSESSION Generates a main experimental session for the continuous
%laser task with block-wise volatility and jumps in variance/noise.

if nargin < 1
    sessionFileName = 'test_session';
end

% Design choices
session.nBlocks = 4;
session.blockDuration = 3; % in min
session.blockSequence = {'lo', 'lo', 'hi', 'hi'};

% Settings
session.sampleRate = 60;
session.jumpDuration.mean = 0.3*session.sampleRate; % frames or samples (s*1/s)
session.jumpDuration.min = 0.1*session.sampleRate;
session.jumpDuration.max = 1*session.sampleRate;

% Generating stimulus stats
designMean = meanJumpDesignVolatility;
designVar = varJumpDesign;

% Generate block stimuli
% We will generate one volatile and one stable sequence, then mix their
% variance jump schedules to have it counterbalanced.

% Generate two variance schedules (both with more low variance epochs)
stimVarOne = generateVarianceJumps(session.blockDuration*60, designVar.blocks(1), session.sampleRate);
stimVarTwo = generateVarianceJumps(session.blockDuration*60, designVar.blocks(1), session.sampleRate);

% Generate two stimulus streams for blockType 1 (stable) - they are the
% same except different starting points.
stimMeanStable1 = generateMeanJumps(session.blockDuration*60, designMean.blocks(1), session.sampleRate);
stimMeanStable2 = moveStartingPoint(stimMeanStable1);
stimStable1 = combineMeanAndVarianceJumps(stimMeanStable1, stimVarOne);
stimStable2 = combineMeanAndVarianceJumps(stimMeanStable2, stimVarTwo);

stimStable1 = generateBlockStimulusVaJump(stimStable1, session);
stimStable2 = generateBlockStimulusVaJump(stimStable2, session);

% Generate a stimulus for blockType 2 (volatile) - they are the
% same except different starting points.
stimMeanVolatile1 = generateMeanJumps(session.blockDuration*60, designMean.blocks(2), session.sampleRate);
stimMeanVolatile2 = moveStartingPoint(stimMeanVolatile1);
stimVolatile1 = combineMeanAndVarianceJumps(stimMeanVolatile1, stimVarOne);
stimVolatile2 = combineMeanAndVarianceJumps(stimMeanVolatile2, stimVarTwo);

stimVolatile1 = generateBlockStimulusVaJump(stimVolatile1, session);
stimVolatile2 = generateBlockStimulusVaJump(stimVolatile2, session);

for iBlock = 1: session.nBlocks
    session.blocks(iBlock).blockType = session.blockSequence{iBlock};
    switch session.blocks(iBlock).blockType
        case 'lo'
            session.blocks(iBlock).volatility = 0;
            session.blocks(iBlock).duration = session.blockDuration*60;
        case 'hi'
            session.blocks(iBlock).volatility = 1;
            session.blocks(iBlock).duration = session.blockDuration*60;
    end
end


session.blocks(1).stim = stimStable1;
session.blocks(2).stim = stimStable2;
session.blocks(3).stim = stimVolatile1;
session.blocks(4).stim = stimVolatile2;

% Generate csv file for psychopy task
writeSessionToCsvFile(session, sessionFileName);
save([sessionFileName '.mat'], 'session');


end
