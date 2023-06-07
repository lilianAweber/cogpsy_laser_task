% script to write a stimulus stream into a CSV file for subsequent reading
% by PsychoPy

rng(2); % for reproducibility of streams

params.Fs = 60;           % 60 Hz refresh rate
params.stimDur = 300;     % generate 5 minutes worth of stimulus 
params.xStart = rand*360; % seed with a random value between 0 and 360
params.sigmaStream = 3;   % standard deviation of gaussian walk on each timestep
params.sigmaObs = 25;     % standard deviation of observation noise (in degrees)
params.mod360=true;       % constrain random walk to lie between 0 and 360 degrees
params.poissDraw = 15;    % resampling rate of stimstream 

outstream = generate_outstream(params);

csvwrite('rotation_stream.csv',[outstream.x; outstream.xObs]');