function [ seq, staDev ] = generateToneBlockSequence( blockDuration, design )

%toneUnitDuration = design.toneDuration + design.isiDuration;
toneUnitDuration = design.soaDuration;
nTones = ceil(blockDuration * 60 * 1000 / toneUnitDuration);

nDeviants = round(nTones * design.devProb);

switch design.condition
    case 'stable'
        nDevInSeq = 0;
        while nDevInSeq > nDeviants + design.maxDevDiff || nDevInSeq < nDeviants - design.maxDevDiff
            tonesInSequence = 0;
            seq = [];
            while tonesInSequence < nTones
                newDistance = design.distances(randi(numel(design.distances)));
                seq = [seq zeros(1, newDistance) 1];
                tonesInSequence = numel(seq);
            end
            seq = seq(1:nTones);
            nDevInSeq = sum(seq);
        end
        figure; histogram(diff(find(seq))-1)
        seq = seq+1;
        figure; plot(seq, 'o'); title('Stable sequence')
        staDev = cell(1, numel(seq));
        staDev(seq==1) = {'S'};
        staDev(seq==2) = {'D'};
    case 'volatile'
        % start by generating a stable sequence
        design.condition = 'stable';
        [seq, staDev] = generateToneBlockSequence(blockDuration, design);
        % introduce reversals every few deviants
        nTonesCovered = 0;
        seq = seq-1;
        devInSeq = find(seq);
        seq(seq<1) = -1;
        idxDevInDev = 1;
        flipSign = randi(2) -1;
        while nTonesCovered < nTones
            % draw a new block duration
            blockLength = design.blockDurations(randi(numel(design.blockDurations)));
            if idxDevInDev + blockLength >= numel(devInSeq)
                nTonesCovered = nTones;
                break
            end
            if flipSign
                seq(devInSeq(idxDevInDev)+1 : devInSeq(idxDevInDev+blockLength)) = ...
                    -1 * seq(devInSeq(idxDevInDev)+1 : devInSeq(idxDevInDev+blockLength));
                flipSign = false;
            else
                flipSign = true;
            end
            idxDevInDev = idxDevInDev + blockLength;
            %if idxDevInDev >= numel(devInSeq)
            %    nTonesCovered = nTones;
            %else
            nTonesCovered = devInSeq(idxDevInDev);
            %end
        end
        seq(seq<0) = 0;
        seq = seq +1;
        figure; plot(seq, 'o'); title('Volatile sequence')
end
end