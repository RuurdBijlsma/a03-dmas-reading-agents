Tokenresults = csvread('data/toke_20_15.csv',1,0);
Spiderresults = csvread('data/spider_20_15.csv',1,0);
COresults = csvread('data/callmeonce_20_15.csv',1,0);
LNSresults = csvread('data/LNS_20_15.csv',1,0);


title('Test results')
xlabel('Agents')
ylabel('Energy')

agents = Tokenresults(:, 3); hold on;
energy = Tokenresults(:, 6);
p1=plot(agents, energy);

agents = Spiderresults(:, 3);
energy = Spiderresults(:, 6);
p2=plot(agents, energy);

agents = COresults(:, 3);
energy = COresults(:, 6);
p3=plot(agents, energy);

agents = LNSresults(:, 3);
energy = LNSresults(:, 6);
p4=plot(agents, energy);

hold off;

legend([p1, p2, p3, p4], 'Token','Spider','CO','LNS');