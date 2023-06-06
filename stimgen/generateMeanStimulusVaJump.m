function stim = generateMeanStimulusVaJump( totalSeconds, blockDesign, sampRate )
%GENERATESTIMULUS Generates a sequence of mean values and standard
%deviations for a duration of totalSeconds

if nargin == 0
    totalSeconds = 300;
end

if nargin < 2
    % default settings
    jumpValues = [-5 -3 -1 1 3 5]; % in SD of stimulus?
    STD = 20;
    meanDur = 5000;
    stdDur = 1500;
    minDur = 500;
    maxDur = 10000;
    flagPlot = true;
else
    % extract block design info
    jumpValues = blockDesign.jumpValueSet;
    noiseValues = blockDesign.noiseValueSet;
    STD = blockDesign.noiseMean;
    meanDur = blockDesign.durMeanStdMinMax(1)*sampRate;
    stdDur = blockDesign.durMeanStdMinMax(2)*sampRate;
    minDur = blockDesign.durMeanStdMinMax(3)*sampRate;
    maxDur = blockDesign.durMeanStdMinMax(4)*sampRate;
    meanDurNoise = blockDesign.noiseDurMeanStdMinMax(1)*sampRate;
    stdDurNoise = blockDesign.noiseDurMeanStdMinMax(2)*sampRate;
    minDurNoise = blockDesign.noiseDurMeanStdMinMax(3)*sampRate;
    maxDurNoise = blockDesign.noiseDurMeanStdMinMax(4)*sampRate;
    flagPlot = true;
end
if nargin < 3
    sampRate = 1000;
end

nValues = numel(jumpValues);
nNoiseValues = numel(noiseValues);

% Generate mean values and durations
totalLength = 0;
meanValues = 0;
durations = [];
while totalLength < totalSeconds*sampRate
    % generate a new mean
    meanValues = [meanValues meanValues(end)+jumpValues(randi(nValues))*STD];
    % generate a duration for the new mean
    newDur = 0;
    while newDur < minDur || newDur > maxDur
        newDur = round(meanDur + stdDur.*randn(1,1));
    end
    durations = [durations newDur];    
    totalLength = totalLength + durations(end);
end
meanValues(1) = [];
% move starting point to a random value
meanValues = meanValues + randi(360);
stim.meanValues = meanValues;
stim.meanValuesDeg = mod(meanValues,360);
stim.meanDurations = durations;

% Generate noise values and durations
noiseTotalLength = 0;
stdValues = [];
noiseDurations = [];
while noiseTotalLength < totalLength
    % generate a new mean
    stdValues = [stdValues noiseValues(randi(nNoiseValues))];
    % generate a duration for the new noise
    newDur = 0;
    while newDur < minDurNoise || newDur > maxDurNoise
        newDur = round(meanDurNoise + stdDurNoise.*randn(1,1));
    end
    noiseDurations = [noiseDurations newDur];    
    noiseTotalLength = noiseTotalLength + noiseDurations(end);
end
tooMuchNoise = noiseTotalLength - totalLength;
tooMuchNoiseTotal = tooMuchNoise;
samplesRemoved = 0;
while samplesRemoved < tooMuchNoiseTotal
    if tooMuchNoise < noiseDurations(end)
        noiseDurations(end) = noiseDurations(end) - tooMuchNoise;
        samplesRemoved = samplesRemoved + tooMuchNoise;
    else
        samplesToRemove = noiseDurations(end);
        noiseDurations(end) = [];
        stdValues(end) = [];
        tooMuchNoise = tooMuchNoise - samplesToRemove;
        samplesRemoved = samplesRemoved + samplesToRemove;
    end
end
% sanity check
if sum(durations) ~= sum(noiseDurations)
    error('total duration must match between noise and mean values');
end
stim.stdValues = stdValues;
stim.stdValuesDeg = mod(stdValues,360);
stim.stdDurations = noiseDurations;


% generate plottable vector
stim.time = [1:sum(durations)]/sampRate;
stim.meanValueVector = [];
for iEpoch = 1: numel(durations)
    stim.meanValueVector = [stim.meanValueVector ones(1, durations(iEpoch))*stim.meanValues(iEpoch)];
end
stim.meanValueVectorDeg = mod(stim.meanValueVector, 360);
stim.stdValueVector = [];
for iEpoch = 1: numel(noiseDurations)
    stim.stdValueVector = [stim.stdValueVector ones(1, noiseDurations(iEpoch))*stim.stdValues(iEpoch)];
end
stim.stdValueVectorDeg = mod(stim.stdValueVector, 360);

if flagPlot
    figure; 
    plot(stim.time, stim.meanValueVector); hold on, 
    plot(stim.time, stim.meanValueVector+stim.stdValueVector, '-r');
    plot(stim.time, stim.meanValueVector-stim.stdValueVector, '-r');
    figure; 
    plot(stim.time, stim.meanValueVector); hold on, 
    plot(stim.time, stim.stdValueVector, '-r');
end

% work out epochs with different generative stats
isChangePointMean = [0 diff(stim.meanValueVector)~=0];
isChangePointNoise = [0 diff(stim.stdValueVector)~=0];
isChangePoint = isChangePointMean | isChangePointNoise;
changePoints = find(isChangePoint);
changePoints = [1 changePoints numel(stim.meanValueVector)+1];
for iCP = 1: numel(changePoints)-1
    stim.epochs(iCP).mean = stim.meanValueVector(changePoints(iCP));
    stim.epochs(iCP).std = stim.stdValueVector(changePoints(iCP));
    stim.epochs(iCP).duration = changePoints(iCP+1)-changePoints(iCP);
end
stim.changePointsMean = find(isChangePointMean);
stim.changePointsStd = find(isChangePointNoise);


    
end