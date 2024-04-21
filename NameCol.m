function res = NameCol(n)
res = strings(n, 1);
for i=1:n
    res(i) = "N_{\mathrm{" + num2str(i) + "}}";
end
end