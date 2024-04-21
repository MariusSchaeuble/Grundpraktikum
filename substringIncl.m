function res = substringIncl(str, start, ende)
res = "";
for i=start:ende
    res = res + extract(str, i);
end
end