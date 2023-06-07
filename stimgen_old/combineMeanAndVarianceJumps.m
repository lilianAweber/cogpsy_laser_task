function stim = combineMeanAndVarianceJumps( stimMean, stimVar )
%COMBINEMEANANDVARIANCEJUMPS Combines mean jumps and variance jumps into
%one mean stimulus stream. Also works out epochs with constant stats for
%feeding into generateBlockStimulus.

% sanity check
if sum(stimMean.meanDurations) ~= sum(stimVar.stdDurations)
    error('total duration must match between noise and mean values');
end

% add all fields together
stim = stimMean;
fieldsVar = fieldnames(stimVar);
for curr_field = fieldsVar(:)'  
  stim = setfield(stim, curr_field{:}, getfield(stimVar, curr_field{:}));
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

% plot the combined stimulus
figure; 
plot(stim.time, stim.meanValueVector); hold on, 
plot(stim.time, stim.meanValueVector+stim.stdValueVector, '-r');
plot(stim.time, stim.meanValueVector-stim.stdValueVector, '-r');
figure; 
plot(stim.time, stim.meanValueVector); hold on, 
plot(stim.time, stim.stdValueVector, '-r');

end