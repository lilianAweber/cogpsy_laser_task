load('MainSession1.mat')
bData = session.blocks(2).stim;

shieldSize = bData.stdValueVector;

cp = diff(bData.valueVector)~=0;
cp = [true; cp];

valAtCp = bData.valueVector(cp);
meanAtCp = bData.meanValueVector(cp);
ssAtCp = shieldSize(cp);
peAtCp = valAtCp-meanAtCp';
absPeAtCp = abs(peAtCp);
losses = [absPeAtCp-ssAtCp']>0;
sum(losses)

figure; plot(absPeAtCp); hold on; plot(ssAtCp)

lossFactor = 0.003;
loss = computeBlockLoss(absPeAtCp, ssAtCp, lossFactor);

% Previous experiment parameters
trueSdVals = [10 20 30];
shieldSizes = [12.5 22.5 32.5];
sizeFactors = [inf 2.25 1.625];

shieldSdVals = shieldSizes./trueSdVals;
expectedMisses = erf(shieldSdVals/sqrt(2));

nTrials = 1;

hyLossPrev = computeLossForDifferentShieldSizes(shieldSizes, trueSdVals, ...
    lossFactor, sizeFactors, nTrials);

% New parameters
lossFactor = 0.003;
trueSdVals = [10 20 30];
shieldSizes = [10 20 30];
sizeFactors = [inf 3 2];
nTrials = 550;

hyLoss = computeLossForDifferentShieldSizes(shieldSizes, trueSdVals, ...
    lossFactor, sizeFactors, nTrials);

% Alternative
shieldSizes = [10 20 60];
sizeFactors = [inf 3 1.5];
trueSdVals = [10 20 40];