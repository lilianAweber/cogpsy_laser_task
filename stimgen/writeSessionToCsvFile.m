function writeSessionToCsvFile( session, sessName )

for iBlock = 1: session.nBlocks
    csvwrite([sessName '_block' num2str(iBlock) '.csv'], [session.blocks(iBlock).stim.meanValueVectorDeg; session.blocks(iBlock).stim.valueVectorDeg'; session.blocks(iBlock).stim.stdValueVectorDeg]');
end