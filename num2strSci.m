function res = num2strSci(zahl)
str = num2str(zahl);
res = str;
f = strfind(str, "e");
if ~isempty(f)
    %potenzdarstellung
    occ = f(1);
    res = substringIncl(str, 1, occ-1) + " \cdot 10^{" + substringIncl(str, occ+1, strlength(str)) + "}";
end

end