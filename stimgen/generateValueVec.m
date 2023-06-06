function [ valVec, values, durations ] = generateValueVec( nFrames, meanDur, minDur, ...
    maxDur, meanVal, sdVal )
%GENERATEVALUEVEC This function generates a vector of values by
%drawing values from a normal distribution and drawing the
%durations of each value from a truncated exponential function.
%   IN:     nFrames     - total number of frames (length of vector) to fill
%           meanDur     - mean duration for exponential function
%           minDur      - minimum duration for truncating exp function
%           maxDur      - maximum duration for truncating exp function
%           meanCoh     - mean value for normal distribution
%           sdCoh       - standard deviation for normal distribution

%=== Draw durations from exponential distribution
frames = 0; 
durCount = 0;
while  frames < nFrames
    durCount = durCount + 1;
    % draw a new duration
    durations(durCount) = round(exprnd(meanDur));
    % truncate: only allow durations between minDur and maxDur
    while durations(durCount) < minDur || durations(durCount) > maxDur
        durations(durCount) = round(exprnd(meanDur));
    end
    % count how many frames we've covered
    frames = frames + durations(durCount);
end

%=== Draw coherence values from normal distribution
valVec = zeros(sum(durations), 1);
values = NaN(durCount, 1);
periodStart = 1;
for iEpoch = 1 : length(durations)
    % draw a new value
    newValue =  sdVal .* randn(1,1) + meanVal;
    % save in values
    values(iEpoch) = newValue;
    % fill all frames belonging to this period with this value
    valVec(periodStart : periodStart + (durations(iEpoch)-1)) ...
        = newValue .* ones(durations(iEpoch), 1);
    % start time of next period
    periodStart = periodStart + durations(iEpoch);
end

% discard all coherences after last frame
valVec = valVec(1: nFrames);
durations(durCount) = durations(durCount) - (sum(durations) - nFrames);
end

