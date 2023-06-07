function stim = generateVarianceJumps( totalSeconds, blockDesign, sampRate )
%GENERATEVARIANCEJUMPS Generates a sequence of standard deviations based on
%blockDesign for a duration of totalSeconds

if nargin == 0
    totalSeconds = 300;
end

if nargin < 2
    % default settings
    sampRate = 1000;
    noiseValues = [10 10 20 30];
    meanDurNoise = 15*sampRate;
    stdDurNoise = 3*sampRate;
    minDurNoise = 5*sampRate;
    maxDurNoise = 20*sampRate;
    flagPlot = true;
else
    % extract block design info
    noiseValues = blockDesign.noiseValueSet;
    meanDurNoise = blockDesign.noiseDurMeanStdMinMax(1)*sampRate;
    stdDurNoise = blockDesign.noiseDurMeanStdMinMax(2)*sampRate;
    minDurNoise = blockDesign.noiseDurMeanStdMinMax(3)*sampRate;
    maxDurNoise = blockDesign.noiseDurMeanStdMinMax(4)*sampRate;
    flagPlot = false;
end
if nargin < 3
    sampRate = 1000;
end

nNoiseValues = numel(noiseValues);

% Generate noise values and durations
noiseTotalLength = 0;
stdValues = [];
noiseDurations = [];
while noiseTotalLength < totalSeconds*sampRate
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
% remove entries beyond total seconds
toRemove = noiseTotalLength - totalSeconds*sampRate;
noiseDurations(end) = noiseDurations(end) - toRemove;

stim.stdValues = stdValues;
stim.stdValuesDeg = mod(stdValues,360);
stim.stdDurations = noiseDurations;

% generate plottable vector
stim.stdTime = [1:sum(noiseDurations)]/sampRate;
stim.stdValueVector = [];
for iEpoch = 1: numel(noiseDurations)
    stim.stdValueVector = [stim.stdValueVector ones(1, noiseDurations(iEpoch))*stim.stdValues(iEpoch)];
end
stim.stdValueVectorDeg = mod(stim.stdValueVector, 360);

if flagPlot
    figure; 
    plot(stim.stdTime, stim.stdValueVector, '-r');
end    
end