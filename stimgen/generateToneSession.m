function session = generateToneSession( sessName, conditions )

session.nBlocks = 4;
session.blockDuration = 3; % in min
session.blockSequence = conditions; 

stableDesign = mmnDesign('stable', 0.15);
volatileDesign = mmnDesign('volatile', 0.15);

for iBlock = 1: session.nBlocks
    session.blocks(iBlock).condID = session.blockSequence(iBlock);
    switch session.blockSequence(iBlock)
        case 1
            session.blocks(iBlock).condition = 'stable';
            session.blocks(iBlock).design = stableDesign;
        case 2
            session.blocks(iBlock).condition = 'volatile';
            session.blocks(iBlock).design = volatileDesign;
    end
    [session.blocks(iBlock).seq, session.blocks(iBlock).staDev] = ...
        generateToneBlockSequence(session.blockDuration, session.blocks(iBlock).design);
    session.blocks(iBlock).seqStats = computeToneSequenceStats(...
        session.blocks(iBlock).seq, session.blocks(iBlock).staDev);
end

% for stable blocks, we want to flip the assignment of standard and deviant
% to tone 1 vs tone 2 every second block
doFlip = randi(2)-1;
for iBlock = 1: session.nBlocks
    if session.blocks(iBlock).condID == 1
        if doFlip
            origSeq = session.blocks(iBlock).seq;
            newSeq = origSeq;
            newSeq(origSeq==1) = 2;
            newSeq(origSeq==2) = 1;
            session.blocks(iBlock).seq = newSeq;
            doFlip = false;
        else
            doFlip = true;
        end
    end
end

save([sessName '_session.mat'], 'session');

writeBlockCsvFiles(session, sessName);

end


function writeBlockCsvFiles( session, sessName )

for iBlock = 1: session.nBlocks
    fileID = fopen([sessName '_block' num2str(iBlock) '.csv'], 'w');
    fprintf(fileID,'%s\n', 'toneType');
    fprintf(fileID,'%i\n', session.blocks(iBlock).seq);
    fclose(fileID);
end

end