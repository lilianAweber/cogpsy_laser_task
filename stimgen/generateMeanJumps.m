function stim = generateMeanJumps( totalSeconds, blockDesign, sampRate )
%GENERATEMEANJUMPS Generates a sequence of mean values based on the
%blockDesign for a duration of totalSeconds

% extract block design info
jumpValues = blockDesign.jumpValueSet;
%STD = blockDesign.noiseStd;
meanDur = blockDesign.durMeanStdMinMax(1)*sampRate;
stdDur = blockDesign.durMeanStdMinMax(2)*sampRate;
minDur = blockDesign.durMeanStdMinMax(3)*sampRate;
maxDur = blockDesign.durMeanStdMinMax(4)*sampRate;

nValues = numel(jumpValues);

% Generate mean values and durations
totalLength = 0;
% start in a random location
meanValues = randi(360);
durations = [];
while totalLength < totalSeconds*sampRate
    % generate a duration for current new mean
    newDur = 0;
    while newDur < minDur || newDur > maxDur
        newDur = round(meanDur + stdDur.*randn(1,1));
    end
    durations = [durations newDur];    
    totalLength = totalLength + durations(end);
    if totalLength < totalSeconds*sampRate
        % generate a new mean, if we still need more values
        %meanValues = [meanValues meanValues(end)+jumpValues(randi(nValues))*STD];
        meanValues = [meanValues meanValues(end)+jumpValues(randi(nValues))];
    end
end
% remove entries beyond total seconds
toRemove = totalLength - totalSeconds*sampRate;
durations(end) = durations(end) - toRemove;

stim.meanValues = meanValues;
stim.meanValuesDeg = mod(meanValues,360);
stim.meanDurations = durations;

% generate plottable vector
stim.time = [1:sum(durations)]/sampRate;
stim.meanValueVector = [];
for iEpoch = 1: numel(durations)
    stim.meanValueVector = [stim.meanValueVector ones(1, durations(iEpoch))*stim.meanValues(iEpoch)];
end
stim.meanValueVectorDeg = mod(stim.meanValueVector, 360);

end