function stim = generateMeanStimulus( totalSeconds, blockDesign, sampRate )
%GENERATESTIMULUS Generates a sequence of rewards and punishments for three
%patches

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
    STD = blockDesign.noise;
    meanDur = blockDesign.durMeanStdMinMax(1)*sampRate;
    stdDur = blockDesign.durMeanStdMinMax(2)*sampRate;
    minDur = blockDesign.durMeanStdMinMax(3)*sampRate;
    maxDur = blockDesign.durMeanStdMinMax(4)*sampRate;
    flagPlot = false;
end
if nargin < 3
    sampRate = 1000;
end

nValues = numel(jumpValues);


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

if flagPlot
    figure; 
    plot(stim.timeVector, stim.meanValueVector);
end

end