function session = generateMainSession
%GENERATEMAINSESSION Generates a main experimental session for the continuous
%laser task with block-wise volatility and stochasticity.

% Design choices
session.nBlocks = 12;
session.blockDuration = 2; % in min
session.blockSequence = {'ls', 'lv', 'hs', 'ls', 'lv', 'hv', 'hs', 'lv', 'hs', 'hv', 'ls', 'hv'};

% Settings
session.sampleRate = 60;
session.jumpDuration.mean = 0.3*session.sampleRate; % frames or samples
session.jumpDuration.min = 0.1*session.sampleRate;
session.jumpDuration.max = 1*session.sampleRate;

% Generating stimulus stats
design = blockDesignNoiseVolatility;

% Generate block stimuli
for iBlock = 1: session.nBlocks
    session.blocks(iBlock).blockType = session.blockSequence{iBlock};
    switch session.blocks(iBlock).blockType
        case 'ls'
            session.blocks(iBlock).noise = 0;
            session.blocks(iBlock).volatility = 0;
            session.blocks(iBlock).duration = session.blockDuration*60;
            % Generate a stimulus for blockType 1 (low noise, stable)
            session.blocks(iBlock).stim = generateMeanStimulus(session.blockDuration*60, design.blocks(1), session.sampleRate);
            session.blocks(iBlock).stim = generateBlockStimulus(session.blocks(iBlock).stim, session, design.blocks(1).noise);
        case 'lv'
            session.blocks(iBlock).noise = 0;
            session.blocks(iBlock).volatility = 1;
            session.blocks(iBlock).duration = session.blockDuration*60;
            % Generate a stimulus for blockType 2 (low noise, volatile)
            session.blocks(iBlock).stim = generateMeanStimulus(session.blockDuration*60, design.blocks(2), session.sampleRate);
            session.blocks(iBlock).stim = generateBlockStimulus(session.blocks(iBlock).stim, session, design.blocks(2).noise);
        case 'hs'
            session.blocks(iBlock).noise = 1;
            session.blocks(iBlock).volatility = 0;
            session.blocks(iBlock).duration = session.blockDuration*60;
            % Generate a stimulus for blockType 3 (high noise, stable)
            session.blocks(iBlock).stim = generateMeanStimulus(session.blockDuration*60, design.blocks(3), session.sampleRate);
            session.blocks(iBlock).stim = generateBlockStimulus(session.blocks(iBlock).stim, session, design.blocks(3).noise);
        case 'hv'
            session.blocks(iBlock).noise = 1;
            session.blocks(iBlock).volatility = 1;
            session.blocks(iBlock).duration = session.blockDuration*60;
            % Generate a stimulus for blockType 4 (high noise, volatile)
            session.blocks(iBlock).stim = generateMeanStimulus(session.blockDuration*60, design.blocks(4), session.sampleRate);
            session.blocks(iBlock).stim = generateBlockStimulus(session.blocks(iBlock).stim, session, design.blocks(4).noise);
    end
end


% Generate csv file for psychopy task
writeSessionToCsvFile(session, 'sess2');


end
