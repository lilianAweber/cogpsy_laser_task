function stats = computeToneSequenceStats( seq, staDev )
%COMPUTETONESEQUENCESTATS Computes a few descriptive statistics for a tone
%sequence as used in the COGPSY MMN task.

isDev = strcmp(staDev,'D');
stats.nDeviants = sum(isDev);
stats.nStandards = sum(strcmp(staDev,'S'));
stats.nTones = numel(seq);
stats.pDeviants = stats.nDeviants/stats.nTones;

binSeq = zeros(1, stats.nTones);
binSeq(strcmp(staDev, 'D')) = 1;
stats.trainLengthSeq = diff(find(binSeq))-1;
stats.trainLengths = unique(stats.trainLengthSeq);
stats.trainLengthFreq = histcounts(stats.trainLengthSeq, 'binmethod', 'integers');

% how many deviants are starting a new rule (i.e., reversals)
devIdx = find(isDev);
isReversalDev = zeros(stats.nDeviants, 1);
for iDev = 1: stats.nDeviants-1
    if seq(devIdx(iDev)) == seq(devIdx(iDev) +1)
        isReversalDev(iDev, 1) = 1;
    end
end
stats.nReversals = sum(isReversalDev);
if stats.nReversals > 0
    stats.phaseLengthSeq = diff(find(isReversalDev))-1;
    stats.phaseLengths = unique(stats.phaseLengthSeq);
    stats.phaseLengthFreq = histcounts(stats.phaseLengthSeq, 'binmethod', 'integers');
else
    stats.phaseLengthSeq = stats.nTones;
    stats.phaseLengths = stats.nTones;
    stats.phaseLengthFreq = 1;    
end

end