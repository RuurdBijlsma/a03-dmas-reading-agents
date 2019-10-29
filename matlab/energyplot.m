function energyplot(plotTitle, fileName, energyColumn)
    clf('reset')

    title(plotTitle)
    xlabel("Agents")
    ylabel("Energy")

    iterations = 50
    repeats = 20
    protocols = {"Token", "Spider", "Call me once", "Learn new secret"}
    colors = {'r','g','b','m'}
    plots = [];


    hold on;
    for i = 1:4
        protocol = protocols(i);
        color = colors(i);

        results = csvread(strcat("../data/", protocol{1}, "_", mat2str(iterations), "_", mat2str(repeats), ".csv"), 1, 0);

        agents = results(:, 3);
        energy = results(:, energyColumn);

        plots = [plots plot(agents, energy, color)];
    end
    hold off;


    legend(plots, protocols{:});
    saveas(plots(1), strcat("../data/", fileName, "_", mat2str(iterations), "_", mat2str(repeats), ".png"))
end