function stim = generateBlockStimulus( stim, session, noise )
%GENERATEBLOCKSTIMULUS Generates a continuous stimulus for a rotating laser, 
%where values are drawn from a normal distribution with stdev 'noise' around a 
%changing mean, and durations of constant epochs are drawn from an
%exponential function.

stim.values = [];
stim.durations = [];
stim.valueVector = [];
for iEpoch = 1: numel(stim.meanValues)

    [valVec, values, nSamplesJumps] = generateValueVec(...
        stim.meanDurations(iEpoch), ...
        session.jumpDuration.mean, session.jumpDuration.min, ...
        session.jumpDuration.max, stim.meanValues(iEpoch), ...
        noise);

    stim.values = [stim.values; round(values)];
    stim.durations = [stim.durations nSamplesJumps./session.sampleRate];
    stim.valueVector = [stim.valueVector; round(valVec)];
end

% use circle degrees for the final stimulus
stim.valuesDeg = mod(stim.values, 360);
stim.valueVectorDeg = mod(stim.valueVector, 360);

end