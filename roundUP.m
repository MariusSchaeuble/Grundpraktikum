function res = roundUP(zahl)
r = round(zahl);
if r>zahl
    res = r;
else
    res = r+1;
end
end