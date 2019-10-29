Tokenresults = csvread('data/Token_20_15.csv',1,0);
Spiderresults = csvread('data/Spider_20_15.csv',1,0);
COresults = csvread('data/Call me once_20_15.csv',1,0);
LNSresults = csvread('data/Learn New Secret_20_15.csv',1,0);


title('Energy use per agent')
xlabel('Agents')
ylabel('Energy')

agents = Tokenresults(:, 3); hold on;
energy = Tokenresults(:, 7);
p1=plot(agents, energy);

agents = Spiderresults(:, 3);
energy = Spiderresults(:, 7);
p2=plot(agents, energy);

agents = COresults(:, 3);
energy = COresults(:, 7);
p3=plot(agents, energy);

agents = LNSresults(:, 3);
energy = LNSresults(:, 7);
p4=plot(agents, energy);

hold off;

legend([p1, p2, p3, p4], 'Token','Spider','CO','LNS');

print -djpg data/image_20_15.jpg