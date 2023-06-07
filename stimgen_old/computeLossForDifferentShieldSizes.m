function hyLoss = computeLossForDifferentShieldSizes( shieldSizes, trueSdVals, lossFactor, sizeFactors, nTrials )

for i=1:3
    for j=1:3
        usedShield = shieldSizes(i);
        trueSD = trueSdVals(j);
        relShieldSize = usedShield/trueSD;
        expHit = erf(relShieldSize/sqrt(2));
        hyLoss(i,j) = (1-expHit)*nTrials*lossFactor + expHit*nTrials*lossFactor/sizeFactors(i);
    end
end

end