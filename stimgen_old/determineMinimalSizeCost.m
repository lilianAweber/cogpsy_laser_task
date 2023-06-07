function minSizeCost = determineMinimalSizeCost( sd1, sd2, hit1Cost )

nTrials = 200;
lossFactor =1;

hits1 = nTrials*erf(sd1/sqrt(2));
hits2 = nTrials*erf(sd2/sqrt(2));

price1 = (nTrials-hits1)*lossFactor + hits1*hit1Cost;
price2 = (nTrials-hits2)*lossFactor;

priceGain = price1-price2;
minPricePerHit = priceGain/hits2;
%hitGain = (hits2-hits1)*lossFactor;
%minSizeCost = hits2/hitGain;
minSizeCost = minPricePerHit;
end