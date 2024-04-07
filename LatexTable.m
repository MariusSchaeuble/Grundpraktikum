function res = LatexTable(spalten)
s = size(spalten);
res = "copy below" + newline;
res = res + "\begin{table}[H]";
res = res + newline + "\centering";
res = res + newline + "\label{LABEL}";
res = res + newline + "\caption{CAPTION}";

res = res + newline + "\begin{tabular}{|";
for i=1:s(2)
    res = res + "c|";
end
res = res + "}";

res = res + newline + "\hline";

res = res + newline;
for i=1:s(2)-1
    res = res + "Bezeichnung" + num2str(i) + " & ";
end
res = res + "Bezeichnung" + num2str(s(2));
res = res + "\\";
 
res = res + newline + "\hline";
res = res + newline;


for i=1:s(1)
    res = res + newline;
    for j=1:s(2)-1
        res = res + "$" + spalten(i, j) + "$" + " & ";
    end
    res = res + "$" + spalten(i, s(2)) + "$";
    res = res + "\\";
end


res = res + newline;
res = res + newline + "\hline";
res = res + newline + "\end{tabular}";
res = res + newline + "\end{table}" + newline;

end