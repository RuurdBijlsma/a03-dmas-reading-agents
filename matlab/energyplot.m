function energyplot(plotTitle, fileName, energyColumn, iterations, repeats, readCost)
%    Reset figure to make sure no other information is on there
    clf('reset')

%   Title should reflect what's in the graph
    title(strcat(plotTitle, " (read cost: ", mat2str(readCost), ")"))
    xlabel("Agents")
    ylabel("Energy")

    protocols = {"Token", "Spider", "Call me once", "Learn new secret"};
%    Colours have to be given explicitely, to make sure all six graphs are consistent color-wise.
    colors = {'r','g','b','m'};
    plots = [];


    hold on;
    for i = 1:4
        protocol = protocols(i);
        color = colors(i);

        results = csvread(strcat(
            "../data/", protocol{1},
            "_", mat2str(readCost),
            "_", mat2str(iterations),
            "_", mat2str(repeats), ".csv"
        ), 1, 0);

        agents = results(:, 3);
        energy = results(:, energyColumn);

%        Add new data to graph
        plots = [plots plot(agents, energy, color)];
    end
    hold off;

    imageLocation = strcat("../data/", fileName, "_", mat2str(readCost), "_", mat2str(iterations), "_", mat2str(repeats), ".png");
    strcat("Saved image to ", imageLocation)

    legend(plots, protocols{:});
    saveas(plots(1), imageLocation)
end