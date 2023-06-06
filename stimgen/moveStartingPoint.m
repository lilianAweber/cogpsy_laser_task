function stim = moveStartingPoint( stim )
%MOVESTARTINGPOINT Moves the starting point on the wheel for a given mean
%stimulus sequence.

moveSize = randi(90)+90;

stim.meanValues = stim.meanValues + moveSize;
stim.meanValueVector = stim.meanValueVector + moveSize;

startPoint = stim.meanValues(1);

diff2start = stim.meanValues - startPoint;
stim.meanValues = stim.meanValues - 2*diff2start;

diff2startVec = stim.meanValueVector - startPoint;
stim.meanValueVector = stim.meanValueVector - 2*diff2startVec;

stim.meanValuesDeg = mod(stim.meanValues,360);
stim.meanValueVectorDeg = mod(stim.meanValueVector,360);

end