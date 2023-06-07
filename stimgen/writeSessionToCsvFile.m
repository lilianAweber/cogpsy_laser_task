function writeSessionToCsvFile( session, sessName, sequenceRoot )
%WRITESESSIONTOCSVFILE Writes out one csv file per block within a session
%to be used in the psychopy laser experiment.

for iBlock = 1: session.nBlocks
    data = [session.blocks(iBlock).stim.meanValueVectorDeg; ...
        session.blocks(iBlock).stim.valueVectorDeg'; ...
        session.blocks(iBlock).stim.stdValueVectorDeg];
    
    fileID = fopen(fullfile(sequenceRoot, [sessName '_block' num2str(iBlock) '.csv']), 'w');
    fprintf(fileID,'%8s,%7s,%8s\n', 'true_pos','obs_pos','true_var');
    fprintf(fileID,'%3d,%3d,%2d\n', data);
    fclose(fileID);
end

