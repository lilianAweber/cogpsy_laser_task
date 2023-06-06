function [outstream,poissDlengths] = generate_outstream(params)

% function [outstream,poissDlengths] = generate_outstream(params)
% 
% fields of Params:
% Fs = sampling rate, Hz (default 1000)
% stimDur = stimulation duration, seconds (default 30)
% sigmaStream = standard deviation of Gaussian walk, step each sample (default 2)
% sigmaObs = standard deviation of observation noise, IID at each sample (default 50)
% xStart = initial value of x
% mod360 = %project onto circular trajectory with mod(x,360) (default:off)
% poissDraw = if greater than 0, then x_obs is only resampled with
%           frequency drawn from poisson distribution (with lambda =
%           poissDraw)
%
% generates gaussian random walk with observation noise 
%

try Fs = params.Fs;                     catch, Fs = 1000; params.Fs = Fs; end
try stimDur = params.stimDur;         catch, stimDur = 30; params.stimDur = stimDur; end
try xStart  = params.xStart;          catch, xStart = 0; params.xStart = xStart; end
try sigmaStream = params.sigmaStream;   catch, sigmaStream = 2; params.sigmaStream = sigmaStream; end
try sigmaObs = params.sigmaObs;         catch, sigmaObs = 50; params.sigmaObs = sigmaObs; end
try mod360 = params.mod360;             catch, mod360=0; params.mod360=mod360; end
try poissDraw = params.poissDraw;       catch, poissDraw = 0; end


nSamples = ceil(Fs*stimDur); % number of samples in stimulus stream

%% generate 1D stimulus stream, x

x = nan(1,nSamples);
xObs = nan(1,nSamples);
x(1) = xStart;
xObs(1) = x(1) + randn*sigmaObs;

poissDlengths = [];
if poissDraw>0
    poissDlengths(1) = poissrnd(poissDraw)+1;
    current_samplelength = 1;
end

for i = 2:nSamples
    x(i) = x(i-1) + randn*sigmaStream; % update the stimulus stream, x
    if poissDraw == 0 %update on every sample - NOT poisson distributed samples
        xObs(i) = x(i) + randn*sigmaObs; % observed value, with observation noise added
    elseif current_samplelength==poissDlengths(end) %time to resample
        xObs(i) = x(i) + randn*sigmaObs; % observed value, with observation noise added
        poissDlengths(end+1) = poissrnd(poissDraw)+1;
        current_samplelength = 1;
    else
        xObs(i) = xObs(i-1);
        current_samplelength = current_samplelength + 1;
    end
end

%% now change onto 360-degree axis

if mod360
    x = mod(x,360);
    xObs = mod(xObs,360);
end

%% store outputs
outstream.params = params;
outstream.x = x;
outstream.xObs = xObs;