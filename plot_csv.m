Tokenresults = csvread('data/toke_20_15.csv',1,0);
Spiderresults = csvread('data/spider_20_15.csv',1,0);
COresults = csvread('data/callmeonce_20_15.csv',1,0);
LNSresults = csvread('data/toke_20_15.csv',1,0);

hold on;
title('Test results')
xlabel('Agents')
ylabel('Energy')
agents = Tokenresults(:, 3);
energy = Tokenresults(:, 6);
plot(agents, energy);

agents = Spiderresults(:, 3);
energy = Spiderresults(:, 6);
plot(agents, energy);

agents = COresults(:, 3);
energy = COresults(:, 6);
plot(agents, energy);

