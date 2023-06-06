% script to write a stimulus stream into a CSV file for subsequent reading
% by PsychoPy

rng(2); % for reproducibility of streams

params.Fs = 60;           % 60 Hz refresh rate
params.stimDur = 60;     % generate 5 minutes worth of stimulus 
params.xStart = rand*360; % seed with a random value between 0 and 360

params.mod360=true;       % constrain random walk to lie between 0 and 360 degrees
params.poissDraw = 15;    % resampling rate of stimstream 

figure;

% block type 1: low noise, low volatility
params.sigmaStream = 2;   % standard deviation of gaussian walk on each timestep
params.sigmaObs = 10;     % standard deviation of observation noise (in degrees)
outstream = generate_outstream(params);
csvwrite('lowlow.csv',[outstream.x; outstream.xObs]');
save('lowlow.mat', 'outstream');
subplot(2, 2, 1); 
plot(outstream.xObs, '-k')
hold on; plot(outstream.x, '-y', 'linewidth', 2)

% block type 2: low noise, high volatility
params.sigmaStream = 8;   % standard deviation of gaussian walk on each timestep
params.sigmaObs = 10;     % standard deviation of observation noise (in degrees)
outstream = generate_outstream(params);
csvwrite('lowhigh.csv',[outstream.x; outstream.xObs]');
save('lowhigh.mat', 'outstream');
subplot(2, 2, 2); 
plot(outstream.xObs, '-k')
hold on; plot(outstream.x, '-y', 'linewidth', 2)

% block type 3: high noise, low volatility
params.sigmaStream = 2;   % standard deviation of gaussian walk on each timestep
params.sigmaObs = 30;     % standard deviation of observation noise (in degrees)
outstream = generate_outstream(params);
csvwrite('highlow.csv',[outstream.x; outstream.xObs]');
save('highlow.mat', 'outstream');
subplot(2, 2, 3); 
plot(outstream.xObs, '-k')
hold on; plot(outstream.x, '-y', 'linewidth', 2)

% block type 4: high noise, high volatility
params.sigmaStream = 8;   % standard deviation of gaussian walk on each timestep
params.sigmaObs = 30;     % standard deviation of observation noise (in degrees)
outstream = generate_outstream(params);
csvwrite('highhigh.csv',[outstream.x; outstream.xObs]');
save('highhigh.mat', 'outstream');
subplot(2, 2, 4); 
plot(outstream.xObs, '-k')
hold on; plot(outstream.x, '-y', 'linewidth', 2)
